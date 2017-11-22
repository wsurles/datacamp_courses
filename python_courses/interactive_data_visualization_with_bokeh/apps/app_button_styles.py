# Import CheckboxGroup, RadioGroup, Toggle from bokeh.models
from bokeh.layouts import widgetbox
from bokeh.io import output_file, curdoc
from bokeh.models import CheckboxGroup, RadioGroup, Toggle

# Add a Toggle: toggle
toggle = Toggle(
    label = 'Toggle button',
    button_type = 'success')

# Add a CheckboxGroup: checkbox
checkbox = CheckboxGroup(
    labels = ['Option 1','Option 2','Option 3'])

# Add a RadioGroup: radio
radio = RadioGroup(
    labels = ['Option 1','Option 2','Option 3'])

# Add widgetbox(toggle, checkbox, radio) to the current document
layout = widgetbox(toggle, checkbox, radio)
curdoc().add_root(layout)
