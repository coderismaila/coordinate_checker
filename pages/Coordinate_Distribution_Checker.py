import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

st.title("Coordinate Distribution Checker")

uploaded_file = st.file_uploader("Upload your Excel file", type="xlsx")

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)

    st.write("Uploaded Data:")
    st.dataframe(df.head())

    # Search for possible latitude and longitude columns
    lat_col = None
    lon_col = None
    dss_code_col = None
    dss_name_col = None

    for col in df.columns:
        if "lat" in col.lower():
            lat_col = col
        if "lon" in col.lower() or "lng" in col.lower() or "long" in col.lower():
            lon_col = col
        if "dss code" in col.lower():
            dss_code_col = col
        if "substation name" in col.lower():
            dss_name_col = col

    if lat_col and lon_col:
        # Remove rows with invalid or missing latitude/longitude values
        df = df.dropna(subset=[lat_col, lon_col])

        # Convert latitude and longitude to numeric, coercing errors to NaN
        df[lat_col] = pd.to_numeric(df[lat_col], errors="coerce")
        df[lon_col] = pd.to_numeric(df[lon_col], errors="coerce")

        # Drop rows with non-numeric latitude/longitude values
        df = df.dropna(subset=[lat_col, lon_col])

        # Remove rows with invalid latitude or longitude (not within valid range)
        df = df[(df[lat_col].between(-90, 90)) & (df[lon_col].between(-180, 180))]

        if "selected_data" not in st.session_state:
            st.session_state["selected_data"] = []

        if not df.empty:
            # Calculate the mean latitude and longitude for centering the map
            latitude_mean = df[lat_col].mean()
            longitude_mean = df[lon_col].mean()

            # Initialize the foium map
            m = folium.Map(
                max_bounds=True,
                location=[latitude_mean, longitude_mean],
                zoom_start=5,
            )

            # Add markers to the map
            for index, row in df.iterrows():
                folium.Marker(
                    location=[row[lat_col], row[lon_col]],
                    popup=f"{row[dss_name_col]}(<span style='font-weight: 700;'>{row[dss_code_col]}</span>)<br>{row[lat_col]}, {row[lon_col]}",
                    icon=folium.Icon(icon="arrow-down", color="green"),
                ).add_to(m)

            # Display the map using streamlit-folium
            map_data = st_folium(m, width=725)

        else:
            st.warning(
                "No valid data points available after cleaning. Please check your file."
            )
    else:
        st.error(
            "Could not find latitude and longitude columns automatically. Please ensure your file contains columns with 'lat' and 'lon', 'lng', or 'long' in their names."
        )
else:
    st.info("Please upload an Excel file to display the map.")
