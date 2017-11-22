from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Select
from bokeh.plotting import figure
from numpy.random import random, normal, lognormal

##|-------------
##| Plot
##|-------------

N = 1000
source = ColumnDataSource(
    data = {'x': random(N), 'y': random(N)})

plot = figure()
plot.circle(x='x', y='y', source=source)

##|-------------
##| Select Box
##|-------------

menu = Select(
    options=['uniform','normal','lognormal'],
    value = 'uniform',
    title = 'Distribution')

##|-------------
##| Callbacks
##|-------------

def callback(attr, old, new):

    if menu.value == 'uniform':
        f = random
    elif menu.value == 'normal':
        f = normal
    else:
        f = lognormal

    source.data = {'x': f(size=N), 'y': f(size=N)}

menu.on_change('value', callback)

##|-------------
##| Layout
##|-------------

layout = column(menu, plot)

curdoc().add_root(layout)
