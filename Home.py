import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="📌",
)

# Set the title of the main page
st.title("Welcome to the Coordinate Verification App")

# Description of the app
st.write(
    """
This app is designed to help you manage and verify coordinates efficiently.
You can:
- Check the distribution of coordinates by uploading a file.
- Verify individual coordinates to ensure they are correctly placed on the map.

Please use the navigation links below to access the different functionalities of the app.
"""
)

# Navigation Links to Other Pages
st.markdown("### Navigation")
st.page_link(
    page="pages/Coordinate_Distribution_Checker.py",
    label="Coordinate Distribution Checker",
    icon="1️⃣",
)
st.page_link(page="pages/Verify_Coordinate.py", label="Verify Coordinate", icon="2️⃣")

# Footer
st.markdown("---")
st.write(
    "This app is built using Streamlit to streamline coordinate management and verification tasks for the Technical Staffs of Kaduna Electric."
)
