import streamlit as st
import re
import pyperclip


# Function to convert DMS to decimal
def dms_str_to_decimal(dms_str):
    # Regular expression to parse DMS format (e.g., 10°23'42")
    dms_regex = re.compile(
        r"""(?P<degrees>\d+)[°|o]\s*(?P<minutes>\d+)'?\s*(?P<seconds>\d+(?:\.\d+)?|(?:\d+)?)"?"""
    )
    match = dms_regex.match(dms_str.strip())
    if not match:
        st.error(f"Invalid DMS format: {dms_str}")
        return None

    degrees = int(match.group("degrees"))
    minutes = int(match.group("minutes"))
    seconds = float(match.group("seconds")) if match.group("seconds") else 0.0

    return degrees + minutes / 60 + seconds / 3600


st.set_page_config(page_title="Convert DMS to Decimal", page_icon="➡️")

# Initialize session state variables
if "decimal_lat" not in st.session_state:
    st.session_state.decimal_lat = None

if "decimal_lon" not in st.session_state:
    st.session_state.decimal_lon = None

# Title and description
st.title("DMS to Decimal Converter")
st.write(
    "Convert coordinates from Degrees, Minutes, Seconds (DMS) format to Decimal format."
)

# Input fields
st.header("Enter DMS Coordinates")

col1, col2 = st.columns(2)

with col1:
    lat_input = st.text_input("Latitude (e.g., 10°23'42\" or 10o23'42\")")
    lat_dir = st.selectbox("Latitude Direction", options=["N", "S"])

with col2:
    lon_input = st.text_input("Longitude (e.g., 14°42'45\"6 or 14o42'45\"6)")
    lon_dir = st.selectbox("Longitude Direction", options=["E", "W"])

# Convert button
if st.button("Convert"):
    st.session_state.decimal_lat = dms_str_to_decimal(lat_input)
    st.session_state.decimal_lon = dms_str_to_decimal(lon_input)

    if (
        st.session_state.decimal_lat is not None
        and st.session_state.decimal_lon is not None
    ):
        if lat_dir == "S":
            st.session_state.decimal_lat = -st.session_state.decimal_lat
        if lon_dir == "W":
            st.session_state.decimal_lon = -st.session_state.decimal_lon

# Display the results
if (
    st.session_state.decimal_lat is not None
    and st.session_state.decimal_lon is not None
):
    lat_text = f"{st.session_state.decimal_lat:.6f}"
    lon_text = f"{st.session_state.decimal_lon:.6f}"
    combined_text = f"{lat_text}, {lon_text}"

    lat_col, lat_btn_col = st.columns([4, 1])
    lon_col, lon_btn_col = st.columns([4, 1])
    combined_col, combined_btn_col = st.columns([4, 1])

    lat_col.write(f"**Latitude:** {lat_text}")
    if lat_btn_col.button("📋", key="copy_lat"):
        pyperclip.copy(lat_text)
        st.success("Latitude copied to clipboard!")

    lon_col.write(f"**Longitude:** {lon_text}")
    if lon_btn_col.button("📋", key="copy_lon"):
        pyperclip.copy(lon_text)
        st.success("Longitude copied to clipboard!")

    combined_col.write(f"**Latitude, Longitude:** {combined_text}")
    if combined_btn_col.button("📋", key="copy_combined"):
        pyperclip.copy(combined_text)
        st.success("Latitude, Longitude copied to clipboard!")

# Footer
st.markdown("---")
st.write(
    "Use this tool to easily convert DMS coordinates to decimal format for mapping and analysis."
)
