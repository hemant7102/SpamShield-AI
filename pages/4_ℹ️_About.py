import streamlit as st
import pandas as pd
import os

# =====================================================
# Page Configuration
# =====================================================

st.set_page_config(
    page_title="About | SpamShield AI",
    page_icon="ℹ️",
    layout="wide"
)

# =====================================================
# Load CSS
# =====================================================

css_path = os.path.join("assets", "styles.css")

if os.path.exists(css_path):
    with open(css_path) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

# =====================================================
# Sidebar
# =====================================================

with st.sidebar:

    st.title("ℹ️ About")

    st.markdown("---")

    st.success("SpamShield AI")

    st.markdown("""
### Sections

• Project Overview

• Workflow

• Technology Stack

• Dataset

• Model Performance

• Future Scope

• Developer
""")

# =====================================================
# Hero Section
# =====================================================

st.markdown("""
<div class='hero-card'>

<h1 class='main-title'>
🛡️ SpamShield AI
</h1>

<p class='sub-title'>
AI Powered Email & SMS Spam Detection System
</p>

</div>
""",
unsafe_allow_html=True)

# =====================================================
# Project Overview
# =====================================================

st.subheader("📌 Project Overview")

st.write("""
SpamShield AI is a Machine Learning based web application
that detects whether an Email or SMS is **Spam** or
**Legitimate**.

The application uses Natural Language Processing (NLP)
and a trained Multinomial Naive Bayes model to classify
messages with high accuracy.

The project demonstrates the complete Machine Learning
workflow from data preprocessing to deployment using
Streamlit.
""")

st.markdown("---")

# =====================================================
# Project Workflow
# =====================================================

st.subheader("⚙️ Workflow")

st.code("""
User Input

↓

Lowercase

↓

Tokenization

↓

Stopword Removal

↓

Stemming

↓

TF-IDF Vectorization

↓

Machine Learning Model

↓

Prediction
""")

st.markdown("---")

# =====================================================
# Technology Stack
# =====================================================

st.subheader("🛠 Technology Stack")

tech = pd.DataFrame({

    "Technology":[
        "Python",
        "Streamlit",
        "Scikit-Learn",
        "NLTK",
        "Pandas",
        "Plotly",
        "Pickle"
    ],

    "Purpose":[
        "Programming Language",
        "Web Application",
        "Machine Learning",
        "Text Processing",
        "Data Handling",
        "Interactive Charts",
        "Model Serialization"
    ]

})

st.dataframe(
    tech,
    hide_index=True,
    use_container_width=True
)

st.markdown("---")

# =====================================================
# Dataset
# =====================================================

st.subheader("📂 Dataset")

dataset = pd.DataFrame({

    "Property":[
        "Dataset",
        "Total Messages",
        "Spam",
        "Legitimate",
        "Language"
    ],

    "Value":[
        "SMS Spam Collection",
        "5572",
        "747",
        "4825",
        "English"
    ]

})

st.dataframe(
    dataset,
    hide_index=True,
    use_container_width=True
)

st.markdown("---")

# =====================================================
# Model Information
# =====================================================

st.subheader("🤖 Machine Learning Model")

left, right = st.columns(2)

with left:

    st.info("""
Algorithm

Multinomial Naive Bayes
""")

    st.info("""
Feature Extraction

TF-IDF Vectorizer
""")

with right:

    st.metric(
        "Accuracy",
        "98.26%"
    )

    st.metric(
        "F1 Score",
        "98.20%"
    )

st.markdown("---")

# =====================================================
# Application Features
# =====================================================

st.subheader("✨ Key Features")

feature1, feature2 = st.columns(2)

with feature1:

    st.success("""
### Prediction

✔ Real-time Email Prediction

✔ SMS Prediction

✔ Confidence Score

✔ Spam Keyword Detection
""")

    st.success("""
### Dashboard

✔ Model Metrics

✔ Interactive Charts

✔ Dataset Overview

✔ Confusion Matrix
""")

with feature2:

    st.info("""
### Batch Prediction

✔ CSV Upload

✔ Bulk Prediction

✔ Download Results

✔ Analytics
""")

    st.info("""
### History

✔ Search Predictions

✔ Filter Results

✔ Download History

✔ Session Tracking
""")

st.markdown("---")

# =====================================================
# Future Enhancements
# =====================================================

st.subheader("🚀 Future Enhancements")

future = pd.DataFrame({

    "Upcoming Features":[

        "Deep Learning (LSTM)",

        "BERT Transformer",

        "Explainable AI (SHAP)",

        "REST API",

        "Multi-language Support",

        "Email Attachment Scanner",

        "Voice Message Detection",

        "Cloud Deployment"

    ]

})

st.dataframe(
    future,
    hide_index=True,
    use_container_width=True
)

st.markdown("---")

# =====================================================
# Developer
# =====================================================

st.subheader("👨‍💻 Developer")

left, right = st.columns([1,2])

with left:

    st.markdown("""
## 👨‍💻

Data Science

Machine Learning

Python Developer
""")

with right:

    st.write("""
### Hemant Narute

Passionate Data Science and Machine Learning enthusiast
focused on building practical AI applications using
Python, Scikit-Learn, NLP, SQL and Streamlit.

This project demonstrates the end-to-end Machine Learning
lifecycle including preprocessing, feature engineering,
model building and deployment.
""")

st.markdown("---")

# =====================================================
# Skills
# =====================================================

st.subheader("🛠 Skills Used")

skills = [
    "Python",
    "Machine Learning",
    "Natural Language Processing",
    "Scikit-Learn",
    "NLTK",
    "Pandas",
    "Plotly",
    "Streamlit",
    "Git",
    "GitHub"
]

cols = st.columns(5)

for i, skill in enumerate(skills):

    cols[i % 5].markdown(
        f"""
<div class='keyword'>
{skill}
</div>
""",
        unsafe_allow_html=True
    )

st.markdown("---")

# =====================================================
# Project Statistics
# =====================================================

st.subheader("📊 Project Statistics")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Pages", "5")
c2.metric("Language", "Python")
c3.metric("Framework", "Streamlit")
c4.metric("ML Model", "MNB")

st.markdown("---")

# =====================================================
# Acknowledgements
# =====================================================

with st.expander("🙏 Acknowledgements"):

    st.markdown("""
This project was developed for learning and portfolio
purposes.

Dataset

• SMS Spam Collection Dataset

Libraries

• Streamlit

• Scikit-Learn

• Pandas

• Plotly

• NLTK
""")

st.markdown("---")

# =====================================================
# Contact
# =====================================================

st.subheader("📬 Connect")

st.info("""
Update these with your own links before publishing.

🔗 GitHub :
https://github.com/hemant7102

💼 LinkedIn :
 https://www.linkedin.com/in/hemant-narute-282265355

📧 Email :
hemantnarute28@gmail.com
""")

st.markdown("---")

# =====================================================
# Footer
# =====================================================

st.markdown(
"""
<div class="footer">

<h3>🛡️ SpamShield AI</h3>

Machine Learning Powered Email & SMS Spam Detection

<br><br>

Developed by <b>Hemant Narute</b>

<br><br>

Python • Streamlit • Scikit-Learn • NLTK • Plotly

<br><br>

© 2026 All Rights Reserved

</div>
""",
unsafe_allow_html=True
)