import streamlit as st
import sqlite3
import pandas as pd
from datetime import datetime
from textblob import TextBlob

st.set_page_config(
    page_title="The Coding Companion",
    page_icon="🌸",
    layout="centered"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Cormorant+Garamond:wght@300;400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'EB Garamond', Georgia, serif;
}

.stApp {
    background: #fdf6f0;
    color: #3a2a1a;
}

#MainMenu, footer, header { visibility: hidden; }

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 680px !important;
    margin: 0 auto !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
}

/* ── Hero ── */
.hero {
    text-align: center;
    padding: 2.5rem 1rem 1.5rem;
}
.hero-eyebrow {
    font-family: 'EB Garamond', Georgia, serif;
    font-size: 0.75rem;
    font-weight: 500;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: #c9956a;
    margin-bottom: 1rem;
}
.hero-title {
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: clamp(2.8rem, 7vw, 4.2rem);
    font-weight: 300;
    line-height: 1.1;
    color: #2c1a0e;
    margin: 0 0 1.4rem;
    letter-spacing: 0.01em;
}
.hero-title em {
    font-style: italic;
    color: #c9956a;
}
.hero-sub {
    font-family: 'EB Garamond', Georgia, serif;
    font-size: 1.08rem;
    font-weight: 400;
    color: #6b4f3a;
    line-height: 1.85;
    max-width: 560px;
    margin: 0 auto 1rem;
    font-style: italic;
}
.hero-divider {
    width: 60px;
    height: 1px;
    background: linear-gradient(90deg, #f2c4a0, #d4a855, #f2c4a0);
    margin: 1.6rem auto 0;
}

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
    gap: 0;
    background: #faeee4;
    border-radius: 8px;
    padding: 4px;
    border: 1px solid #e8cdb5;
}
.stTabs [data-baseweb="tab"] {
    font-family: 'EB Garamond', Georgia, serif;
    font-size: 0.92rem;
    font-weight: 500;
    color: #9e7a5a;
    border-radius: 6px;
    padding: 0.5rem 1.1rem;
    border: none;
    background: transparent;
    transition: all 0.2s;
    letter-spacing: 0.02em;
}
.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #f2c4a0, #d4a855) !important;
    color: #2c1a0e !important;
    font-weight: 600;
}
.stTabs [data-baseweb="tab-highlight"],
.stTabs [data-baseweb="tab-border"] { display: none; }

/* ── Card ── */
.card {
    background: #faeee4;
    border: 1px solid #e8cdb5;
    border-radius: 12px;
    padding: 1.6rem 1.8rem;
    margin-bottom: 1.4rem;
}
.card-title {
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 1.3rem;
    font-weight: 500;
    color: #2c1a0e;
    margin-bottom: 0.25rem;
}
.card-sub {
    font-family: 'EB Garamond', Georgia, serif;
    font-size: 0.92rem;
    color: #9e7a5a;
    font-style: italic;
}

/* ── Inputs ── */
.stTextInput label, .stTextArea label {
    font-family: 'EB Garamond', Georgia, serif !important;
    font-size: 0.78rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.12em !important;
    text-transform: uppercase !important;
    color: #9e7a5a !important;
}
.stTextInput input, .stTextArea textarea {
    background: #fffaf6 !important;
    border: 1px solid #e8cdb5 !important;
    border-radius: 8px !important;
    color: #2c1a0e !important;
    font-family: 'EB Garamond', Georgia, serif !important;
    font-size: 1rem !important;
    transition: border-color 0.2s !important;
}
.stTextInput input:focus, .stTextArea textarea:focus {
    border-color: #d4a855 !important;
    box-shadow: 0 0 0 3px rgba(212, 168, 85, 0.15) !important;
}
.stTextInput input::placeholder, .stTextArea textarea::placeholder {
    color: #c8aa90 !important;
    font-style: italic !important;
}

