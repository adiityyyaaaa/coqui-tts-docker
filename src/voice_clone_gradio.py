import gradio as gr
from TTS.api import TTS
import os

# Load YourTTS model (multilingual + voice cloning)
MODEL_NAME = "tts_models/multilingual/multi-dataset/your_tts"
tts = TTS(MODEL_NAME)

def clone_and_speak(text, voice_file, language):
    """Clone uploaded voice and synthesize text."""
    if voice_file is None or text.strip() == "":
        return None
    output_path = "cloned_output.wav"
    # Voice cloning: supply uploaded audio file path
    tts.tts_to_file(
        text=text,
        speaker_wav=voice_file,
        language=language,
        file_path=output_path
    )
    return output_path

iface = gr.Interface(
    fn=clone_and_speak,
    inputs=[
        gr.Textbox(lines=4, label="Text to Speak"),
        gr.Audio(label="Upload Voice Sample", type="filepath"),
        gr.Dropdown(
            ["en", "hi", "fr", "es"],
            value="en",
            label="Language Code"
        ),
    ],
    outputs=gr.Audio(label="Cloned Voice Output"),
    title="Aditya’s AI Voice Cloner",
    description=(
        "Upload a 5–10 second voice sample and type any text to hear it "
        "in your cloned voice! Powered by Coqui YourTTS."
    ),
)

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", server_port=7860)
