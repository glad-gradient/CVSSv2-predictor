import re
import string
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))


def clean_text(text, remove_stopwords=True):
    def remove_URL(_text):
        url = re.compile(r'https?://\S+|www\.\S+')
        return url.sub(r'', _text)

    def remove_html(_text):
        html = re.compile(r'<.*?>')
        return html.sub(r'', _text)

    def remove_punct(_text):
        table = str.maketrans('', '', string.punctuation)
        return _text.translate(table)

    text = remove_URL(text)
    text = remove_html(text)
    text = remove_punct(text)
    text = text.lower()

    if remove_stopwords:
        text = text.split()
        text = [word for word in text if word not in stop_words]
        text = ' '.join(text)

    return text
