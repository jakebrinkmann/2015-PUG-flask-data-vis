from flask import Flask

app = Flask(__name__)

@app.route('/')
def show_html():
    return '<h1>Big heading</h1><p>And some <b>paragraph</b> text</p>'

if __name__ == '__main__':
    app.run()
