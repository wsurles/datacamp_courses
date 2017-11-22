
from bokeh.layouts import widgetbox, column
from bokeh.models import Select, ColumnDataSource
from bokeh.io import curdoc

select1 = Select(
    title = 'First',
    options = ['A','B'],
    value = 'A'
)

select2 = Select(
    title = 'Second',
    options = ['1','2','3'],
    value = '1'
)

def callback(attr, old, new):
    if select1.value == 'A':
        select2.options = ['1','2','3']
        select2.value = '1'
    else:
        select2.options = ['100','200','300']
        select2.value = '100'

select1.on_change('value', callback)

layout = widgetbox(select1, select2)
curdoc().add_root(layout)
