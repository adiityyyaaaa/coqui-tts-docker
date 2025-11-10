from TTS.api import TTS
import gradio as gr

# Available models for different voices/languages
MODELS = {
    "English (Female)": "tts_models/en/ljspeech/tacotron2-DDC",
    "English (Male)": "tts_models/en/vctk/vits",
    "Multilingual (YourTTS)": "tts_models/multilingual/multi-dataset/your_tts",
    "Hindi": "tts_models/multilingual/multi-dataset/your_tts",  # same model, but detects Hindi automatically
}

# Cache models to avoid reloading every time
loaded_models = {}

def synthesize(text, voice_choice):
    model_name = MODELS[voice_choice]
    if model_name not in loaded_models:
        print(f"🔄 Loading model: {model_name}")
        loaded_models[model_name] = TTS(model_name)
    tts = loaded_models[model_name]

    output_path = f"tts_output_{voice_choice.replace(' ', '_')}.wav"
    tts.tts_to_file(text=text, file_path=output_path)
    return output_path

iface = gr.Interface(
    fn=synthesize,
    inputs=[
        gr.Textbox(lines=4, placeholder="Type text here..."),
        gr.Dropdown(list(MODELS.keys()), label="Select Voice/Language"),
    ],
    outputs=gr.Audio(label="Generated Speech"),
    title="Aditya's Coqui TTS",
    description="Switch between multiple voices and languages. All local, no API cost!",
)

if __name__ == "__main__":
    iface.launch(server_name="0.0.0.0", server_port=7860)
