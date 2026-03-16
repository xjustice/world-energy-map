# World Energy Map 🌍⚡

Welcome to the **World Energy Map**, an interactive choropleth web application that visualizes global per capita electricity consumption data.

**Live Demo:** [https://xjustice.github.io/world-energy-map/](https://xjustice.github.io/world-energy-map/)

## Project Overview

This project aims to provide a comprehensive and engaging look at how electricity is consumed worldwide. By analyzing per capita usage, we can better understand the energy disparities, developmental trends, and efficiency shifts across different nations and regions.

The application is built using lightweight, vanilla web technologies (HTML, CSS, JavaScript) alongside powerful mapping and data visualization libraries.

## Key Features

*   **Interactive Global Map:** A responsive, dark-themed choropleth map that visually categorizes countries based on their electricity usage.
*   **🏆 Global Leaderboard:** A floating panel (top-left) that displays the Top 10 High and Top 10 Low electricity consumers in the world. Clicking on any country in the leaderboard instantly zooms the map to that location.
*   **📱🚗 Fun Energy Converter:** Hovering over a country doesn't just show raw numbers (kWh). It automatically converts the usage into relatable real-world comparison:
    *   How many **iPhone charges** the energy equates to.
    *   How many **kilometers you could drive in a Tesla Model 3**.
*   **Optimized Data Pipeline:** The raw 40MB CSV data from Our World in Data is distilled via Python (`build_data.py`) into a lightning-fast 12KB `data.json` file, ensuring instantaneous page loads without browser stalling.
*   **Dynamic Year Label:** Automatically analyzes the dataset and displays the most recent year of data available.

## Built With

*   **[Leaflet.js](https://leafletjs.com/):** For rendering the interactive map interface and handling geographical layers.
*   **[D3.js](https://d3js.org/):** For fetching, parsing, and formatting the JSON data seamlessly.
*   **Vanilla JS/CSS:** For performance-driven logic and styling without heavy frameworks.
*   **Python:** For backend data preprocessing (`build_data.py`).

## Data Source

The data is meticulously curated and provided by **[Our World in Data (OWID)](https://ourworldindata.org/energy)**. It aggregates information from primary sources including Ember, the Energy Institute Statistical Review of World Energy, and Eurostat.

## Local Development

If you'd like to run this project locally or update the data:

1.  Clone the repository:
    ```bash
    git clone https://github.com/xjustice/world-energy-map.git
    cd world-energy-map
    ```
2.  (Optional) Run the data builder script to fetch the latest OWID CSV and generate a fresh `data.json`:
    ```bash
    python3 build_data.py
    ```
3.  Open `index.html` in your browser. (Note: For some local environments, you may need to use a simple local server like `npx http-server` to avoid CORS issues when fetching JSON files).

## License & Attribution

*   Code visualization by xjustice.
*   Map data © [OpenStreetMap](https://www.openstreetmap.org/copyright) contributors, © [CARTO](https://carto.com/attributions).
*   Energy data by [Our World in Data](https://ourworldindata.org/).
