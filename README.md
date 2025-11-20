# 📬 MailMate – Think Less, Send Smart

**MailMate** is an AI-powered automatic email response generator built using Streamlit. It analyzes received emails, applies your chosen tone, and crafts a smart, human-like reply — then the user can preview the generated email and edit if needed and can send it directly via email. 💼🤖

---

## 🚀 Features

* ✨ **AI-Powered Replies** (via OpenRouter's models)
* 🎯 Tone Customization: Professional, Friendly, Apologetic, Persuasive
* 📤 Sends Emails Automatically (via Gmail SMTP)
* 🧠 Lightweight UI with [Streamlit](https://streamlit.io/)
* 🔐 Secret management using `.env`

---

## Live 🌐

* You can check the app [here](https://mailmate-1.streamlit.app/)

---

## 📦 Folder Structure

```
MailMate/
│
├── agents/
│   └── email_agent.py       # Generates AI-based email responses
├── utils/
│   └── email_sender.py      # Handles email sending via SMTP
├── .env                     # Local environment variables (not committed)
├── app.py                   # Main Streamlit app
├── requirements.txt
└── README.md
```

---

## 🛠️ Setup & Installation

### 1. Clone the Repo

```bash
git clone https://github.com/shivakumarsouta/mailmate.git
cd mailmate
```

### 2. Create Virtual Environment

```bash
python -m venv mailmate
source mailmate/bin/activate     # On Windows: mailmate\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file:

```ini
OPENROUTER_API_KEY=your_openrouter_api_key
SENDER_EMAIL=your_gmail@gmail.com
EMAIL_PASSWORD=your_gmail_app_password
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
```

> **⚠️ Use an [App Password](https://support.google.com/accounts/answer/185833) if you have 2FA enabled on your Gmail account.**

---

## 💻 Run the App

```bash
streamlit run app.py
```

Then open in your browser at [http://localhost:8501](http://localhost:8501)

---

## 🔑 Streamlit Secrets (Optional for Deployment)

Create `.streamlit/secrets.toml` for production:

```toml
OPENROUTER_API_KEY = "your_openrouter_api_key"
SENDER_EMAIL = "your_gmail@gmail.com"
EMAIL_PASSWORD = "your_app_password"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
```

---

## 📬 Example Usage

1. Paste an email someone sent you
2. Choose a tone (e.g., Professional)
3. Enter their email address
4. Click **"Generate & Send Email"**

Done. You’ll see the AI-generated reply, and the email will be sent automatically. ⚡

---

### ⚠️NOTE

As the replies are AI generated & may not be 100% correct, Please recheck before sending the replies.

---

## 🧾 License

MIT License. Free to use and modify.

---

## 🤝 Contributions Welcome

* Found a bug? Open an issue.
* Want to add more tones or language support? PRs are welcome!
* Want to switch models? Support for Claude, Mistral, or Llama can be added easily via OpenRouter.

---

## ✨ Credits

Built with:

* [Streamlit](https://streamlit.io/)
* [OpenRouter.ai](https://openrouter.ai/)
* [SMTP via Gmail](https://support.google.com/mail/answer/7126229)

---

## 📫 Connect

* [Email](shivakumarsouta18@gmail.com)
* [LinkedIn](https://www.linkedin.com/in/shivakumarsouta/)

---