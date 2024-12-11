from app_analytics import app
from flask import render_template

@app.route('/')
def main():
    a = 12
    b = 5
    answer = {
        'plus': a+b,
        'minus': a-b,
    }

    minus8 = a-8
    
    return render_template(
        'main.html', answer = answer, minus8 = minus8 # 引数はいくつでも追加可能
    )