/* ── Button ── */
.stFormSubmitButton button, .stButton button {
    background: linear-gradient(135deg, #f2c4a0, #d4a855) !important;
    color: #2c1a0e !important;
    font-family: 'EB Garamond', Georgia, serif !important;
    font-weight: 600 !important;
    font-size: 1rem !important;
    letter-spacing: 0.06em !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.65rem 2rem !important;
    transition: all 0.2s !important;
    width: 100% !important;
}
.stFormSubmitButton button:hover, .stButton button:hover {
    opacity: 0.88 !important;
    transform: translateY(-1px) !important;
    box-shadow: 0 6px 20px rgba(212, 168, 85, 0.3) !important;
}

/* ── Alerts ── */
.stSuccess > div {
    background: #fdf3e7 !important;
    border: 1px solid #d4a855 !important;
    border-radius: 8px !important;
    color: #7a5a1e !important;
    font-family: 'EB Garamond', Georgia, serif !important;
}
.stWarning > div {
    background: #fdf3e7 !important;
    border: 1px solid #e8cdb5 !important;
    border-radius: 8px !important;
    font-family: 'EB Garamond', Georgia, serif !important;
}
.stInfo > div {
    background: #fdf0ea !important;
    border: 1px solid #f2c4a0 !important;
    border-radius: 8px !important;
    font-family: 'EB Garamond', Georgia, serif !important;
}

/* ── Vibe badge ── */
.vibe-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.4rem 1.1rem;
    border-radius: 999px;
    font-family: 'EB Garamond', Georgia, serif;
    font-size: 0.88rem;
    font-weight: 500;
    letter-spacing: 0.06em;
    margin-top: 0.9rem;
    font-style: italic;
}
.vibe-good { background: #fdf0ea; color: #a0522d; border: 1px solid #d4a855; }
.vibe-meh  { background: #fdf3e7; color: #8b6914; border: 1px solid #c8a44a; }
.vibe-hard { background: #fdf0f3; color: #8b3a4a; border: 1px solid #e8a0b0; }

/* ── Metrics ── */
[data-testid="metric-container"] {
    background: #faeee4 !important;
    border: 1px solid #e8cdb5 !important;
    border-radius: 12px !important;
    padding: 1.2rem 1rem !important;
    text-align: center !important;
}
[data-testid="metric-container"] label {
    font-family: 'EB Garamond', Georgia, serif !important;
    font-size: 0.72rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.12em !important;
    color: #9e7a5a !important;
}
[data-testid="metric-container"] [data-testid="stMetricValue"] {
    font-family: 'Cormorant Garamond', Georgia, serif !important;
    font-size: 1.8rem !important;
    font-weight: 500 !important;
    color: #2c1a0e !important;
}
[data-testid="stMetricDelta"] {
    font-size: 0.8rem !important;
    font-family: 'EB Garamond', Georgia, serif !important;
    color: #c9956a !important;
}

/* ── Section label ── */
.section-label {
    font-family: 'EB Garamond', Georgia, serif;
    font-size: 0.72rem;
    font-weight: 500;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: #9e7a5a;
    margin: 1.8rem 0 0.7rem;
}

/* ── Dataframe ── */
[data-testid="stDataFrame"] {
    border-radius: 10px !important;
    overflow: hidden !important;
    border: 1px solid #e8cdb5 !important;
}

/* ── Empty state ── */
.empty-state {
    text-align: center;
    padding: 3rem 1rem;
}
.empty-state-icon { font-size: 2rem; margin-bottom: 0.7rem; }
.empty-state-text {
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 1.15rem;
    font-weight: 500;
    color: #9e7a5a;
}
.empty-state-sub {
    font-family: 'EB Garamond', Georgia, serif;
    font-size: 0.92rem;
    color: #c8aa90;
    font-style: italic;
    margin-top: 0.3rem;
}
</style>
""", unsafe_allow_html=True)

# ── Database ──
conn = sqlite3.connect("study_mindset_tracker.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS mindset_logs (
        date TEXT, topic TEXT, log_text TEXT, sentiment_score REAL, mindset_label TEXT
    )
""")
conn.commit()

# ── Hero ──
st.markdown("""
<div class="hero">
    <div class="hero-eyebrow">🌸 your personal space to grow</div>
    <h1 class="hero-title">The Coding<br><em>Companion</em></h1>
    <p class="hero-sub">
        Learning to code is kind of a wild roller coaster. One moment everything
        suddenly makes sense and you feel like you've cracked it, and the next
        you are stuck on something that feels way too small to be this confusing.
        <br><br>
        This space is here for all of it. The small wins, the frustrating bugs,
        the &ldquo;ohhh I get it now&rdquo; moments, and everything in between. A place to pause,
        look back, and actually see how much you are growing &mdash;
        one step at a time.
    </p>
    <div class="hero-divider"></div>
</div>
""", unsafe_allow_html=True)

# ── Tabs ──
tab1, tab2, tab3 = st.tabs(["📝 Today's Session", "📊 Vibe & Progress", "📚 Journal"])

with tab1:
    st.markdown("""
    <div class="card">
        <div class="card-title">How did your session go?</div>
        <div class="card-sub">Take 60 seconds to unpack before you close the laptop.</div>
    </div>
    """, unsafe_allow_html=True)

    with st.form("log_form", clear_on_submit=False):
        topic = st.text_input(
            "What were you working on?",
            placeholder="e.g. Python loops, SQL databases, Streamlit layouts..."
        )
        log_text = st.text_area(
            "Your honest reflection",
            placeholder="What clicked? What frustrated you? Any breakthrough moments? Vent freely.",
            height=160
        )
        submit_button = st.form_submit_button("Save Reflection 🌸", type="primary")

    if submit_button:
        if not topic or not log_text:
            st.warning("Please fill out both fields so your future self knows what happened today.")
        else:
            blob = TextBlob(log_text)
            score = round(blob.sentiment.polarity, 2)

            if score > 0.15:
                label = "Crushing It / Feeling Good"
                badge_class = "vibe-good"
                badge_icon = "✨"
            elif score < -0.15:
                label = "Struggling / High Friction"
                badge_class = "vibe-hard"
                badge_icon = "🌧"
            else:
                label = "Steady / Head Down Coding"
                badge_class = "vibe-meh"
                badge_icon = "🕯"

            timestamp = datetime.now().strftime("%Y-%m-%d")
            cursor.execute(
                "INSERT INTO mindset_logs VALUES (?, ?, ?, ?, ?)",
                (timestamp, topic, log_text, score, label)
            )
            conn.commit()

            st.balloons()
            st.success("Entry saved to your journal.")
            st.markdown(f'<div class="vibe-badge {badge_class}">{badge_icon} {label}</div>', unsafe_allow_html=True)

with tab2:
    df = pd.read_sql_query("SELECT * FROM mindset_logs", conn)

    if df.empty:
        st.markdown("""
        <div class="empty-state">
            <div class="empty-state-icon">📊</div>
            <div class="empty-state-text">Nothing to show yet</div>
            <div class="empty-state-sub">Log your first session to bring these charts to life.</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        total_entries = len(df)
        avg_sentiment = df["sentiment_score"].mean()
        blocked_days = len(df[df["mindset_label"] == "Struggling / High Friction"])

        col1, col2, col3 = st.columns(3)
        col1.metric("Sessions Logged", total_entries)

        if avg_sentiment > 0.15:
            col2.metric("Overall Vibe", "☀️ Positive", delta="You're on a roll!")
        elif avg_sentiment < -0.15:
            col2.metric("Overall Vibe", "🌧️ Frustrated", delta="Hang in there!", delta_color="inverse")
        else:
            col2.metric("Overall Vibe", "🕯 Focused", delta="Steady progress.")

        col3.metric("Tough Days", f"{blocked_days} / {total_entries}")

        st.markdown('<div class="section-label">Sentiment over time</div>', unsafe_allow_html=True)
        chart_data = df[["date", "sentiment_score"]].copy().set_index("date")
        st.line_chart(chart_data, y="sentiment_score", color="#d4a855")

        if total_entries >= 3:
            st.markdown('<div class="section-label">Entries by vibe</div>', unsafe_allow_html=True)
            vibe_counts = df["mindset_label"].value_counts().reset_index()
            vibe_counts.columns = ["Vibe", "Count"]
            st.bar_chart(vibe_counts.set_index("Vibe"), color="#f2c4a0")

with tab3:
    df_vault = pd.read_sql_query(
        """SELECT date as Date,
                  topic as 'What You Studied',
                  mindset_label as 'Vibe',
                  log_text as 'Your Notes'
           FROM mindset_logs ORDER BY date DESC""",
        conn
    )

    if df_vault.empty:
        st.markdown("""
        <div class="empty-state">
            <div class="empty-state-icon">📖</div>
            <div class="empty-state-text">Your journal is waiting</div>
            <div class="empty-state-sub">Every entry becomes part of your story.</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="section-label">{len(df_vault)} entries</div>', unsafe_allow_html=True)
        st.dataframe(df_vault, use_container_width=True, hide_index=True)