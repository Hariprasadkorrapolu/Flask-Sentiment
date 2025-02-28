from flask import Flask, render_template, request
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download VADER Lexicon
nltk.download('vader_lexicon')

# Initialize Flask app
app = Flask(__name__)

# Initialize VADER
sia = SentimentIntensityAnalyzer()

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Sentiment analysis route
@app.route('/analyze', methods=['POST'])
def analyze():
    review = request.form['review']
    sentiment_score = sia.polarity_scores(review)['compound']

    # Classify sentiment
    if sentiment_score >= 0.05:
        sentiment = "Positive"
    elif sentiment_score <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return render_template('index.html', review=review, sentiment=sentiment, score=sentiment_score)

if __name__ == '__main__':
    app.run(debug=True)
