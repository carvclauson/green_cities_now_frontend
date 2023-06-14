import streamlit as st
from utils import background_image_style

st.set_page_config(page_title="Green-Cities-Now: Berlin ",page_icon="🌳")

st.write("# Welcome to Green-Cities-Now! 👋")

st.markdown(
"""
Green-Cities-Now is an informative/predictive application concerned with one of
the most powerful Climate Change adaptation measures: Green Roofs.

Despite their multiple benefits, implementation of them is slow. This application aims to provide a tool
to predict how likely urban areas are to still implement Green Roofs. Such an analysis should help
in identifying areas that need political intervention to be equipped against the consequences of climate change.

### Berlin - Analysis
- Here we provide an Adaptation-Likelihood analysis of Berlin
- Select different attributes associated with green roofs and explore their relationship

### Prediction
- Plug in your own values for the predictive features and see how likely a block with such attributes is to have a green roof implemented

#### Credits
This project was realized as part of the Le Wagon Data Science bootcamp, with contributions from Raquel Brasileiro, Juanes Hoyos, Clauson da Silva and Margaux Huth.

[![Repo](https://badgen.net/badge/icon/GitHub?icon=github&label)](https://github.com/margaux-go/green_cities_now)
"""


)

image_path = 'images/background_opaque.png'

st.write(background_image_style(image_path), unsafe_allow_html=True)
