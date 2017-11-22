# Perform necessary imports
import numpy as np
import pandas as pd
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.models import HoverTool, ColumnDataSource, CategoricalColorMapper, Slider, Select
from bokeh.io import output_file, curdoc
from bokeh.palettes import Spectral6
from bokeh.layouts import widgetbox, row

##|-------------
##| Load Data
##|-------------

file = 'https://assets.datacamp.com/production/course_1392/datasets/gapminder_tidy.csv'
data = pd.read_csv(file, index_col = 'Year')

regions_list = data.region.unique().tolist()

# Turn population into bubble sizes.
# Use min_size and factor to tweak.
def scale_pop(pop):
    """scale the population size to look good as bubbles"""
    scaling  = 200
    pop_size = np.sqrt(pop / np.pi) / scaling
    min_size = 5
    pop_size = pop_size.where(pop_size >= min_size).fillna(min_size)
    return pop_size

pop_size = scale_pop(data.loc[1970].population)

# Make the ColumnDataSource: source
source = ColumnDataSource(data={
    'x'             : data.loc[1970].fertility,
    'y'             : data.loc[1970].life,
    'country'       : data.loc[1970].Country,
    'region'        : data.loc[1970].region,
    'population'    : data.loc[1970].population,
    'pop_size'      : scale_pop(data.loc[1970].population)
})
##|-------------
##| Inputs
##|-------------

slider = Slider(
    title = 'Year',
    start = 1970,
    end = 2010,
    step = 1,
    value = 1970)

x_select = Select(
    options=['fertility', 'life', 'child_mortality', 'gdp'],
    value='fertility',
    title='x-axis data')

y_select = Select(
    options=['fertility', 'life', 'child_mortality', 'gdp'],
    value='life',
    title='y-axis data')

##|-------------
##| Plots
##|-------------

# Create the figure: p
plot = figure(
    title= 'Gapminder data for 1970',
    x_axis_label='Fertility (children per woman)',
    y_axis_label='Life Expectancy (years)',
    plot_height=400,
    plot_width=700)

# Make a color mapper: color_mapper
color_mapper = CategoricalColorMapper(factors=regions_list, palette=Spectral6)

# Add a circle glyph to the figure p
plot.circle(
    x='x', y='y',
    source=source,
    fill_alpha=0.8,
    size = 'pop_size',
    line_color='#7c7e71',
    line_width=0.5,
    line_alpha=0.5,
    color=dict(field='region', transform=color_mapper),
    legend='region')

hover = HoverTool(
    tooltips = [('Country', '@country')])

plot.add_tools(hover)

## Plot styling
plot.legend.location = 'bottom_left'
plot.legend.background_fill_alpha = 0.3
plot.legend.label_text_font_size = '8pt'

##|-------------
##| Callbacks
##|-------------

def update_plot(attr, old, new):

    ## Read current values from inputs
    yr = slider.value
    x = x_select.value
    y = y_select.value

    ## Label plot axes
    plot.xaxis.axis_label = x
    plot.yaxis.axis_label = y

    ## Set new data
    new_data = {
        'x'             : data.loc[yr][x],
        'y'             : data.loc[yr][y],
        'country'       : data.loc[yr].Country,
        'region'        : data.loc[yr].region,
        'population'    : data.loc[yr].population,
        'pop_size'      : scale_pop(data.loc[yr].population)

    }
    source.data = new_data

    ## Set the range of all axes
    plot.x_range.start = min(data[x])
    plot.x_range.end = max(data[x])
    plot.y_range.start = min(data[y])
    plot.y_range.end = max(data[y])

    ## Add title to plot based on year selected
    plot.title.text = 'Gapminder data for %d' % yr

# Attach the callback to the 'value' property of inputs
slider.on_change('value', update_plot)
x_select.on_change('value', update_plot)
y_select.on_change('value', update_plot)

##|-------------
##| Layout
##|-------------

# Add the plot to the current document and add the title
layout = row(widgetbox(slider, x_select, y_select), plot)
curdoc().add_root(layout)
curdoc().title = 'Gapminder'
