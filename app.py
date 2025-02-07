from flask import Flask, render_template, request

app = Flask(__name__)


WORD_COUNTS =[]
@app.route('/')

def index():
    return render_template("index.html")

@app.route('/count', methods=['POST'])

def count():
    text = request.form.get("string")
    print(text)
    words_ = text.split(' ')
    for word in words_:
        word = word.strip('.').strip('!').strip('?')
        WORD_COUNTS.append(word)

    word = 0
    character = 0
    for words in WORD_COUNTS:
        word += 1
        for char in words:
            character += 1

    average = character/word

    return render_template("count.html", word=word, character=character, average=average)

