from flask import Flask, render_template, request
import csv
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/ask')
def ask():
    quest = request.args.get('question')
    time=datetime.datetime.now()
    dt=time.strftime("%Y년 %m월 %d일 %H시 %M분")
    q_list=[quest, dt]
    with open('question.csv','a') as f:
        writer = csv.writer(f)
        with open('question.csv','r') as fi:
            num = len(list(csv.reader(fi)))
            q_list=[num+1, quest, dt]
        writer.writerow(q_list)
    return render_template('ask.html', quest=q_list)

@app.route('/question')
def question():
    quest_list=[]
    with open('question.csv','r') as i:
        rdr = csv.reader(i)
        for row in rdr:
            quest_list.append(row)
    return render_template('question.html', quest_list=reversed(quest_list))