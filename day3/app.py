#flask app 만드는 코드 덩어리

import random
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('hello.html')
#def 함수를 만들었다.

@app.route('/hi')
def hi():
    return render_template('hi.html')

# variable routung! 경로를 변수로 활용한다.
@app.route('/hi/<string:name>')
def hiname(name):
    return render_template('hi2.html', namee=name)

# /cube/<숫자>
# 세제곱 결과를 보여주는 페이지
@app.route('/cube/<int:num>')
def cube(num):
    return f'{num**3}'

# /lunch/사람이름
@app.route('/lunch/<string:name>')
def lunch (name):
    menu = ['한식','중식']
    # pick = random.choice(menu)
    # return f'{name}아 {pick}먹어'
    return render_template('lunch.html', name=name ,pick=random.choice(menu))


# /lotto
# 로또 번호 6개를 추천해주는 페이지
@app.route("/lotto")
def lotto():
    numbers = range(1,46)
    lotto = random.sample(numbers,6)
    return f'이번주 당첨번호는 {lotto}!! '

if __name__ == '__main__':
    #python app.py를 하면 아ㅐ의 코드 블록을 실행시킨다.
    app.run(debug=True)
