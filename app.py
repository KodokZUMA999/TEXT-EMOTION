from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        if sentiment > 0:
            emotion = "Senang"
        elif sentiment < 0:
            emotion = "Sedih"
        else:
            emotion = "Netral"
        return render_template('index.html', text=text, emotion=emotion)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
