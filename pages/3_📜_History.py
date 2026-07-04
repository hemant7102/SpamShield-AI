import streamlit as st
import pandas as pd
import os

# =====================================================
# Page Configuration
# =====================================================

st.set_page_config(
    page_title="Prediction History | SpamShield AI",
    page_icon="📜",
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

    st.title("📜 Prediction History")

    st.markdown("---")

    st.success("View all previous predictions")

    st.markdown("### Features")

    st.write("""
• Search Messages

• Filter Results

• Download History

• Clear History
""")

# =====================================================
# Header
# =====================================================

st.markdown("""
<div class='hero-card'>

<h1 class='main-title'>
📜 Prediction History
</h1>

<p class='sub-title'>
View, search and manage all previous spam predictions.
</p>

</div>
""",
unsafe_allow_html=True)

# =====================================================
# Session State
# =====================================================

if "history" not in st.session_state:
    st.session_state.history = []

# =====================================================
# Empty History
# =====================================================

if len(st.session_state.history) == 0:

    st.info("No prediction history available.")

    st.stop()

# =====================================================
# History DataFrame
# =====================================================

history_df = pd.DataFrame(st.session_state.history)

# =====================================================
# Summary Cards
# =====================================================

spam_count = (
    history_df["Prediction"] == "Spam"
).sum()

safe_count = (
    history_df["Prediction"] == "Safe"
).sum()

total = len(history_df)

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Total Predictions",
        total
    )

with col2:

    st.metric(
        "Spam",
        spam_count
    )

with col3:

    st.metric(
        "Safe",
        safe_count
    )

st.markdown("---")

# =====================================================
# Search
# =====================================================

search = st.text_input(
    "🔍 Search Messages"
)

filtered_df = history_df.copy()

if search:

    filtered_df = filtered_df[
        filtered_df["Message"]
        .str.contains(
            search,
            case=False,
            na=False
        )
    ]

# =====================================================
# Filter
# =====================================================

option = st.selectbox(
    "Filter by Prediction",
    [
        "All",
        "Spam",
        "Safe"
    ]
)

if option != "All":

    filtered_df = filtered_df[
        filtered_df["Prediction"] == option
    ]

st.markdown("---")

# =====================================================
# History Table
# =====================================================

st.subheader("Prediction Records")

st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)

st.markdown("---")

# =====================================================
# Analytics
# =====================================================

import plotly.express as px

st.subheader("📊 Prediction Analytics")

chart_df = pd.DataFrame({
    "Category": ["Spam", "Safe"],
    "Count": [spam_count, safe_count]
})

col1, col2 = st.columns(2)

with col1:

    fig = px.pie(
        chart_df,
        names="Category",
        values="Count",
        hole=0.45,
        title="Prediction Distribution"
    )

    fig.update_layout(height=420)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with col2:

    fig = px.bar(
        chart_df,
        x="Category",
        y="Count",
        color="Category",
        text="Count",
        title="History Summary"
    )

    fig.update_layout(
        showlegend=False,
        height=420
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.markdown("---")

# =====================================================
# Confidence Analysis
# =====================================================

st.subheader("🎯 Confidence Analysis")

if "Confidence" in history_df.columns:

    conf_df = history_df.copy()

    conf_df["Confidence"] = (
        conf_df["Confidence"]
        .astype(str)
        .str.replace("%", "", regex=False)
    )

    conf_df["Confidence"] = pd.to_numeric(
        conf_df["Confidence"],
        errors="coerce"
    )

    avg_conf = conf_df["Confidence"].mean()

    st.metric(
        "Average Confidence",
        f"{avg_conf:.2f}%"
    )

    fig = px.histogram(
        conf_df,
        x="Confidence",
        nbins=10,
        title="Confidence Distribution"
    )

    fig.update_layout(height=400)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

st.markdown("---")

# =====================================================
# Download History
# =====================================================

csv = filtered_df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    "📥 Download Prediction History",
    csv,
    "prediction_history.csv",
    "text/csv",
    use_container_width=True
)

# =====================================================
# Clear History
# =====================================================

if st.button(
    "🗑 Clear History",
    use_container_width=True
):

    st.session_state.history = []

    st.success(
        "Prediction history cleared successfully."
    )

    st.rerun()

st.markdown("---")

# =====================================================
# Insights
# =====================================================

st.subheader("💡 History Insights")

left, right = st.columns(2)

with left:

    st.success(f"""
### Safe Messages

Total : **{safe_count}**

Percentage : **{(safe_count/total)*100:.2f}%**
""")

with right:

    st.error(f"""
### Spam Messages

Total : **{spam_count}**

Percentage : **{(spam_count/total)*100:.2f}%**
""")

st.markdown("---")

# =====================================================
# Project Information
# =====================================================

with st.expander("📖 About Prediction History"):

    st.markdown("""
### Prediction History

This page stores predictions made during the current
Streamlit session.

### Features

- Search messages
- Filter Spam/Safe
- Analytics
- Confidence tracking
- Download history
- Clear history

> Note: History is stored in `st.session_state`.
Closing or restarting the application clears the history.
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

Prediction History Module

<br><br>

Built with Python • Streamlit • Pandas • Plotly

<br><br>

© 2026 Hemant Narute

</div>
""",
unsafe_allow_html=True
)
