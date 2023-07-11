import streamlit as st
import requests

################################################################################################################################################################
# Dictionaries

trans_built_type = {
    'Residential use': 'Wohnnutzung',
    'Public and special use': 'Gemeinbedarfs- und Sondernutzung',
    'Construction site': 'Baustelle',
    'Commercial and industrial uses, large scale retail': 'Gewerbe- und Industrienutzung, großflächiger Einzelhandel',
    'core land use': 'Kerngebietsnutzung',
    'Mixed use': 'Mischnutzung',
    'Utilities and waste disposal': 'Ver- und Entsorgung',
    'Transportation area (excluding roads)': 'Verkehrsfläche (ohne Straßen)',
    'Weekend home and allotment type uses': 'Wochenendhaus- und kleingartenähnliche Nutzung'
}

trans_low_to_high = {
    'low': 'gering',
    'medium': 'mittel',
    'high': 'hoch'
}

trans_social_inequality = {
    'very low': 'sehr niedrig',
    'low': 'niedrig',
    'medium': 'mittel',
    'high':'hoch'
}

trans_dynamic_social_inequality = {
    'stable': 'stabil',
    'negative': 'negativ',
    'positive': 'positiv'
}

trans_usetype_block = {
    'Multistory residential buildings (1990s and newer)': 'Geschosswohnungsbau der 1990er Jahre und jünger',
    'Refurbished perimeter block development (infill after 1945)': 'Entkernte Blockrandbebauung, Lückenschluss nach 1945',
    'University and research': 'Hochschule und Forschung',
    'Detached single-family houses with gardens': 'Freistehende Einfamilienhäuser mit Gärten',
    'Free row housing with greenery (1950s - 1970s), 2 - 6 stories': 'Freie Zeilenbebauung mit landschaftlichem Siedlungsgrün (1950er - 1970er), 2 - 6-geschossig',
    'Large housing estate and high-rise buildings (1960s - 1990s), 4 - 11 stories and more': 'Großsiedlung und Punkthochhäuser (1960er - 1990er), 4 - 11-geschossig und mehr',
    'Commercial and industrial area, large-scale retail, dense development': 'Gewerbe- und Industriegebiet, großflächiger Einzelhandel, dichte Bebauung',
    'Closed perimeter block development, backyard (1870s - 1918), 5 stories': 'Geschlossene Blockbebauung, Hinterhof (1870er - 1918), 5-geschossig',
    'Closed and semi-open perimeter block development, decorative and garden courtyard (1870s - 1918), 4 stories': 'Geschlossene und halboffene Blockbebauung, Schmuck- und Gartenhof (1870er - 1918), 4-geschossig',
    'Densification in single-family housing area, mixed development with garden and semi-private greening (1870s to present)': 'Verdichtung im Einzelhausgebiet, Mischbebauung mit Garten und halbprivater Umgrünung (1870er bis heute)',
    'New school building (built after 1945)': 'Neubau-Schule (Baujahr nach 1945)',
    'Perimeter block development with large courtyards (1920s - 1940s), 2 - 5 stories': 'Blockrandbebauung mit Großhöfen (1920er - 1940er), 2 - 5-geschossig',
    'Weekend house and small garden-like area': 'Wochenendhaus- und kleingartenähnliches Gebiet',
    'Other and heterogeneous public and special area': 'Sonstiges und heterogenes Gemeinbedarfs- und Sondergebiet',
    'Railway track': 'Gleiskörper',
    'Sports facility, covered': 'Sportanlage, gedeckt',
    'Parking lot': 'Parkplatz',
    'Safety and order': 'Sicherheit und Ordnung',
    'Commercial and industrial area, large-scale retail, low development': 'Gewerbe- und Industriegebiet, großflächiger Einzelhandel, geringe Bebauung',
    'Heterogeneous inner-city mixed development, infill after 1945': 'Heterogene, innerstädtische Mischbebauung, Lückenschluss nach 1945',
    'Sports facility, uncovered': 'Sportanlage, ungedeckt',
    'Church': 'Kirche',
    'Core area': 'Kerngebiet',
    'Train station and railway facilities without railway tracks': 'Bahnhof und Bahnanlagen ohne Gleiskörper',
    'Terraced and semi-detached houses with gardens': 'Reihen- und Doppelhäuser mit Gärten',
    'Villas and town villas with park-like gardens (mostly 1870s - 1945)': 'Villen und Stadtvillen mit parkartigen Gärten (überwiegend 1870er - 1945)',
    'Old school building (built before 1945)': 'Altbau-Schule (Baujahr vor 1945)',
    'Village-like mixed development': 'Dörfliche Mischbebauung',
    'Other traffic area': 'sonstige Verkehrsfläche',
    'Dense block development, closed backyard (1870s - 1918), 5 - 6 stories': 'Dichte Blockbebauung, geschlossener Hinterhof (1870er - 1918), 5 - 6-geschossig',
    'Supply and disposal': 'Ver- und Entsorgung',
    'Mixed area without residential character, low development': 'Mischgebiet ohne Wohngebietscharakter, geringe Bebauung',
    'Construction site': 'Baustelle',
    'Administration': 'Verwaltung',
    'Kindergarten': 'Kindertagesstätte',
    'Parallel row housing with architectural row greenery (1920s - 1930s), 2 - 5 stories': 'Parallele Zeilenbebauung mit architektonischem Zeilengrün (1920er - 1930er), 2 - 5-geschossig',
    'Culture': 'Kultur',
    'Hospital': 'Krankenhaus',
    'Campsite': 'Campingplatz',
    'Mixed development, semi-open and open shed courtyard, 2 - 4 stories': 'Mischbebauung, halboffener und offener Schuppenhof, 2 - 4-geschossig',
    'Other youth facility': 'Sonstige Jugendeinrichtung',
    'Mixed area without residential character, dense development': 'Mischgebiet ohne Wohngebietscharakter, dichte Bebauung'
}

