# The Coding Companion ♡

A personal coding journal that tracks your daily sessions, moods, and progress as you learn to code — built with Streamlit, SQLite, and TextBlob sentiment analysis.

Learning to code is kind of a wild roller coaster. One moment everything suddenly makes sense and you feel like you've cracked it, and the next you are stuck on something that feels way too small to be this confusing. The Coding Companion is an intentionally designed personal journal space where developers can pause, look back, and actually see how much they are growing — one step at a time.

---

## Features ♡

- **Session Logging** — Document your daily study topics and honest reflections in a clean, minimal interface.
- **Vibe & Progress Tracking** — Sentiment is automatically analyzed using TextBlob and mapped over time via interactive line and bar charts so you can see your emotional trajectory as a developer.
- **Local SQLite Database** — All entries are stored locally in a `.db` file. No cloud, no accounts, no data leaving your machine.
- **Custom UI** — Styled with EB Garamond and Cormorant Garamond, a pastel pink and gold palette, and fully light-mode-locked so it looks consistent across all devices.

---

## Built With ♡

- [Streamlit](https://streamlit.io) — Web interface and layout
- [SQLite3](https://docs.python.org/3/library/sqlite3.html) — Local relational database
- [TextBlob](https://textblob.readthedocs.io) — NLP sentiment scoring
- [Pandas](https://pandas.pydata.org) — Data parsing and analysis

---

## Running Locally ♡

1. Clone this repository
2. Install dependencies:

```bash
pip install streamlit pandas textblob
```

3. Run the app:

```bash
streamlit run app2.py
```

---

## Project Structure ♡

```
my-coding-companion/
├── app2.py                    # Main application
├── study_mindset_tracker.db   # Auto-generated local database
└── README.md
```

---

*Built for developers who are still figuring it out, which is all of us :)*
