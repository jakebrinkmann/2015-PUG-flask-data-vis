from flask import render_template, request, make_response
from flask_wtf import Form
from wtforms.fields.html5 import DecimalRangeField
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import random
import StringIO
from app import app

class MyForm(Form):
    my_slider = DecimalRangeField('Slider')

@app.route('/<int:mag>/plot.png')
def plot(mag):
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)

    xs = range(100)
    ys = [mag * random.randint(1, 50) for x in xs]

    axis.plot(xs, ys)
    canvas = FigureCanvas(fig)
    output = StringIO.StringIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response

@app.route('/', methods=('GET', 'POST'))
def index():
    form = MyForm()
    magnitude = 50
    if request.method == 'POST':
        magnitude = float(request.form['my_slider'])
    return render_template('index.html',
                           title='Home',
                           mag=magnitude,
                           form=form)
