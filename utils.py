import streamlit as st
import base64

import json
import geopandas as gpd
import pyproj
import pandas as pd


@st.cache_data
def load_image(path):
    with open(path, 'rb') as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    return encoded


def background_image_style(path):
    encoded = load_image(path)
    style = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
    }}
    </style>
    '''
    return style

@st.cache_data
def create_geojson():
        # reading in the polygon shapefile
    map_df = gpd.read_file("./data/geometry.shp")

    # set GeoJSON file path
    path_json = ("./data/geojson.json")

    # write GeoJSON to file.
    # DON'T NEED TO BE EXECUTED EVERYTIME
    map_df.to_file(path_json, driver = "GeoJSON")

    with open('./data/geojson.json') as geofile:
        j_file = json.load(geofile)

    # index geojson
    i=1
    for feature in j_file["features"]:
        feature['id'] = str(i).zfill(2)
        i += 1
    return j_file


@st.cache_data
def load_geojson():
    with open('./data/geojson.json') as geofile:
        j_file = json.load(geofile)

    # index geojson
    i=1
    for feature in j_file["features"]:
        feature['id'] = str(i).zfill(2)
        i += 1
    return j_file

def load_data(cols):

    # reading columns info
    data = pd.read_csv('./data/analysis_cols.csv', usecols=cols)
    return data
