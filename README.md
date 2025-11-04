# A.I.D
# 🌍 Project A.I.D. (Autonomous Image Description)

> Making images accessible in Indian languages - because accessibility shouldn't be limited to English.

![Project A.I.D. Banner](https://via.placeholder.com/800x200/667eea/ffffff?text=Project+A.I.D.+-+Accessible+Image+Descriptions)

## 🎯 The Problem

**450 million people** in India speak Hindi or Bengali as their primary language. When visually impaired users rely on screen readers, most image descriptions are only available in English - creating a massive accessibility gap.

Current solutions:
- ❌ Image alt-text is usually in English only
- ❌ Screen readers struggle with Indian languages
- ❌ Manual translation is slow and expensive
- ❌ Existing tools don't support Indic scripts well

## 💡 The Solution

Project A.I.D. uses AI to:
1. 📸 Analyze any uploaded image
2. 🤖 Generate detailed English descriptions using Vision-Language Models
3. 🌐 Translate descriptions into Hindi and Bengali
4. 🔊 Provide text-to-speech in all three languages

**Built for real people. Built for India.**

## ✨ Features

- 🖼️ **Smart Image Analysis** - AI-powered image understanding
- 🌏 **Multilingual Support** - English, Hindi (हिंदी), and Bengali (বাংলা)
- 🔊 **Text-to-Speech** - Listen to descriptions in your language
- 📱 **Simple Interface** - Clean, accessible design
- 🚀 **Fast Processing** - Get results in seconds
- 🔒 **Privacy First** - Images processed securely, not stored

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **AI/ML**: Hugging Face Transformers (BLIP model)
- **Translation**: Google Translate API (googletrans)
- **Frontend**: HTML, CSS, JavaScript
- **Text-to-Speech**: Web Speech API

## 📦 Installation

### Prerequisites
- Python 3.8+
- pip

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/project-aid.git
cd project-aid
```

2. **Create a virtual environment** (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables** (optional)
```bash
cp .env.example .env
# Edit .env if you want to use custom API keys
```

5. **Run the application**
```bash
python app.py
```

6. **Open in browser**
