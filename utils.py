import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Download required NLTK resources if missing
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")

ps = PorterStemmer()

# Common spam keywords
SPAM_KEYWORDS = {
    "free", "win", "winner", "won", "cash", "claim", "click", "offer",
    "urgent", "limited", "prize", "reward", "gift", "bonus", "money",
    "credit", "loan", "guarantee", "congratulations", "selected",
    "call", "subscribe", "exclusive", "discount"
}


def transform_text(text):
    """
    Preprocess text exactly like the training notebook.
    """
    text = text.lower()

    tokens = nltk.word_tokenize(text)

    filtered = []

    for word in tokens:
        if word.isalnum():
            filtered.append(word)

    tokens = []

    stop_words = set(stopwords.words("english"))

    for word in filtered:
        if word not in stop_words and word not in string.punctuation:
            tokens.append(ps.stem(word))

    return " ".join(tokens)


def get_statistics(text):
    """
    Return message statistics.
    """

    words = text.split()

    sentences = re.split(r"[.!?]+", text)

    sentences = [s for s in sentences if s.strip()]

    special = len(re.findall(r"[^A-Za-z0-9\s]", text))

    return {
        "Characters": len(text),
        "Words": len(words),
        "Sentences": len(sentences),
        "Special Characters": special
    }


def detect_spam_keywords(text):
    """
    Detect suspicious words inside the message.
    """

    found = []

    for word in text.lower().split():
        word = re.sub(r"[^a-zA-Z]", "", word)

        if word in SPAM_KEYWORDS and word not in found:
            found.append(word)

    return found


from sklearn.exceptions import NotFittedError

def get_confidence(model, vector):
    """
    Returns:
        prediction
        confidence
        probabilities
    """

    try:
        probs = model.predict_proba(vector)[0]

        prediction = probs.argmax()

        confidence = round(max(probs) * 100, 2)

        return prediction, confidence, probs

    except NotFittedError:

        return None, None, None