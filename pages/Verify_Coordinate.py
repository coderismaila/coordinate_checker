import streamlit as st
import folium
from streamlit_folium import st_folium


st.set_page_config(page_title="Verify Single Coordinate", page_icon="📈")

st.title("Verify a Single Coordinate")

# Input form for latitude and longitude
st.header("Enter the Latitude and Longitude")

# Get user input for latitude and longitude
latitude = st.number_input("Latitude", format="%.6f")
longitude = st.number_input("Longitude", format="%.6f")

# Initialize session state for map flag
if "map_displayed" not in st.session_state:
    st.session_state.map_displayed = False
if "map_object" not in st.session_state:
    st.session_state["map_object"] = None

# Button to plot the location on the map
if st.button("Plot Location"):
    # Create a Folium map centered around the provided latitude and longitude
    m = folium.Map(location=[latitude, longitude], zoom_start=10)

    # Add a marker at the provided location
    folium.Marker(
        location=[latitude, longitude],
        popup=f"Location: ({latitude}, {longitude})",
        icon=folium.Icon(color="red", icon="info-sign"),
    ).add_to(m)

    # Store map in session state
    st.session_state["map_displayed"] = True
    st.session_state["map_object"] = m

# Display the map if it has been created and stored in session state
if st.session_state["map_displayed"] and st.session_state["map_object"] is not None:
    st_folium(st.session_state["map_object"], width=725, height=500)
