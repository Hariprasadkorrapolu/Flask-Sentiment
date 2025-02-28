<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sentiment Analyzer</title>
    <style>
        body { 
            font-family: 'Poppins', sans-serif;
            background-color: #f4f4f4;
            text-align: center;
            padding: 20px;
        }
        .container {
            background: white;
            padding: 20px;
            max-width: 500px;
            margin: auto;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }
        textarea {
            width: 90%;
            height: 100px;
            padding: 10px;
            border-radius: 5px;
            border: 1px solid #ddd;
        }
        button {
            background: #007BFF;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background: #0056b3;
        }
        .result-box {
            margin-top: 20px;
            padding: 15px;
            border-radius: 5px;
            font-size: 18px;
            font-weight: bold;
        }
        .positive { background: #d4edda; color: #155724; }
        .negative { background: #f8d7da; color: #721c24; }
        .neutral  { background: #fff3cd; color: #856404; }
    </style>
</head>
<body>

    <div class="container">
        <h1>Amazon Review Sentiment Analyzer</h1>
        <form action="/analyze" method="post">
            <textarea name="review" placeholder="Enter your review here..."></textarea><br><br>
            <button type="submit">Analyze Sentiment</button>
        </form>
        
        {% if review %}
            <div class="result-box {% if sentiment == 'Positive' %}positive{% elif sentiment == 'Negative' %}negative{% else %}neutral{% endif %}">
                <p><strong>Review:</strong> {{ review }}</p>
                <p><strong>Sentiment:</strong> {{ sentiment }}</p>
                <p><strong>Score:</strong> {{ score }}</p>
            </div>
        {% endif %}
    </div>

</body>
</html>
