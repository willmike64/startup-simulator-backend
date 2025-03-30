# 🚀 Startup Simulator (Alpha)

This is a modular, AI-enhanced business simulation game built with Streamlit.

## 🌐 Live Deployment
Once pushed to GitHub, you can deploy it via [Streamlit Cloud](https://share.streamlit.io)

## 📦 Features
- 🔐 User login + role selection
- 🧠 AI advisors (Banker, HR, Board, etc.)
- 📊 Decision logging (per user)
- ☁️ Cloud-ready structure

## 🛠 How to Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🌩 Deploy to Streamlit Cloud
1. Push to GitHub
2. Go to https://share.streamlit.io
3. Point to this repo and `app.py`
4. Add secrets (optional):
```toml
openai_key = "sk-..."
```