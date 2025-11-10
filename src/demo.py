from TTS.api import TTS
import soundfile as sf

def main():
    model_name = "tts_models/en/ljspeech/tacotron2-DDC"
    tts = TTS(model_name)

    text = "Hello! This is Aditya's custom Coqui TTS engine running inside Docker."
    tts.tts_to_file(text=text, file_path="output.wav")

    print("✅ Audio generated successfully: output.wav")

if __name__ == "__main__":
    main()
