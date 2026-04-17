# 🎙️ Rao - AI Voice Assistant

Rao is a Python-based AI voice assistant that listens to user input, processes it using an AI language model, and responds with synthesized speech. It also supports basic web interaction such as fetching website titles.

---

## 🚀 Features

* 🎤 Voice input using microphone
* 🧠 AI-generated responses
* 🔊 Text-to-speech output
* 🌐 Web scraping (fetch website titles)
* ⚡ Real-time interaction loop

---

## 🛠️ Tech Stack

* Python 3.x
* SpeechRecognition (voice input)
* pyttsx3 (text-to-speech)
* OpenAI API (AI responses)
* Requests + BeautifulSoup (web scraping)

---

## 📂 Project Structure

```
.
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone <your-repo-link>
cd <your-folder>
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

## 🔑 Setup API Key

Open `main.py` and replace:

```
openai.api_key = "YOUR_API_KEY"
```

with your actual API key.

---

## ▶️ Usage

Run the application:

```
python main.py
```

Then say:

```
Rao
```

The assistant will start listening and respond accordingly.

---

## ⚠️ Notes

* Ensure your microphone is properly configured
* Update `device_index` in code if needed
* Internet connection required for speech recognition and AI responses

---

## 🧠 Future Improvements

* GUI interface (Tkinter / Web app)
* Wake word detection without manual trigger
* Multi-language support
* Integration with APIs (weather, news, etc.)

---

## 📜 License

This project is for educational and experimental purposes.

---

## 👨‍💻 Author

Developed as part of an AI/ML learning project.
