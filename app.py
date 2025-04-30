from flask import Flask, render_template
import requests

app = Flask(__name__)

def get_random_meme():
    url = "https://meme-api.com/gimme"
    response = requests.get(url)
    data = response.json()
    return data["url"]

@app.route('/')
def index():
    meme_url = get_random_meme()
    return render_template('index.html', meme_url=meme_url)

if __name__ == '__main__':
    app.run(debug=True)
