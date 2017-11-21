# Perform necessary imports
from bokeh.io import curdoc
from bokeh.plotting import figure

##|----------------
##| Create Plot
##|----------------

# Create a new plot: plot
plot = figure()

# Add a line to the plot
plot.line(x = [1,2,3,4,5], y = [2,5,4,6,7])

# Add the plot to the current document
curdoc().add_root(plot)

##|----------------
##| Create Sliders
##|----------------

# Perform necessary imports
from bokeh.layouts import widgetbox
from bokeh.models import Slider

# Create first slider: slider1
slider1 = Slider(
    title = 'slider1',
    start = 0,
    end = 10,
    step = 0.1,
    value = 2)

# Create second slider: slider2
slider2 = Slider(
    title = 'slider2',
    start = 10,
    end = 100,
    step = 1, 
    value = 20)

# Add slider1 and slider2 to a widgetbox
layout = widgetbox(slider1, slider2)

# Add the layout to the current document
curdoc().add_root(layout)
