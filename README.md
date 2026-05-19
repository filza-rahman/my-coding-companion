# my-coding-companion
A beautiful, fully local Python web application built with Streamlit and SQLite to help developers track their daily learning sessions, visualize cognitive data, and get instant container syntax assistance.

Learning to code is a wild roller coaster of small wins, frustrating bugs, and sudden breakthroughs. **The Coding Companion** is an intentional, aesthetically designed personal journal space that allows developers to pause, look back, and actively measure their cognitive growth over time—completely offline and error-free.

## ✨ Features

- **📝 Real-Time Session Logging:** A beautiful, custom minimalist UI built with Streamlit to document daily study topics and unfiltered development reflections.
- **📊 Vibe Check & Trajectory Analytics:** Automatically processes journal sentiment using `TextBlob` and maps historical emotional trajectories using interactive data framing and line charts.
- **💾 Local Persistence SQL Database:** Securely commits logs, syntax labels, and sentiment tracking scores directly to a local `SQLite3` database.
- **🤖 Smart Local Mentorship:** Completely stripped of unstable external API configurations to guarantee 100% reliability, utilizing localized keyword analysis to serve instant, contextual cheat sheets for complex Python concepts (e.g., container mutability, bracket structures, and database pipelines).

## 🛠️ Built With

- **Streamlit** - For the high-fidelity web interface layout.
- **SQLite3** - For robust, relational local data logging.
- **TextBlob** - For local Natural Language Processing (NLP) sentiment scoring.
- **Pandas** - For dataset parsing and tracking analysis.

## 🚀 How to Run Locally

1. Clone this repository to your desktop.
2. Ensure you have the required dependencies installed:
   ```bash
   pip install streamlit pandas textblob
