# 0 flask 패기키 가져오기
import random
from flask import Flask, render_template, request

# 1. app 설정
app = Flask(__name__)

# 2. 요청 경로 (route) + 함수 만들기
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/<string:name>')
def hello(name):
    return render_template('hello.html', name=name)

@app.route('/lunch')
def lunch():
    menu = ['레드코코넛누들', '순두부', '소불고기']    
    return render_template('lunch.html',menu=menu, pick=random.choice(menu))

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/ping')
def ping():
    return render_template('ping.html')    

@app.route('/pong')
def pong():
    # 사용자가 보낸 데이터를 받아 와서 
    text = request.args.get('say')
    ps = request.args.get('ss')
    print(request.args)

    # 템플릿에 넘겨준다.
    return render_template('pong.html',text=text ,ps=ps)    

@app.route('/who')
def who():
    return render_template('who.html')   

@app.route('/result')
def result():
    who = request.args.get('who')
    chr = request.args.get('chr')
    vehicle = request.args.get('vehicle')
    gender = request.args.get('gender')
    if chr == "귀여운":
        url_1 = "static/아이유.jpg"
    elif chr == "예쁜":
        url_1 = "static/임수정.jpg"
    elif chr == "잘생긴":
        url_1 = "static/박보검.jpg"
    
    
    return render_template('result.html',url_1=url_1, who=who ,gender=gender, chr=chr, vehicle=vehicle)

if __name__ == '__main__':
    app.run(debug=True)