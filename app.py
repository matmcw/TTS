import gradio as gr
from datetime import datetime
from pathlib import Path

from engine import TTSEngine

engine = TTSEngine()
OUT_DIR = Path(__file__).parent / "out"
OUT_DIR.mkdir(exist_ok=True)


def generate(text, voice_ref_path, exaggeration, cfg_weight, temperature, post_process):
    if not text.strip():
        raise gr.Error("Please enter some text.")
    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".wav"
    output_path = OUT_DIR / filename
    engine.synthesize(
        text=text,
        voice_reference=voice_ref_path if voice_ref_path else None,
        exaggeration=exaggeration,
        cfg_weight=cfg_weight,
        temperature=temperature,
        post_process=post_process,
        output_path=str(output_path),
    )
    return str(output_path)


def on_voice_cleared(voice_ref_path, text, exaggeration, cfg_weight, temperature, post_process):
    if voice_ref_path is None and text.strip():
        return generate(text, None, exaggeration, cfg_weight, temperature, post_process)
    return gr.update()


with gr.Blocks(title="TTS") as demo:
    gr.Markdown("# Text to Speech")

    with gr.Row():
        with gr.Column(scale=3):
            text_input = gr.Textbox(
                label="Text",
                placeholder="Enter any text to synthesize...",
                lines=10,
            )
            generate_btn = gr.Button("Generate", variant="primary", size="lg")

        with gr.Column(scale=2):
            audio_output = gr.Audio(label="Output", type="filepath", autoplay=True)
            voice_ref = gr.Audio(
                label="Voice Reference (optional — upload a clip to clone a voice)",
                type="filepath",
                sources=["upload"],
            )
            with gr.Accordion("Settings", open=False):
                exaggeration = gr.Slider(
                    minimum=0.25, maximum=2.0, value=0.5, step=0.05,
                    label="Exaggeration",
                    info="Emotional intensity. 0.35 = calm, 0.5 = default, 0.75 = expressive, 1.0+ = dramatic.",
                )
                cfg_weight = gr.Slider(
                    minimum=0.05, maximum=1.0, value=0.5, step=0.05,
                    label="Guidance",
                    info="Pacing control. Lower = faster/more creative. Reduce when raising exaggeration.",
                )
                temperature = gr.Slider(
                    minimum=0.05, maximum=1.5, value=0.8, step=0.05,
                    label="Temperature",
                    info="Randomness. Lower = consistent delivery. Higher = more varied prosody.",
                )
                post_process = gr.Checkbox(
                    label="Post-processing",
                    value=False,
                    info="Adds subtle grain and early reflections for a more natural sound.",
                )

    inputs = [text_input, voice_ref, exaggeration, cfg_weight, temperature, post_process]

    generate_btn.click(fn=generate, inputs=inputs, outputs=audio_output)
    text_input.submit(fn=generate, inputs=inputs, outputs=audio_output)
    voice_ref.change(
        fn=on_voice_cleared,
        inputs=[voice_ref, text_input, exaggeration, cfg_weight, temperature, post_process],
        outputs=audio_output,
    )

if __name__ == "__main__":
    demo.launch(allowed_paths=[str(OUT_DIR)])
