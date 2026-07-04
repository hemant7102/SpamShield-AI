import streamlit as st
import pickle
import pandas as pd
import os
from datetime import datetime

from utils import (
    transform_text,
    get_statistics,
    detect_spam_keywords,
    get_confidence
)

# -------------------------------
# Page Config
# -------------------------------

st.set_page_config(
    page_title="SpamShield AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------
# Load CSS
# -------------------------------

css_path = os.path.join("assets", "styles.css")

if os.path.exists(css_path):
    with open(css_path) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# -------------------------------
# Load Model
# -------------------------------

@st.cache_resource
def load_model():

    with open("vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)

    with open("model.pkl", "rb") as f:
        model = pickle.load(f)

    return vectorizer, model


tfidf, model = load_model()

# -------------------------------
# Session State
# -------------------------------

if "history" not in st.session_state:
    st.session_state.history = []

# -------------------------------
# Sidebar
# -------------------------------

with st.sidebar:

    st.title("🛡️ SpamShield AI")

    st.markdown("---")

    st.subheader("Project")

    st.write("Machine Learning Powered")
    st.write("Email & SMS Spam Detection")

    st.markdown("---")

    st.subheader("Model Information")

    st.info("Model : Multinomial Naive Bayes")

    st.info("Vectorizer : TF-IDF")

    st.info("Language : English")

    st.markdown("---")

    st.subheader("Developer")

    st.write("Hemant Narute")

    st.caption("Data Science & Machine Learning")

# -------------------------------
# Hero Section
# -------------------------------

st.markdown(
    """
    <div class='hero-card'>

    <h1 class='main-title'>
    🛡️ SpamShield AI
    </h1>

    <p class='sub-title'>
    Intelligent Email & SMS Spam Detection using Machine Learning
    </p>

    </div>
    """,
    unsafe_allow_html=True
)

# -------------------------------
# Metrics
# -------------------------------

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown(
        """
        <div class='metric-card'>
        <div class='metric-title'>Accuracy</div>
        <div class='metric-value'>98.2%</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:

    st.markdown(
        """
        <div class='metric-card'>
        <div class='metric-title'>Model</div>
        <div class='metric-value'>MNB</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:

    st.markdown(
        """
        <div class='metric-card'>
        <div class='metric-title'>Vectorizer</div>
        <div class='metric-value'>TF-IDF</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# -------------------------------
# Input Section
# -------------------------------

st.subheader("📩 Enter your Email or SMS")

input_sms = st.text_area(
    "",
    height=220,
    placeholder="Paste your Email or SMS here..."
)

col1, col2 = st.columns([2,1])

with col1:

    predict = st.button(
        "🚀 Analyze Message",
        use_container_width=True
    )

with col2:

    clear = st.button(
        "🗑 Clear",
        use_container_width=True
    )

if clear:
    st.rerun()

st.markdown("---")

# ==========================================================
# PART 2 : Statistics + Prediction
# ==========================================================

if predict:

    if input_sms.strip() == "":
        st.warning("⚠️ Please enter an Email or SMS.")
        st.stop()

    # ----------------------------
    # Message Statistics
    # ----------------------------

    stats = get_statistics(input_sms)

    st.subheader("📊 Message Statistics")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Characters", stats["Characters"])
    c2.metric("Words", stats["Words"])
    c3.metric("Sentences", stats["Sentences"])
    c4.metric("Special Characters", stats["Special Characters"])

    st.markdown("---")

    # ----------------------------
    # Preprocessing
    # ----------------------------

    transformed_sms = transform_text(input_sms)

    with st.expander("🔍 View Text Preprocessing"):

        st.write("### Original Message")
        st.write(input_sms)

        st.write("### Processed Text")
        st.code(transformed_sms)



    # Vectorize the text
    # ----------------------------
    # Prediction
    # ----------------------------

    vector = tfidf.transform([transformed_sms])

    prediction, confidence, probabilities = get_confidence(model, vector)

    # Check if model is fitted
    if prediction is None:

        st.markdown(
        """
        <div class='error-card'>

        <div class='error-title'>
        ❌ MODEL NOT TRAINED
        </div>

        <div class='error-text'>
        The loaded <b>model.pkl</b> is not fitted.

        <br><br>

        Please train your model in the notebook and regenerate
        <b>model.pkl</b>.
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

        st.stop()

    st.markdown("---")

    # ----------------------------
    # Result Card
    # ----------------------------

    if prediction == 1:

     st.markdown(
        """
        <div class='error-card'>

        <div class='error-title'>
        🚨 SPAM DETECTED
        </div>

        <div class='error-text'>
        This message appears to be spam or promotional.
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    else:
     
     st.markdown(
        """
        <div class='success-card'>

        <div class='success-title'>
        ✅ SAFE MESSAGE
        </div>

        <div class='success-text'>
        This message appears legitimate.
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )



    # ----------------------------
    # Confidence Score
    # ----------------------------

    if confidence is not None:

        st.markdown("### 🎯 Prediction Confidence")

        st.progress(min(int(confidence), 100))

        st.metric(
            label="Confidence",
            value=f"{confidence:.2f}%"
        )

    # ----------------------------
    # Prediction Probabilities
    # ----------------------------

    if probabilities is not None:

        st.markdown("### 📈 Probability Distribution")

        safe_prob = probabilities[0] * 100
        spam_prob = probabilities[1] * 100

        p1, p2 = st.columns(2)

        p1.metric(
            "Safe",
            f"{safe_prob:.2f}%"
        )

        p2.metric(
            "Spam",
            f"{spam_prob:.2f}%"
        )

    st.markdown("---")

    # ----------------------------
    # Spam Keywords
    # ----------------------------

    keywords = detect_spam_keywords(input_sms)

    st.subheader("🚩 Suspicious Keywords")

    if len(keywords) == 0:

        st.success("No suspicious keywords detected.")

    else:

        cols = st.columns(min(4, len(keywords)))

        for i, word in enumerate(keywords):

            cols[i % len(cols)].markdown(
                f"""
                <div class='keyword'>
                {word.upper()}
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("---")

# ==========================================================
# PART 3 : History, Download & Footer
# ==========================================================

    # ----------------------------
    # Save Prediction History
    # ----------------------------

    history_item = {
        "Time": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
        "Message": input_sms,
        "Prediction": "Spam" if prediction == 1 else "Safe",
        "Confidence": (
            f"{confidence:.2f}%"
            if confidence is not None
            else "N/A"
        )
    }

    st.session_state.history.insert(0, history_item)

# ==========================================================
# Prediction History
# ==========================================================

if len(st.session_state.history) > 0:

    st.markdown("## 📜 Prediction History")

    history_df = pd.DataFrame(st.session_state.history)

    st.dataframe(
        history_df,
        use_container_width=True,
        hide_index=True
    )

    csv = history_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Prediction History",
        data=csv,
        file_name="prediction_history.csv",
        mime="text/csv",
        use_container_width=True
    )

    if st.button(
        "🗑 Clear Prediction History",
        use_container_width=True
    ):
        st.session_state.history = []
        st.rerun()

# ==========================================================
# Sample Messages
# ==========================================================

st.markdown("---")

st.subheader("💡 Try Sample Messages")

spam_example = """
Congratulations!

You have won ₹50,000 Cash Prize.

Click the link below immediately to claim your reward.

Limited Time Offer.
"""

safe_example = """
Hello Hemant,

The project meeting is scheduled tomorrow at 10:00 AM.

Please bring your laptop and project documents.

Thank you.
"""

col1, col2 = st.columns(2)

with col1:

    st.code(spam_example)

with col2:

    st.code(safe_example)

# ==========================================================
# About Model
# ==========================================================

st.markdown("---")

with st.expander("🤖 About this Model"):

    st.markdown("""
### SpamShield AI

This application uses a Machine Learning model trained on the
SMS Spam Collection Dataset.

### Workflow

Email/SMS

⬇

Text Cleaning

⬇

Tokenization

⬇

Stopword Removal

⬇

Stemming

⬇

TF-IDF Vectorization

⬇

Multinomial Naive Bayes

⬇

Prediction

---

### Technologies

- Python
- Streamlit
- Scikit-Learn
- NLTK
- Pandas

---

Developer

Hemant Narute
""")

# ==========================================================
# Footer
# ==========================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(
"""
<div class='footer'>

🛡️ <b>SpamShield AI</b><br>

Machine Learning Powered Email & SMS Spam Detection

<br><br>

Built with ❤️ using

Python • Streamlit • Scikit-Learn • NLTK

<br><br>

© 2026 Hemant Narute

</div>
""",
unsafe_allow_html=True
)