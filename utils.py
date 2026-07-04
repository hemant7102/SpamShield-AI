import re
import string
import ssl
import nltk

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.exceptions import NotFittedError

# ---------------------------------------------------
# SSL Fix (for Streamlit Cloud)
# ---------------------------------------------------

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

# ---------------------------------------------------
# Download required NLTK resources
# ---------------------------------------------------

RESOURCES = {
    "tokenizers/punkt": "punkt",
    "tokenizers/punkt_tab": "punkt_tab",
    "corpora/stopwords": "stopwords",
}

for resource_path, resource_name in RESOURCES.items():
    try:
        nltk.data.find(resource_path)
    except LookupError:
        nltk.download(resource_name, quiet=True)

# ---------------------------------------------------
# Stemmer
# ---------------------------------------------------

ps = PorterStemmer()

# ---------------------------------------------------
# Common Spam Keywords
# ---------------------------------------------------

SPAM_KEYWORDS = {
    "free",
    "win",
    "winner",
    "won",
    "cash",
    "claim",
    "click",
    "offer",
    "urgent",
    "limited",
    "prize",
    "reward",
    "gift",
    "bonus",
    "money",
    "credit",
    "loan",
    "guarantee",
    "congratulations",
    "selected",
    "call",
    "subscribe",
    "exclusive",
    "discount",
}

# ---------------------------------------------------
# Text Preprocessing
# ---------------------------------------------------

def transform_text(text):
    """
    Preprocess text exactly like the training notebook.
    """

    text = text.lower()

    words = nltk.word_tokenize(text)

    filtered = []

    for word in words:
        if word.isalnum():
            filtered.append(word)

    stop_words = set(stopwords.words("english"))

    final_words = []

    for word in filtered:
        if word not in stop_words:
            final_words.append(ps.stem(word))

    return " ".join(final_words)

# ---------------------------------------------------
# Message Statistics
# ---------------------------------------------------

def get_statistics(text):

    words = text.split()

    sentences = re.split(r"[.!?]+", text)

    sentences = [s for s in sentences if s.strip()]

    special = len(re.findall(r"[^A-Za-z0-9\s]", text))

    return {
        "Characters": len(text),
        "Words": len(words),
        "Sentences": len(sentences),
        "Special Characters": special,
    }

# ---------------------------------------------------
# Spam Keywords
# ---------------------------------------------------

def detect_spam_keywords(text):

    found = []

    for word in text.lower().split():

        word = re.sub(r"[^a-zA-Z]", "", word)

        if word in SPAM_KEYWORDS and word not in found:
            found.append(word)

    return found

# ---------------------------------------------------
# Confidence
# ---------------------------------------------------

def get_confidence(model, vector):

    try:

        probabilities = model.predict_proba(vector)[0]

        prediction = probabilities.argmax()

        confidence = round(max(probabilities) * 100, 2)

        return prediction, confidence, probabilities

    except NotFittedError:

        return None, None, None