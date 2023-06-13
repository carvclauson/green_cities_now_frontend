import streamlit as st
from utils import load_geojson, load_data
import plotly.graph_objs as go

st.set_page_config(page_title="Green-Cities-Now: Berlin Analysis!", page_icon="🌳")

# mapbox token
mapboxt = 'MapBox Token'

st.write("# Green-Cities-Now: Analysis")
st.markdown(""" Click Reveal to show information about Berlin. This might take up
            to a minute.""")

cols_dict = {'green_roof':'Green Roofs',
             'air_pollution':'Air Pollution'}

cols = []
green_roof = st.checkbox("Green Roofs")
air_pollut = st.checkbox("Air Pollution")

if green_roof:
    cols.append("green_roof")
if air_pollut:
    cols.append("air_pollution")

submitted = st.button("Reveal")

if submitted:

    data = load_data(cols)
    j_file = load_geojson()

    for col in cols:
        choro = go.Choroplethmapbox(z=data[col], locations =
                data.index, colorscale = 'Viridis', geojson = j_file, marker_line_width=0.1)

        bounds = go.layout.mapbox.Bounds(east = 14., west = 13., north = 52.8, south = 52.2)

        layout = go.Layout(title_text =cols_dict[col], title_x =0.5,
                width=950, height=700,mapbox = dict(center= dict(lat=52.520008,lon=13.404954),
                accesstoken= mapboxt, zoom=4,style="stamen-terrain",bounds = bounds))

        fig = go.Figure(data=choro, layout=layout)
        # display streamlit map
        st.plotly_chart(fig)


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
