from flask import render_template, request, make_response
from flask_wtf import Form
from wtforms.fields.html5 import DecimalRangeField
import matplotlib.pyplot as plt
import mpld3
from mpld3 import plugins
import random
from app import app

class MyForm(Form):
    my_slider = DecimalRangeField('Slider')

def draw_plot(mag):
    fig, ax = plt.subplots()
    xs = range(100)
    ys = [mag * random.randint(1, 50) for x in xs]
    ax.scatter(xs, ys)
    return mpld3.fig_to_html(fig)

@app.route('/', methods=('GET', 'POST'))
def index():
    form = MyForm()
    magnitude = 50
    if request.method == 'POST':
        magnitude = float(request.form['my_slider'])
    fig = draw_plot(magnitude)
    return render_template('index.html',
                           title='Home',
                           form=form,
                           figure=fig)
