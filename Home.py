import streamlit as st
from utils import background_image_style

st.set_page_config(page_title="Green-Cities-Now: Berlin ",page_icon="🌳")

st.write("# Welcome Green-Cities-Now! 👋")

st.markdown(
"""
Green-Cities-Now is an informative/predictive application concerned with one of
society's most powerful tools against the impacts of Global Warming: Green Roofs.

### Analysis
- Check the current situation regarding Green roofs in your city
- Select different attributes associated with green roofs and visualize their correlation.

### Prediction
- Our model shows you how given attributes for a block match the attributes of blocks where a relevant portion of the roofs are green. This can be interpreted as a likelihood of a given block to achieve the same portion of green roofs.
"""
)

image_path = 'images/background_opaque.png'

st.write(background_image_style(image_path), unsafe_allow_html=True)
