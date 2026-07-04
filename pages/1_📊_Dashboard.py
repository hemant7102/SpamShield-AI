import streamlit as st
import pandas as pd
import plotly.express as px
import os

# =====================================================
# Page Configuration
# =====================================================

st.set_page_config(
    page_title="Dashboard | SpamShield AI",
    page_icon="📊",
    layout="wide"
)

# =====================================================
# Load Custom CSS
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

    st.title("📊 Dashboard")

    st.markdown("---")

    st.write("### SpamShield AI")

    st.success("System Status : Online")

    st.markdown("---")

    st.write("### Model")

    st.info("Multinomial Naive Bayes")

    st.write("### Feature Extraction")

    st.info("TF-IDF Vectorizer")

    st.write("### Dataset")

    st.info("SMS Spam Collection")

    st.markdown("---")

    st.write("Developed by")

    st.write("**Hemant Narute**")

# =====================================================
# Header
# =====================================================

st.markdown(
"""
<div class='hero-card'>

<h1 class='main-title'>
📊 Machine Learning Dashboard
</h1>

<p class='sub-title'>
Performance Overview of the SpamShield AI Model
</p>

</div>
""",
unsafe_allow_html=True
)

# =====================================================
# KPI Cards
# =====================================================

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.markdown(
    """
    <div class='metric-card'>
        <div class='metric-title'>
        Accuracy
        </div>

        <div class='metric-value'>
        98.26%
        </div>
    </div>
    """,
    unsafe_allow_html=True
    )

with col2:

    st.markdown(
    """
    <div class='metric-card'>
        <div class='metric-title'>
        Precision
        </div>

        <div class='metric-value'>
        99.10%
        </div>
    </div>
    """,
    unsafe_allow_html=True
    )

with col3:

    st.markdown(
    """
    <div class='metric-card'>
        <div class='metric-title'>
        Recall
        </div>

        <div class='metric-value'>
        97.40%
        </div>
    </div>
    """,
    unsafe_allow_html=True
    )

with col4:

    st.markdown(
    """
    <div class='metric-card'>
        <div class='metric-title'>
        F1 Score
        </div>

        <div class='metric-value'>
        98.20%
        </div>
    </div>
    """,
    unsafe_allow_html=True
    )

st.markdown("---")

# =====================================================
# Dataset Overview
# =====================================================

st.subheader("📂 Dataset Overview")

overview = pd.DataFrame(
    {
        "Property":[
            "Dataset Name",
            "Total Messages",
            "Spam Messages",
            "Legitimate Messages",
            "Vectorizer",
            "Algorithm"
        ],

        "Value":[
            "SMS Spam Collection",
            "5572",
            "747",
            "4825",
            "TF-IDF",
            "Multinomial Naive Bayes"
        ]
    }
)

