from flask import render_template, request, make_response
from flask_wtf import Form
from wtforms.fields.html5 import DecimalRangeField
from wtforms import RadioField
from bokeh.embed import components
from bokeh.plotting import figure
import random
from app import app

class MyForm(Form):
    my_slider = DecimalRangeField('Mag')
    my_radio = RadioField('Color', choices=[('#c51b8a','Pink'),('#5ab4ac','Teal')])

def draw_plot(mag, color):
    xs = range(100)
    ys = [(mag + x) **2 + random.randint(1, 50) for x in xs]
    fig = figure(title="Polynomial", plot_width=500, plot_height=400)
    fig.line(xs, ys, color=color, line_width=2)
    return fig

@app.route('/', methods=('GET', 'POST'))
def index():
    form = MyForm()
    magnitude = 50
    color = '#67a9cf'
    if request.method == 'POST':
        magnitude = float(request.form['my_slider'])
        color = request.form['my_radio']
    fig = draw_plot(magnitude, color)
    script, div = components(fig)
    return render_template('index.html',
                           title='Home',
                           form=form,
                           div=div, script=script)
