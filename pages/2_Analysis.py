import streamlit as st
from utils import load_geojson, load_data
import plotly.graph_objs as go
import matplotlib.pyplot as plt

st.set_page_config(page_title="Green-Cities-Now: Berlin Analysis!", page_icon="🌳")

#function to make grid
def make_grid(cols,rows):
    grid = [0]*cols
    for i in range(cols):
        with st.container():
            grid[i] = st.columns(rows, gap='medium')
    return grid


# mapbox token
mapboxt = 'MapBox Token'

st.write("# Berlin Climate Change Adaptation Analysis")
st.markdown(""" Analysis for Berlin is loading. This might take up
            to a minute.""")

cols_dict = {'green_roof':'Green Roofs',
             'air_pollution':'Air Pollution',
             'thermal_stress': 'Thermal Stress',
             'green_roof_pred': 'Green Roof Prediction'}

cols = ['green_roof','green_roof_pred','air_pollution','thermal_stress']



st.markdown("---")


data = load_data(cols)
j_file = load_geojson()

mygrid = make_grid(4,2)


with mygrid[0][0]:
    st.header('Green Roofs')

    st.write(
    """Since 1975 the world has been growing by billion people every 12 years.
    It passed 7 billion in 2011 and, by the end of 2022,
    #there will be 8 billion people in the world.
    #But, the growth rate is below 1%, less than half its peak rate of growth - of 2.3% - in the 1960s.

    #Since 1975 the world has been growing by billion people every 12 years.
    #It passed 7 billion in 2011 and, by the end of 2022,
    #there will be 8 billion people in the world.
    #But, the growth rate is below 1%, less than half its peak rate of growth - of 2.3% - in the 1960s.
    """)

with mygrid[1][0]:
    st.header('Green Roof Prediction')
    st.write("""
    \n \n \n \n Since 1975 the world has been growing by billion people every 12 years.
    It passed 7 billion in 2011 and, by the end of 2022,
    #there will be 8 billion people in the world.
    #But, the growth rate is below 1%, less than half its peak rate of growth - of 2.3% - in the 1960s.

    #Since 1975 the world has been growing by billion people every 12 years.
    #It passed 7 billion in 2011 and, by the end of 2022,
    #there will be 8 billion people in the world.
    #But, the growth rate is below 1%, less than half its peak rate of growth - of 2.3% - in the 1960s.

    #""")

with mygrid[2][0]:
    st.header("Air Pollution")
    st.write("""
    \n \n \n \n Since 1975 the world has been growing by billion people every 12 years.
    It passed 7 billion in 2011 and, by the end of 2022,
    #there will be 8 billion people in the world.
    #But, the growth rate is below 1%, less than half its peak rate of growth - of 2.3% - in the 1960s.

    #Since 1975 the world has been growing by billion people every 12 years.
    #It passed 7 billion in 2011 and, by the end of 2022,
    #there will be 8 billion people in the world.
    #But, the growth rate is below 1%, less than half its peak rate of growth - of 2.3% - in the 1960s.

    #""")

with mygrid[3][0]:
    st.header('Thermal Stress')
    st.write("""
    \n \n \n \n Since 1975 the world has been growing by billion people every 12 years.
    It passed 7 billion in 2011 and, by the end of 2022,
    #there will be 8 billion people in the world.
    #But, the growth rate is below 1%, less than half its peak rate of growth - of 2.3% - in the 1960s.

    #Since 1975 the world has been growing by billion people every 12 years.
    #It passed 7 billion in 2011 and, by the end of 2022,
    #there will be 8 billion people in the world.
    #But, the growth rate is below 1%, less than half its peak rate of growth - of 2.3% - in the 1960s.

    #""")


for idx, col in enumerate(cols):
    choro = go.Choroplethmapbox(z=data[col], locations =
            data.index, colorscale = 'Viridis', geojson = j_file, marker_line_width=0.1)

    bounds = go.layout.mapbox.Bounds(east = 13.8, west = 13., north = 52.7, south = 52.32)

    margins = go.layout.Margin(b=20,t=20)

    layout = go.Layout(
            width=600, height=500,mapbox = dict(center= dict(lat=52.520008,lon=13.404954),
            accesstoken= mapboxt, zoom=4,style="stamen-terrain",bounds = bounds),margin=margins)

    fig = go.Figure(data=choro, layout=layout)

    mygrid[idx][1].plotly_chart(fig)

# if submitted:
#     data = load_data(cols)
#     j_file = load_geojson()
#     choro = go.Choroplethmapbox(z=green_roof['green_roof'], locations =
#             green_roof.index, colorscale = 'Viridis', geojson = j_file, marker_line_width=0.1)

#     bounds = go.layout.mapbox.Bounds(east = 14., west = 13., north = 52.8, south = 52.2)

#     layout = go.Layout(title_text ='Berlin Blocks', title_x =0.5,
#             width=950, height=700,mapbox = dict(center= dict(lat=52.520008,lon=13.404954),
#             accesstoken= mapboxt, zoom=4,style="stamen-terrain",bounds = bounds))

#     fig = go.Figure(data=choro, layout=layout)
#     # display streamlit map
#     st.plotly_chart(fig)



# # CODE TO ALLOW LAYERS
# # define layers and plot map
# choro = go.Choroplethmapbox(z=green_roof['green_roof'], locations =
#         green_roof.index, colorscale = 'Viridis', geojson = j_file, marker_line_width=0.1)

# bounds = go.layout.mapbox.Bounds(east = 14., west = 13., north = 53, south = 52)

# layout = go.Layout(title_text ='Berlin Blocks', title_x =0.5,
#         width=950, height=700,mapbox = dict(center= dict(lat=52.520008,lon=13.404954),
#         accesstoken= mapboxt, zoom=4,style="stamen-terrain",bounds = bounds))

# # streamlit multiselect widget
# layer1 = st.multiselect('Layer Selection', [choro],
#          format_func=lambda x: 'Polygon' if x==choro else 'Points')

# # assign Graph Objects figure
# fig = go.Figure(data=layer1, layout=layout)
# # display streamlit map
# st.plotly_chart(fig)
