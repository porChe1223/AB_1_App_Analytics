from app_analytics import app
from flask import render_template

@app.route('/')
def main():
    a = 12
    b = 5
    c = 2

    answers = [
        {
            'plus': a+b,
            'minus': a-b,
        },
        {
            'plus': b+c,
            'minus': b-c,
        },
        {
            'plus': a+c,
            'minus': a-c,
        }
    ]

    minus8 = a-8

    return render_template(
        'main.html', answers = answers, minus8 = minus8 # 引数はいくつでも追加可能
    )