################################################################################################################################################################

st.set_page_config(page_title="Green-Cities-Now: Berlin Prediction!", page_icon="🌳")

st.write("# Green-Cities-Now: Predict")


with st.form("my_form"):
    st.write("Fill the attributes in the following form")
    #slider_val = st.slider("Form slider")

    subsid_val = st.radio(
        "Green Roof Subsidy Program eligibility:",
        ('True', 'False'))


    usetype_block = st.selectbox(
        "Enter type of block usage 👇",
        tuple(trans_usetype_block.keys())
    )


    district_input = st.selectbox(
    "Choose a disctrict 👇",
    ('Charlottenburg-Wilmersdorf',
    'Friedrichshain-Kreuzberg',
    'Lichtenberg',
    'Marzahn-Hellersdorf',
    'Mitte',
    'Neukölln',
    'Pankow',
    'Reinickendorf',
    'Spandau',
    'Steglitz-Zehlendorf',
    'Tempelhof-Schöneberg',
    'Treptow-Köpenick'))

    #Dropdown with building types -> TRANSLATION NEEDED
    built_type_input = st.selectbox(
        "Choose type of building 👇",
        tuple(trans_built_type.keys())
    )

    residents_input = st.number_input(
        "Select number of residents of the block 👇",
        min_value=1,
        value=128,
        step=1
    )

    air_pollution_input = st.select_slider(
    "Enter level of air pollution 👇",
    options=list(trans_low_to_high.keys()),
    value='medium'
)

    thermal_stress_input = st.select_slider(
        "Enter level of thermal stress 👇",
        options=list(trans_low_to_high.keys()),
    value='medium'
)

    social_inequality_input = st.select_slider(
    "Enter social inequality parameter 👇",
    options=list(trans_social_inequality.keys()),
    value='medium'
)

    dynamic_social_inequality_input = st.selectbox(
    "Enter dynamic social inequality parameter 👇",
    options=list(trans_dynamic_social_inequality.keys())
)

    # Change input to EURO
    rent_input = st.number_input(
        "Rent offered on market (eur/m2 per month, cold)  👇",
        min_value=7.21,
        max_value=16.17,
        value=12.9,
        step=5.0
    )

    # Change input to percentage
    unnemployement_benefit_input = st.number_input(
        "Percentage of residents in block receiveing unemployment benefits 👇",
        min_value=0.0246,
        max_value=0.3119,
        value=0.0787,
        step=0.1
    )

    social_housing_input = st.number_input(
        "Percentage of apartments in block that are categorised as social housing 👇",
        min_value=0.0,
        max_value=0.2609,
        value=0.0314,
        step=0.1
    )

    hous_assoc_input = st.number_input(
        "Percentage of apartments owned by city-owned housing associations 👇",
        min_value=0.0,
        max_value=0.53,
        value=0.0393
    )

    rent_duration_input = st.number_input(
        "Percentage of residents having lived there longer than 5 years 👇",
        min_value=0.5241,
        max_value=0.7687,
        value=0.6566
    )

    apartments_sold_input = st.number_input(
        "Apartments sold per 1.000 apartments between 2015 and 2020 👇",
        min_value=0.46,
        max_value=84.35,
        value=70.00,
        step=5.0
    )

    input_data={
    "usetype_block": trans_usetype_block [usetype_block],
    "district": district_input,
    "built_type": trans_built_type[built_type_input],
    "residents": residents_input,
    "air_pollution": trans_low_to_high[air_pollution_input],
    "thermal_stress": trans_low_to_high[thermal_stress_input],
    "social_status": trans_social_inequality[social_inequality_input],
    "social_dyn": trans_dynamic_social_inequality[dynamic_social_inequality_input],
    "rent": rent_input,
    "unemp_benef": unnemployement_benefit_input,
    "social_hou": social_housing_input,
    "hous_assoc": hous_assoc_input,
    "rent_duration": rent_duration_input,
    "aparts_sold": apartments_sold_input,
    "subsidized": subsid_val
    }

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        # API GET call
        #url = 'https://greencitiesnow-3xhym4op3a-ew.a.run.app/predict'

        #url of the new and clean backend
        url = 'https://gcnb-7i5ykxmpsa-ey.a.run.app/predict'
        response = requests.get(url, params= input_data)

        # Displaying prediction:

        def res():
            st.header('Probability of adaptation:')
            if response.json() is False:
                return st.subheader('🧱 Low 🧱')
            if response.json() is True:
                return st.subheader('🌳 High 🌳')


        result = res()
