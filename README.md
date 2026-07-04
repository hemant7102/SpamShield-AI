
# 🛡️ SpamShield AI

> Intelligent Email & SMS Spam Detection using Machine Learning

SpamShield AI is a professional Machine Learning web application that detects whether an Email or SMS message is **Spam** or **Safe (Not Spam)**. The application is built using **Python**, **Streamlit**, **Scikit-Learn**, **NLTK**, and **TF-IDF Vectorization**, providing fast and accurate predictions with an interactive user interface.

---

# 🚀 Features

- 📩 Email & SMS Spam Detection
- 🤖 Machine Learning Powered Prediction
- 📊 Message Statistics
- 🎯 Confidence Score
- 📈 Prediction Probability Distribution
- 🚩 Suspicious Keyword Detection
- 📜 Prediction History
- 📥 Download Prediction History (CSV)
- 💡 Sample Spam & Safe Messages
- 📱 Professional Responsive UI
- ⚡ Fast Real-Time Prediction

---

# 📸 Application Preview

## Home Page

- Professional Dashboard
- Modern UI
- Interactive Metrics
- Spam Detection Panel

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Streamlit | Web Application |
| Scikit-Learn | Machine Learning |
| Pandas | Data Processing |
| NLTK | Text Preprocessing |
| Pickle | Model Serialization |
| TF-IDF | Text Vectorization |
| Multinomial Naive Bayes | Spam Classification |

---

# 📂 Project Structure

```
SpamShield-AI/
│
├── app.py
├── utils.py
├── requirements.txt
├── model.pkl
├── vectorizer.pkl
├── assets/
│   └── styles.css
├── images/
│   ├── home.png
│   ├── prediction.png
│   └── history.png
├── notebooks/
│   └── spam_model_training.ipynb
├── dataset/
│   └── spam.csv
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/hemant7102/SpamShield-AI.git
```

```bash
cd SpamShield-AI
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Application

```bash
streamlit run app.py
```

---

# 🧠 Machine Learning Workflow

```
Input Email / SMS
        │
        ▼
Text Cleaning
        │
        ▼
Lowercase Conversion
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
Prediction
        │
        ▼
Spam / Safe
```

---

# 📊 Model Information

| Property | Value |
|----------|-------|
| Algorithm | Multinomial Naive Bayes |
| Vectorizer | TF-IDF |
| Dataset | SMS Spam Collection |
| Language | English |
| Accuracy | 98.2% |

---

# 🎯 Prediction Output

The application provides:

- Spam or Safe Prediction
- Confidence Score
- Prediction Probability
- Spam Keywords Detection
- Message Statistics
- Prediction History

---

# 📈 Message Statistics

For every message the application displays:

- Number of Characters
- Number of Words
- Number of Sentences
- Number of Special Characters

---

# 🚩 Suspicious Keyword Detection

SpamShield AI detects suspicious words such as:

- Congratulations
- Winner
- Lottery
- Free
- Prize
- Urgent
- Cash
- Claim
- Offer
- Click
- Reward

---

# 📜 Prediction History

The application stores previous predictions including:

- Date & Time
- Original Message
- Prediction
- Confidence Score

Users can:

- View History
- Download CSV
- Clear History

---

# 📦 Dependencies

```
streamlit
pandas
numpy
scikit-learn
nltk
pickle
```

---

# 📚 Dataset

The model is trained using the **SMS Spam Collection Dataset**, containing labeled SMS messages categorized as:

- Spam
- Ham (Safe)

---

# 💻 Future Improvements

- Multi-language Spam Detection
- Email Attachment Analysis
- URL Safety Detection
- Phishing Detection
- Deep Learning Models
- Explainable AI
- Cloud Deployment
- REST API Integration
- User Authentication
- Dark Mode

---

# 👨‍💻 Developer

**Hemant Narute**

Data Science | Machine Learning | Artificial Intelligence

GitHub: https://github.com/hemant7102

LinkedIn: https://www.linkedin.com/in/hemant-narute-282265355

---

# ⭐ If you found this project useful

Please consider giving it a ⭐ on GitHub.

---

# 📄 License

This project is licensed under the MIT License.

---

## 🛡️ SpamShield AI

**Intelligent Email & SMS Spam Detection using Machine Learning**

Built with ❤️ using **Python • Streamlit • Scikit-Learn • NLTK**
