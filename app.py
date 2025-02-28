from flask import Flask, render_template, request
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download VADER Lexicon
nltk.download('vader_lexicon')

app = Flask(__name__)

# Initialize VADER
sia = SentimentIntensityAnalyzer()

@app.route('/')
def home():
    return '''
    <form action="/analyze" method="post">
        <textarea name="review" placeholder="Enter your review..."></textarea><br>
        <button type="submit">Analyze</button>
    </form>
    '''

@app.route('/analyze', methods=['POST'])
def analyze():
    review = request.form['review']
    score = sia.polarity_scores(review)['compound']
    
    sentiment = "Neutral"
    if score > 0.05:
        sentiment = "Positive"
    elif score < -0.05:
        sentiment = "Negative"

    return f"Review Sentiment: {sentiment} (Score: {score})"

if __name__ == "__main__":
    app.run(debug=True)
