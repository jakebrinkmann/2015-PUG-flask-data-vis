from flask import render_template, request
from flask_wtf import Form
from wtforms.fields.html5 import DecimalRangeField
from app import app

class MyForm(Form):
    my_slider = DecimalRangeField('Slider')

@app.route('/', methods=('GET', 'POST'))
def index():
    form = MyForm()
    user = {'nickname': 'Dr. Robert'}
    if request.method == 'POST':
        value = request.form['my_slider']
        user['nickname'] = value
    return render_template('index.html',
                           title='Home',
                           user=user,
                           form=form)
