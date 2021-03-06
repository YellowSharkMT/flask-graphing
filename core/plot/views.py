from flask import Blueprint, make_response
import random
import StringIO
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

plotter = Blueprint('plotter', __name__, template_folder='templates')

@plotter.route('/')
def plot():
    fig = Figure((8,5), dpi=100)
    axis = fig.add_subplot(1, 1, 1)

    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]

    axis.plot(xs, ys)
    canvas = FigureCanvas(fig)
    output = StringIO.StringIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response
