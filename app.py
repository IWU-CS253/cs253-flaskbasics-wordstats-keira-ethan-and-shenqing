from flask import Flask, render_template, request

app = Flask(__name__)

WORD_COUNTS =[]
@app.route('/')

def index():
    return render_template("index.html")

@app.route('/count', methods=['POST'])

def count():
    string = request.form.get("string")
    words = string.split(' ')
    for word in words:
        word = word.strip('.').strip('!').strip('?')
        WORD_COUNTS.append(word)

    count = 0
    character = 0
    for word in WORD_COUNTS:
        count += 1
        for char in word:
            character += 1

    average = character/count

    return render_template("count.html", count="count", character="character", average="average")

