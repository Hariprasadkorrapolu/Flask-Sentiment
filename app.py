from flask import Flask, render_template_string, request
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

app = Flask(__name__)

html_template = """ <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Sentiment Analyzer</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
    <style>
        body { padding: 20px; background-color: #f8f9fa; }
        .container { max-width: 600px; margin: auto; background: white; padding: 20px; border-radius: 10px; 
                     box-shadow: 0 0 10px rgba(0,0,0,0.1); }
        .result { margin-top: 20px; font-size: 18px; font-weight: bold; }
        .positive { color: green; }
        .negative { color: red; }
        .neutral { color: gray; }
    </style>
</head>
<body>
    <div class="container text-center">
        <h1 class="mb-4">Amazon Review Sentiment Analyzer</h1>
        <form action="/analyze" method="post">
            <textarea name="review" class="form-control mb-3" placeholder="Enter your review here..." rows="4"></textarea>
            <button type="submit" class="btn btn-primary">Analyze Sentiment</button>
        </form>

        {% if review %}
        <div class="result mt-4">
            <p><strong>Review:</strong> {{ review }}</p>
            <p><strong>Sentiment:</strong> <span class="{{ sentiment|lower }}">{{ sentiment }}</span></p>
            <p><strong>Score:</strong> {{ score }}</p>
        </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_template)

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        review = request.form['review']
        sentiment_score = sia.polarity_scores(review)['compound']
        
        if sentiment_score >= 0.05:
            sentiment = "Positive"
        elif sentiment_score <= -0.05:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        return render_template_string(html_template, review=review, sentiment=sentiment, score=sentiment_score)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
