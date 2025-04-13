
import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Streamlit page config
st.set_page_config(page_title="Violations Dashboard", layout="wide")
st.title("Violations Dashboard")

# Authenticate with Google Sheets
try:
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds_dict = st.secrets["gcp_service_account"]
    creds = Credentials.from_service_account_info(creds_dict, scopes=scope)
    client = gspread.authorize(creds)
    sheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1sJOrKkf6RBkkGhL3YBJXX4XuEJuFO7qn_2EF3zQME7Y/edit?usp=sharing")
    worksheet = sheet.get_worksheet(0)
    data = worksheet.get_all_records()
    df = pd.DataFrame(data)
except Exception as e:
    st.error(f"Error loading data: {e}")
    st.stop()

# Preprocess data
try:
    df['Date and Time'] = pd.to_datetime(df['Date and Time'], errors='coerce')
    df['Location Group'] = df['Location'].str.split(' : ').str[0].fillna('Unknown')
    df['Bicycle Type'] = df['Violation Type'].apply(
        lambda x: 'E-Bike' if isinstance(x, str) and ('ELECTRIC BICYCLES' in x.upper() or 'EBIKE' in x.upper()) else 'Regular'
    )
    df['Contact Type'] = df['Contact Type'].str.strip().str.title()
except Exception as e:
    st.error(f"Error preprocessing data: {e}")
    st.stop()

# Widgets
st.sidebar.header("Filter Options")
locations = st.sidebar.multiselect(
    "Location", ['All'] + sorted(df['Location Group'].unique().tolist()), default=['All']
)
bicycle_type = st.sidebar.selectbox("Bicycle Type", ['All', 'Regular', 'E-Bike'], index=0)
start_date = st.sidebar.date_input("Start Date", df['Date and Time'].min().date())
end_date = st.sidebar.date_input("End Date", df['Date and Time'].max().date())
aggregation = st.sidebar.selectbox("Aggregation", ['Daily', 'Weekly', 'Monthly'], index=2)
update_button = st.sidebar.button("Update Chart", type="primary")

# Plotting function
def plot_chart(locations, bicycle_type, start_date, end_date, aggregation):
    filtered_df = df.copy()
    if 'All' not in locations:
        filtered_df = filtered_df[filtered_df['Location Group'].isin(locations)]
    if bicycle_type != 'All':
        filtered_df = filtered_df[filtered_df['Bicycle Type'] == bicycle_type]
    if start_date > end_date:
        start_date, end_date = end_date, start_date
    filtered_df = filtered_df[
        (filtered_df['Date and Time'].dt.date >= start_date) &
        (filtered_df['Date and Time'].dt.date <= end_date)
    ]

    if aggregation == 'Daily':
        filtered_df['Time Period'] = filtered_df['Date and Time'].dt.date
    elif aggregation == 'Weekly':
        filtered_df['Time Period'] = filtered_df['Date and Time'].dt.to_period('W').apply(lambda r: r.start_time.date())
    else:  # Monthly
        filtered_df['Time Period'] = filtered_df['Date and Time'].dt.to_period('M').apply(lambda r: r.start_time.date())

    grouped_df = filtered_df.groupby(['Time Period', 'Contact Type']).size().unstack(fill_value=0).reset_index()
    
    if grouped_df.empty or len(grouped_df) == 0 or all(grouped_df.iloc[:, 1:].sum() == 0):
        st.warning("No data to display for the selected filters.")
        return

    fig, ax = plt.subplots(figsize=(12, 6))
    contact_types = [col for col in grouped_df.columns if col != 'Time Period']
    bottom = None
    for contact in contact_types:
        ax.bar(grouped_df['Time Period'], grouped_df[contact], label=contact, bottom=bottom)
        bottom = grouped_df[contact] if bottom is None else bottom + grouped_df[contact]
    ax.set_title('Violations by Contact Type')
    ax.set_xlabel('Date')
    ax.set_ylabel('Number of Violations')
    ax.tick_params(axis='x', rotation=45)
    ax.legend()
    plt.tight_layout()
    st.pyplot(fig)

# Display chart
if update_button:
    plot_chart(locations, bicycle_type, start_date, end_date, aggregation)
else:
    st.write("Click 'Update Chart' to display the dashboard.")
