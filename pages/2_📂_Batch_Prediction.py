import streamlit as st
import pandas as pd
import pickle
import os

from utils import (
    transform_text,
    get_confidence
)

# =====================================================
# Page Config
# =====================================================

st.set_page_config(
    page_title="Batch Prediction | SpamShield AI",
    page_icon="📂",
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
# Load Model
# =====================================================

@st.cache_resource
def load_model():

    with open("vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)

    with open("model.pkl", "rb") as f:
        model = pickle.load(f)

    return vectorizer, model


tfidf, model = load_model()

# =====================================================
# Sidebar
# =====================================================

with st.sidebar:

    st.title("📂 Batch Prediction")

    st.markdown("---")

    st.success("Predict hundreds of messages at once")

    st.markdown("### Instructions")

    st.write("""
• Upload a CSV file

• CSV must contain a column named

`message`

• Click **Start Prediction**

• Download results
""")

# =====================================================
# Header
# =====================================================

st.markdown("""
<div class='hero-card'>

<h1 class='main-title'>
📂 Batch Spam Detection
</h1>

<p class='sub-title'>
Predict hundreds of Email or SMS messages in one click.
</p>

</div>
""",
unsafe_allow_html=True)

# =====================================================
# Upload CSV
# =====================================================

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.success("CSV uploaded successfully.")

    st.subheader("Preview")

    st.dataframe(
        df.head(),
        use_container_width=True
    )

    if "message" not in df.columns:

        st.error(
            "CSV must contain a column named 'message'"
        )

        st.stop()

    st.markdown("---")

    st.metric(
        "Total Messages",
        len(df)
    )

    predict = st.button(
        "🚀 Start Batch Prediction",
        use_container_width=True
    )

# =====================================================
# Batch Prediction
# =====================================================

if uploaded_file is not None and predict:

    results = []
    predictions = []
    confidence_scores = []

    progress_bar = st.progress(0)
    status = st.empty()

    total = len(df)

    for index, message in enumerate(df["message"]):

        message = str(message)

        transformed = transform_text(message)

        vector = tfidf.transform([transformed])

        prediction, confidence, probabilities = get_confidence(
            model,
            vector
        )

        label = "Spam" if prediction == 1 else "Legitimate"

        predictions.append(label)

        confidence_scores.append(
            round(confidence, 2)
            if confidence is not None
            else None
        )

        results.append({
            "Message": message,
            "Prediction": label,
            "Confidence (%)": confidence
            if confidence is not None
            else None
        })

        progress_bar.progress((index + 1) / total)

        status.text(
            f"Processing {index+1} of {total} messages..."
        )

    status.success("Prediction completed successfully!")

    result_df = pd.DataFrame(results)

    st.markdown("---")

# =====================================================
# Summary Cards
# =====================================================

    spam_count = (result_df["Prediction"] == "Spam").sum()
    safe_count = (result_df["Prediction"] == "Legitimate").sum()

    avg_conf = (
        result_df["Confidence (%)"].mean()
        if result_df["Confidence (%)"].notna().any()
        else 0
    )

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Spam Messages",
        spam_count
    )

    c2.metric(
        "Legitimate Messages",
        safe_count
    )

    c3.metric(
        "Average Confidence",
        f"{avg_conf:.2f}%"
    )

    st.markdown("---")

# =====================================================
# Results Table
# =====================================================

    st.subheader("Prediction Results")

    st.dataframe(
        result_df,
        use_container_width=True,
        hide_index=True
    )

    st.markdown("---")

# =====================================================
# Filter Results
# =====================================================

    st.subheader("Filter Results")

    option = st.selectbox(
        "Select Category",
        [
            "All",
            "Spam",
            "Legitimate"
        ]
    )

    if option == "Spam":

        st.dataframe(
            result_df[
                result_df["Prediction"] == "Spam"
            ],
            use_container_width=True,
            hide_index=True
        )

    elif option == "Legitimate":

        st.dataframe(
            result_df[
                result_df["Prediction"] == "Legitimate"
            ],
            use_container_width=True,
            hide_index=True
        )

    else:

        st.dataframe(
            result_df,
            use_container_width=True,
            hide_index=True
        )

    st.markdown("---")

# =====================================================
# Download Results
# =====================================================

    csv = result_df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        "📥 Download Prediction Results",
        csv,
        "batch_prediction_results.csv",
        "text/csv",
        use_container_width=True
    )

    st.markdown("---")

# =====================================================
# Visualization
# =====================================================

import plotly.express as px

st.subheader("📊 Prediction Analytics")

chart_df = pd.DataFrame({
    "Category": ["Spam", "Legitimate"],
    "Count": [spam_count, safe_count]
})

col1, col2 = st.columns(2)

with col1:

    pie = px.pie(
        chart_df,
        names="Category",
        values="Count",
        hole=0.45,
        title="Prediction Distribution"
    )

    pie.update_layout(height=420)

    st.plotly_chart(
        pie,
        use_container_width=True
    )

with col2:

    bar = px.bar(
        chart_df,
        x="Category",
        y="Count",
        color="Category",
        text="Count",
        title="Spam vs Legitimate"
    )

    bar.update_layout(
        showlegend=False,
        height=420
    )

    st.plotly_chart(
        bar,
        use_container_width=True
    )

st.markdown("---")

# =====================================================
# Batch Insights
# =====================================================

st.subheader("📈 Batch Prediction Insights")

spam_percentage = (spam_count / len(result_df)) * 100
safe_percentage = (safe_count / len(result_df)) * 100

left, right = st.columns(2)

with left:

    st.success(f"""
### Legitimate Messages

Total : **{safe_count}**

Percentage : **{safe_percentage:.2f}%**
""")

with right:

    st.error(f"""
### Spam Messages

Total : **{spam_count}**

Percentage : **{spam_percentage:.2f}%**
""")

st.markdown("---")

# =====================================================
# Sample CSV Format
# =====================================================

with st.expander("📄 Sample CSV Format"):

    sample = pd.DataFrame({
        "message":[
            "Congratulations! You won ₹5000.",
            "Meeting tomorrow at 10 AM.",
            "Claim your FREE reward now.",
            "Please review the project report."
        ]
    })

    st.dataframe(
        sample,
        hide_index=True,
        use_container_width=True
    )

    sample_csv = sample.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇ Download Sample CSV",
        sample_csv,
        "sample_messages.csv",
        "text/csv"
    )

st.markdown("---")

# =====================================================
# Tips
# =====================================================

st.subheader("💡 Tips")

col1, col2 = st.columns(2)

with col1:

    st.info("""
### Supported

✅ CSV files

✅ UTF-8 Encoding

✅ Column name : message
""")

with col2:

    st.warning("""
### Notes

• Remove empty rows

• One message per row

• Keep text in English for best accuracy
""")

st.markdown("---")

# =====================================================
# Footer
# =====================================================

st.markdown(
"""
<div class="footer">

<b>SpamShield AI</b>

<br>

Batch Prediction Module

<br><br>

Built with Python • Streamlit • Scikit-Learn • NLTK

<br><br>

© 2026 Hemant Narute

</div>
""",
unsafe_allow_html=True
)