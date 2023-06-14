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
            st.markdown("---")
    return grid


# mapbox token
mapboxt = 'MapBox Token'

st.write("## Berlin Climate Change Adaptation Analysis",)
st.markdown(""" Analysis for Berlin is loading... This might take up to one minute.""")

cols_dict = {'green_roof':'Green Roofs',
             'air_pollution':'Air Pollution',
             'thermal_stress': 'Thermal Stress',
             'green_roof_pred': 'Green Roof Prediction'}

cols = ['green_roof','air_pollution','thermal_stress','green_roof_pred']



st.markdown("---")


data = load_data(cols)
j_file = load_geojson()


st.header('Adaptation Prediction')
st.write("""
The lighter the shading of the block (or closer to yellow), the higher the likelihood that green roofs will be implemented.
These areas can be considered to be adapting 'well'.

Purple areas are those where the probability of a green roof being implemented are very low.""")



choro = go.Choroplethmapbox(z=data['green_roof_pred'], locations =
        data.index, colorscale = 'Viridis', geojson = j_file, marker_line_width=0.1)

bounds = go.layout.mapbox.Bounds(east = 13.8, west = 13., north = 52.7, south = 52.32)

margins = go.layout.Margin(b=20,t=20)

layout = go.Layout(
        width=700, height=500,mapbox = dict(center= dict(lat=52.520008,lon=13.404954),
        accesstoken= mapboxt, zoom=4,style="stamen-terrain",bounds = bounds),margin=margins)

fig = go.Figure(data=choro, layout=layout)

st.plotly_chart(fig)

st.markdown("---")

st.header('Model and Data')
st.write("""
    We trained a classification model on data from the Berlin Open Data Portal, which covered 15 features (including
    number of residents, usetype, air pollution, green roof subsidy program eligbility, social inequality index).

    The model was then run on all blocks in Berlin that do not have a green roof as of yet to predict the probability that
    these have a green roof implemented. Knowing that these blocks are in fact empty, allows
    the interpretation that blocks with higher percentages are likely to still implement green roofs, and areas
    with lower percentages will need political and societal intervention, in order to make sure they will adapt as well.

    It is important to note that this is not a potential analysis of where green roofs _can_ be implemented. Seperate analyses
    have shown that the large majority of roofs in Berlin are suitable to carry green roofs.
    """)


st.markdown("---")

# start list of text and supporting graphs
mygrid = make_grid(3,2)


with mygrid[0][0]:
    st.header('Green Roofs')

    st.write(
    """ Green roofs in cities are especially important for their ability to reduce the impacts of
    heavy rain events and urban heat island effects. Additionally they provide habitat for insects
    and contribute to biodiversity conservation.

    Currently only about 3% of roof tops in Berlin are greened. The map on the right displays all blocks in Berlin
    that contain green roofs for more than 15% of the building foot print area, highlighted in yellow color.

    Here, we are presenting green roofs as a proxy for Climate Change adaptation in general. In reality of course, adaptation
    encompasses many more factors that are not considered here.
    """)


with mygrid[1][0]:
    st.header("Air Pollution")
    st.write("""
    Air poulltion data from the Berlin Open Data Portal is categorized into 'high', 'medium' and 'low'. As can be observed in
    the map, the most center of Berlin is most polluted.

    When comparing this map to the current state of green roof coverage in Berlin, we can see that the most
    amount of green roofs are located in the most polluted areas.
    """)

with mygrid[2][0]:
    st.header('Thermal Stress')
    st.write("""
    This last map displays the Thermal Stress categorization from the Berlin Open Data Portal, which indicates areas that
    where on warmer days, the heat can become pysiologically burdonsome. Categories here are also 'high', 'medium' and 'low'.

    Given that the distribution in this map is different from that of Air Pollution, it too, should be taken into account
    for further green roof implementation. Especially combined with our prediction, areas of priority can be identified.

    Areas with high thermal stress, high air pollution and low adaptation likelihood should be the focus of any further political climate change adaptation efforts in Berlin.
    """)


for idx, col in enumerate(cols[:3]):
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
