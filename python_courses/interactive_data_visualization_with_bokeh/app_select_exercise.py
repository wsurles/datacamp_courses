import numpy as np
import pandas as pd
from bokeh.models import ColumnDataSource, Select
from bokeh.plotting import figure, show
from bokeh.layouts import column
from bokeh.io import output_file, curdoc


##| Load data

file = 'https://assets.datacamp.com/production/course_1392/datasets/literacy_birth_rate.csv'
female = pd.read_csv(file)

source = ColumnDataSource(data = {
    'x': female['fertility'],
    'y': female['female literacy']
})

##| Plot

plot = figure()
plot.circle('x','y', source = source)
# output_file('plots/circle_female.html')
# show(plot)

##| Select input

select = Select(
    title = 'Y-Metric',
    options = ['female literacy', 'population'],
    value = 'femaile literacy')

##| Update plot

def update_plot(attr, old, new):
    if new == 'female literacy':
        source.data = {'x': female['fertility'], 'y': female['female literacy']}
    else:
        source.data = {'x': female['fertility'], 'y': female['population']}

select.on_change('value', update_plot)

##| Layout

layout = column(select, plot)
curdoc().add_root(layout)