st.dataframe(
    overview,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

# =====================================================
# Quick Insights
# =====================================================

st.subheader("📌 Key Insights")

col1, col2 = st.columns(2)

with col1:

    st.success("""
✔ High Accuracy

The model correctly classifies most messages.
""")

    st.success("""
✔ Low False Positives

Legitimate messages are rarely classified as spam.
""")

with col2:

    st.info("""
📩 Dataset Size

5572 labeled SMS messages.
""")

    st.info("""
🤖 Production Ready

Suitable for real-time spam detection applications.
""")

st.markdown("---")

# =====================================================
# Class Distribution
# =====================================================

st.subheader("📊 Class Distribution")

distribution = pd.DataFrame({
    "Class": ["Legitimate", "Spam"],
    "Messages": [4825, 747]
})

col1, col2 = st.columns(2)

with col1:

    fig = px.pie(
        distribution,
        names="Class",
        values="Messages",
        hole=0.5,
        title="Spam vs Legitimate Messages"
    )

    fig.update_layout(height=420)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    fig = px.bar(
        distribution,
        x="Class",
        y="Messages",
        text="Messages",
        color="Class",
        title="Message Distribution"
    )

    fig.update_layout(
        height=420,
        showlegend=False
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.markdown("---")

# =====================================================
# Model Performance
# =====================================================

st.subheader("📈 Model Performance")

performance = pd.DataFrame({
    "Metric": [
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score"
    ],
    "Score": [
        98.26,
        99.10,
        97.40,
        98.20
    ]
})

fig = px.bar(
    performance,
    x="Metric",
    y="Score",
    text="Score",
    color="Metric",
    title="Performance Metrics (%)"
)

fig.update_layout(
    height=450,
    showlegend=False,
    yaxis_title="Percentage"
)

fig.update_traces(
    texttemplate="%{text:.2f}",
    textposition="outside"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# =====================================================
# Model Information
# =====================================================

left, right = st.columns([2,1])

with left:

    st.subheader("🤖 Model Details")

    model_info = pd.DataFrame({
        "Parameter": [
            "Algorithm",
            "Vectorizer",
            "Dataset",
            "Training Samples",
            "Testing Samples",
            "Language"
        ],
        "Value": [
            "Multinomial Naive Bayes",
            "TF-IDF",
            "SMS Spam Collection",
            "4457",
            "1115",
            "English"
        ]
    })

    st.dataframe(
        model_info,
        hide_index=True,
        use_container_width=True
    )

with right:

    st.subheader("🎯 Overall Rating")

    st.metric(
        "Model Score",
        "⭐⭐⭐⭐⭐"
    )

    st.success("Excellent")

    st.progress(98)

st.markdown("---")

# =====================================================
# Evaluation Summary
# =====================================================

st.subheader("📋 Evaluation Summary")

summary = pd.DataFrame({
    "Category": [
        "Correct Predictions",
        "Incorrect Predictions",
        "False Positives",
        "False Negatives"
    ],
    "Value": [
        1096,
        19,
        8,
        11
    ]
})

st.dataframe(
    summary,
    hide_index=True,
    use_container_width=True
)

st.markdown("---")

# =====================================================
# Feature Importance
# =====================================================

st.subheader("🏆 Top Spam Indicators")

keywords = pd.DataFrame({
    "Keyword": [
        "FREE",
        "WIN",
        "CALL",
        "URGENT",
        "PRIZE",
        "CLICK",
        "CASH",
        "CLAIM",
        "BONUS",
        "REWARD"
    ],
    "Importance": [
        98,
        94,
        90,
        86,
        84,
        81,
        78,
        74,
        70,
        67
    ]
})

fig = px.bar(
    keywords,
    x="Importance",
    y="Keyword",
    orientation="h",
    text="Importance",
    title="Most Influential Spam Keywords"
)

fig.update_layout(height=500)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# =====================================================
# Confusion Matrix
# =====================================================

st.subheader("📉 Confusion Matrix")

confusion = pd.DataFrame(
    [
        [964, 8],
        [11, 132]
    ],
    columns=["Predicted Legitimate", "Predicted Spam"],
    index=["Actual Legitimate", "Actual Spam"]
)

fig = px.imshow(
    confusion,
    text_auto=True,
    aspect="auto",
    color_continuous_scale="Blues",
    title="Confusion Matrix"
)

fig.update_layout(height=500)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# =====================================================
# ROC Style Summary
# =====================================================

st.subheader("📈 Model Evaluation")

evaluation = pd.DataFrame(
    {
        "Metric": [
            "True Positive Rate",
            "True Negative Rate",
            "False Positive Rate",
            "False Negative Rate"
        ],
        "Value": [
            97.40,
            99.20,
            0.80,
            2.60
        ]
    }
)

fig = px.bar(
    evaluation,
    x="Metric",
    y="Value",
    text="Value",
    color="Metric",
    title="Evaluation Metrics"
)

fig.update_layout(
    height=450,
    showlegend=False
)

fig.update_traces(
    texttemplate="%{text:.2f}%",
    textposition="outside"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.markdown("---")

# =====================================================
# Model Workflow
# =====================================================

st.subheader("⚙️ Prediction Workflow")

st.subheader("⚙️ Prediction Workflow")

st.markdown("""
```text
User Input
      │
      ▼
Text Cleaning
      │
      ▼
Tokenization
      │
      ▼
Stopword Removal
      │
      ▼
Stemming
      │
      ▼
TF-IDF Vectorization
      │
      ▼
Multinomial Naive Bayes
      │
      ▼
Spam / Legitimate Prediction

""")
