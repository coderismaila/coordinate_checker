# Coordinate Verification App

## Overview

The Coordinate Verification App is a Streamlit-based application designed to manage and verify geographic coordinates. It provides users with tools to check the distribution of coordinates from uploaded files and to verify individual coordinates by plotting them on an interactive map.

## Features

- **Coordinate Distribution Checker**: Upload a file containing coordinates (latitude and longitude) to visualize and verify their distribution on a map. The app supports basic data cleaning, removing invalid or malformed coordinates before plotting.
  
- **Single Coordinate Verifier**: Input a single coordinate to verify its accuracy and location on a map. This feature is useful for quickly checking specific coordinates.

## Project Structure

```
coordinate_checker/
│
├── pages/
│   ├── Coordinate_Distribution_Checker.py  # Page to check distribution of coordinates
│   └── Verify_Coordinate.py                # Page to verify a single coordinate
│
├── index.py                                # Main index page of the app
└── README.md                               # Project README file
```

- **index.py**: This is the main entry point of the app. It serves as the homepage, providing an overview of the app’s functionality and links to the different pages.

- **pages/Coordinate_Distribution_Checker.py**: This page allows users to upload a file (e.g., Excel) containing coordinates and visualize their distribution on a map. The app automatically cleans the data by removing invalid or string-based coordinates.

- **pages/Verify_Coordinate.py**: This page allows users to input a single latitude and longitude, which is then plotted on an interactive map to verify its location.

## Installation

To run the app locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/coordinate-verification-app.git
   cd coordinate-verification-app
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Streamlit app**:
   ```bash
   streamlit run index.py
   ```

## Usage

Access the app via your web browser. The homepage provides links to the key features:

### 1. **Check Coordinate Distribution**

Upload an Excel file to visualize the distribution of coordinates on a map.

- **File Preparation**: Ensure the file is in `.xlsx` format with at least two columns for **latitude** and **longitude**.
- **Upload**: Go to the "Check Coordinate Distribution" page, upload your file, and the app will clean and plot the data on a map.
- **Interact**: Zoom in/out and click markers for details. You can also export selected points to a CSV file.

### 2. **Verify Single Coordinate**

Manually input a coordinate to verify its location on a map.

- **Input**: Enter latitude and longitude on the "Verify Single Coordinate" page.
- **Plot**: Click "Plot Location" to see the coordinate on an interactive map.

This allows for quick and easy verification and analysis of geographic data.

## Dependencies

The app is built using the following Python libraries:

- **Streamlit**: For building the interactive web application.
- **Folium**: For generating interactive maps.
- **Pandas**: For handling data in tabular form (e.g., Excel files).
- **streamlit-folium**: For integrating Folium maps within the Streamlit app.

Ensure you have all dependencies installed by running:

```bash
pip install -r requirements.txt
```

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The app was developed using Streamlit, a powerful tool for building interactive data applications in Python.
- Folium was used to integrate interactive maps into the app.

---

This README should provide a comprehensive guide to your project, helping users and contributors understand the app's purpose, how to install and use it, and how they can contribute.
