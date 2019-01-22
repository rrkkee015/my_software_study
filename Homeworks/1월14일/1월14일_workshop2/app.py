from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/dictionary/<string>")
def apple(string):
    dic={'apple':'사과','grape':'포도'}
    if string in dic.keys():
        return f'{string}은(는) {dic[string]}!'
    else:
        return f'{string}은(는) 나만의 단어장에 없는 단어입니다!'