# Perform necessary imports
from bokeh.io import curdoc
from bokeh.plotting import figure
from bokeh.layouts import widgetbox, column
from bokeh.models import Slider, ColumnDataSource
import numpy as np

##|----------------
##| Create Sliders
##|----------------

# Create first slider: slider1
slider1 = Slider(
    title = 'slider1',
    start = 1,
    end = 10,
    step = 1,
    value = 2)

# Add slider1 and slider2 to a widgetbox
layout = widgetbox(slider1)

##|----------------
##| Create Plot
##|----------------

x = np.arange(0,20,0.01)
y = np.sin(x/2)

source = ColumnDataSource(data = {'x': x,'y': y})

# Create a new plot: plot
plot = figure()

# Add a line to the plot
plot.line('x', 'y', source = source)

##|------------------------
##| Create Slider Callback
##|------------------------

# Define a callback function: callback
def callback(attr, old, new):

    # Read the current value of the slider: scale
    scale = slider1.value

    # Compute the updated y using np.sin(scale/x): new_y
    new_y = np.sin(x/scale)

    # Update source with the new data values
    source.data = {'x': x, 'y': new_y}

# Attach the callback to the 'value' property of slider
slider1.on_change('value', callback)

# Create layout and add to current document
layout = column(widgetbox(slider1), plot)
curdoc().add_root(layout)
