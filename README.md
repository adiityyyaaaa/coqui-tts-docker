# 🎙️ Coqui TTS Docker – Local Text-to-Speech & Voice Cloning

Run your own **AI text-to-speech and voice cloning** model locally using [Coqui TTS](https://github.com/coqui-ai/TTS).  
No API costs. No data sharing. 100% local inference in Docker.

---

## 🚀 Features

- 🎤 High-quality TTS for multiple voices and languages  
- 🧠 Optional voice cloning support (your voice or any dataset)  
- 🐳 Fully containerized with Docker (just run and go)  
- ⚙️ Gradio web UI for quick testing and local playback  
- 💾 Works offline — no external API required  

---

## 🛠️ Installation & Usage

### **1. Clone the repo**
```bash
git clone https://github.com/adiityyyaaaa/coqui-tts-docker.git
cd coqui-tts-docker

2. Build Docker image
docker build -t coqui-tts:latest .

3. Run the app
docker run -p 7860:7860 coqui-tts:latest


Open your browser at 👉 http://localhost:7860
You’ll see the Gradio interface — type text and generate speech!

🧬 Voice Cloning (Optional)

To enable cloning:

1  Place your .wav voice samples inside /app/src/voices/

2  Edit voice_clone_gradio.py with your file names

3  Rebuild and rerun Docker

🧱 Project Structure
📂 coqui-tts-docker/
 ┣ 📜 Dockerfile
 ┣ 📜 requirements.txt
 ┣ 📂 src/
 ┃ ┣ 🎙️ gradio_app.py         → Gradio interface for TTS
 ┃ ┣ 🧬 voice_clone_gradio.py  → Voice cloning setup
 ┃ ┣ 🧪 demo.py                → Example script
 ┣ 📜 README.md
 ┗ 📜 .dockerignore

🏗️ Built With

Coqui TTS

Gradio

Docker

Python 3.10

📄 License

MIT License © 2025 Aditya Singh