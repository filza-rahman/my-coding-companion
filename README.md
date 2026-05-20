# The Coding Companion ♡

A personal coding journal that tracks your daily sessions, moods, and progress as you learn to code — built with Streamlit, SQLite, TextBlob, and a Groq-powered AI companion.

Learning to code is kind of a wild roller coaster. One moment everything suddenly makes sense and you feel like you've cracked it, and the next you are stuck on something that feels way too small to be this confusing. The Coding Companion is an intentionally designed personal journal space where developers can pause, reflect, and actually see how much they are growing — one step at a time. And now, they don't have to do it alone.

🔗 **[Live Demo](https://supercool-coding-companion.streamlit.app/)**

---

## Features ♡

### ✦ AI Coding Companion (powered by Groq + LLaMA 3)
The centerpiece of the app!! Every time you log a session, the AI companion reads your reflection and responds — not generically, but specifically to what you studied and how you felt. Struggling with for loops? It gives you a concrete tip. Had a breakthrough? It celebrates with you and nudges you toward what's next. After enough sessions, you can also generate a full **AI pattern summary** that analyzes your emotional trajectory, identifies burnout risk or momentum, and suggests a focus for the week ahead. Built using the Groq inference API for fast, low-latency responses.

### ✦ Session Logging
Document your daily study topics and honest reflections in a clean, minimal interface designed to feel like a journal, not a form.

### ✦ Vibe & Progress Tracking
Sentiment is automatically analyzed using TextBlob NLP and mapped over time via interactive line and bar charts, so you can actually see your emotional trajectory as a developer — not just what you studied, but how it felt.

### ✦ Local SQLite Database
All entries are stored locally in a `.db` file. No cloud, no accounts, no data leaving your machine.

### ✦ Custom UI
Styled with EB Garamond and Cormorant Garamond, a pastel pink and gold palette, and fully light-mode-locked so it looks consistent across all devices.

---

## Built With ♡

- [Streamlit](https://streamlit.io) — Web interface and layout
- [Groq API](https://groq.com) — Fast LLaMA 3 inference for the AI companion
- [SQLite3](https://docs.python.org/3/library/sqlite3.html) — Local relational database
- [TextBlob](https://textblob.readthedocs.io) — NLP sentiment scoring
- [Pandas](https://pandas.pydata.org) — Data parsing and analysis

---

## Running Locally ♡

1. Clone this repository
2. Install dependencies:
```bash
pip install streamlit pandas textblob groq
```
3. Add your Groq API key — create a `.streamlit/secrets.toml` file:
```toml
GROQ_API_KEY = "your-key-here"
```
Get a free key at [console.groq.com](https://console.groq.com). Add `.streamlit/secrets.toml` to your `.gitignore` so it never gets pushed.

4. Run the app:
```bash
streamlit run app2.py
```

---

## Project Structure ♡

```
my-coding-companion/
├── app2.py                    # Main application
├── requirements.txt           # Dependencies
├── study_mindset_tracker.db   # Auto-generated local database
└── README.md
```

---

*Built for developers who are still figuring it out, which is all of us :)*
