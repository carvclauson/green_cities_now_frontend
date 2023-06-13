import streamlit as st
import requests


st.set_page_config(page_title="Green-Cities-Now: Berlin Prediction!", page_icon="🌳")

st.write("# Green-Cities-Now: Predict")


with st.form("my_form"):
    st.write("Fill the attributes in the following form")
    #slider_val = st.slider("Form slider")
    subsid_val = st.checkbox("Check in case subsidized")

    air_pollution_input = st.text_input(
        "Enter air pollution parameter 👇"
    )

    thermal_stress_input = st.text_input(
        "Enter thermal stress parameter 👇"
    )

    social_inequality_input = st.text_input(
        "Enter social inequality parameter 👇"
    )

    dynamic_social_inequality_input = st.text_input(
        "Enter dynamic social inequality parameter 👇"
    )

    rent_input = st.text_input(
        "Enter rent parameter 👇"
    )

    unnemployement_benefit_input = st.text_input(
        "Enter unnemployement benefits parameter 👇"
    )

    social_housing_input = st.text_input(
        "Enter social housing parameter 👇"
    )

    city_owned_input = st.text_input(
        "Enter city owned parameter 👇"
    )

    rent_duration_input = st.text_input(
        "Enter rent duration parameter 👇"
    )

    apartments_sold_input = st.text_input(
        "Enter apartment solds parameter 👇"
    )

    input_data={
    "subsidized": subsid_val,
    "air_pollut": air_pollution_input,
    "thermal_st": thermal_stress_input,
    "status_val": social_inequality_input,
    "dyn_val": dynamic_social_inequality_input,
    "rent": rent_input,
    "unemp_bene": unnemployement_benefit_input,
    "social_hou": social_housing_input,
    "city_owned": city_owned_input,
    "rent_durat": rent_duration_input,
    "aparts_sol": apartments_sold_input
    }

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        #st.write("slider", slider_val, "checkbox", checkbox_val)
        #st.write("checkbox", subsid_val)

        #testing get call
        #url = f'https://greencitiesnow-3xhym4op3a-ew.a.run.app/predict?subsidized={subsid}'
        #response = requests.get(url)

        #testing post call

        url = 'https://greencitiesnow-3xhym4op3a-ew.a.run.app/prediction/{pred_id}'
        response = requests.post(url,json = input_data)
        st.markdown(response.json())
