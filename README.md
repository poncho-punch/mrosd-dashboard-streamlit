# Violations Dashboard

A web-based interactive dashboard for visualizing violation data, built with Streamlit and hosted on Streamlit Cloud. The dashboard allows users to filter and explore violations by location, bicycle type, badge number, date range, and aggregation period, displaying results as a stacked bar chart.

Live app: [Violations Dashboard](https://mrosd-dashboard-app-fhabbkt6qyyx5987f7srjp.streamlit.app)

## Overview

This dashboard connects to a Google Sheet to fetch violation data, including details like date, location, violation type, badge number, and contact type (e.g., Citation, Verbal Warning, Written Warning). Users can apply filters to analyze trends and patterns, such as violations by specific badge numbers or time periods.

**Features**:
- **Interactive Filters**:
  - **Location**: Multi-select to filter by location groups (e.g., EL CORTE DE MADERA) or all locations.
  - **Bicycle Type**: Dropdown to select All, Regular, or E-Bike.
  - **Badge Number**: Multi-select to filter by badge numbers (e.g., 123, 456) or all.
  - **Date Range**: Select start and end dates for the analysis period.
  - **Aggregation**: Choose daily, weekly, or monthly time periods.
- **Visualization**: Stacked bar chart showing violations by contact type over time.
- **Dynamic Updates**: Add new data to the Google Sheet, and the dashboard reflects changes on refresh or update.
- **Website-Like Interface**: Accessible via a URL, no code execution required.

## Usage

1. **Access the Dashboard**:
   - Open [https://mrosd-dashboard-app-fhabbkt6qyyx5987f7srjp.streamlit.app](https://mrosd-dashboard-app-fhabbkt6qyyx5987f7srjp.streamlit.app) in a web browser.
   
2. **Apply Filters**:
   - Use the sidebar to select:
     - **Location**: Choose one or more locations (default: All).
     - **Bicycle Type**: Select All, Regular, or E-Bike (default: All).
     - **Badge Number**: Choose one or more badge numbers (default: All).
     - **Start Date** and **End Date**: Pick a date range (defaults to full data range).
     - **Aggregation**: Select Daily, Weekly, or Monthly (default: Monthly).
   
3. **Update the Chart**:
   - Click the **Update Chart** button to refresh the stacked bar chart based on your filters.
   - The chart shows violations by contact type, stacked over the selected time periods.

4. **Add New Data**:
   - Update the Google Sheet with new violation records (ensure columns match: Date and Time, Location, Violation Type, Badge Number, Contact Type).
   - Refresh the dashboard or click Update Chart to see the latest data.

## Development

For developers looking to maintain or enhance the dashboard:

### Prerequisites
- **Google Sheet**: The data source, accessible via a service account (credentials stored in Streamlit Cloud secrets).
- **Streamlit Cloud**: Hosts the app, linked to this GitHub repository.
- **Python Libraries**: Listed in `requirements.txt` (`streamlit`, `gspread`, `oauth2client`, `pandas`, `matplotlib`).

### Project Structure
- `app.py`: Main Streamlit app code, defining the dashboard logic and UI.
- `requirements.txt`: Python dependencies for Streamlit Cloud.
- `README.md`: This file.

### Enhancing the App
1. **Develop**:
   - Modify `app.py` (e.g., in a local editor or Google Colab).
   - Update the app code (e.g., add new filters, change chart styling).
   - Test logic locally or in a development environment.
   
2. **Commit Changes**:
   - Upload the updated `app.py` to this GitHub repository.
   - Ensure `requirements.txt` includes any new dependencies.
   - Commit with a descriptive message (e.g., "Add badge number filter").

3. **Deploy**:
   - Streamlit Cloud auto-redeploys on GitHub commits.
   - Verify the updated app at the live URL.
   - Check Streamlit Cloud logs if deployment fails.

### Example Enhancement
To add a new filter:
- Modify `app.py` to include a new `st.sidebar` widget (e.g., `st.multiselect` for another column).
- Update the `plot_chart` function to filter `df` based on the new selection.
- Test, commit, and redeploy.

## Resources
- **Live App**: [https://mrosd-dashboard-app-fhabbkt6qyyx5987f7srjp.streamlit.app](https://mrosd-dashboard-app-fhabbkt6qyyx5987f7srjp.streamlit.app)
- **GitHub Repository**: [github.com/poncho-punch/violations-dashboard-streamlit](https://github.com/poncho-punch/violations-dashboard-streamlit)
- **Google Sheet**: Contact the repository owner for access details (data source not publicly shared).
- **Streamlit Documentation**: [docs.streamlit.io](https://docs.streamlit.io) for app development.
- **Google Sheets API**: [developers.google.com/sheets/api](https://developers.google.com/sheets/api) for data integration.

## Contact
For issues or feature requests, open a GitHub issue or contact the repository owner.
