import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import folium
from streamlit_folium import folium_static
from statsmodels.tsa.arima.model import ARIMA

# Load and cache data
@st.cache_data
def load_data(crime_file, state_file):
    try:
        crime_data = pd.read_csv(crime_file)
        state_lat_long = pd.read_csv(state_file)
        merged_data = pd.merge(
            crime_data.dropna(subset=['state_abbr', 'state_name']),
            state_lat_long.dropna(subset=['City']),
            left_on='state_abbr',
            right_on='State',
            how='inner'
        )
        return merged_data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

# Plot time-series trends
def plot_trends(data):
    violent_crime_ts = data.set_index('year')['violent_crime']
    arima_model = ARIMA(violent_crime_ts, order=(2, 1, 2))
    arima_result = arima_model.fit()
    forecast = arima_result.get_forecast(steps=10)
    forecast_index = range(violent_crime_ts.index[-1] + 1, violent_crime_ts.index[-1] + 11)

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(violent_crime_ts.index, violent_crime_ts, label='Historical Violent Crimes', color='blue')
    ax.plot(forecast_index, forecast.predicted_mean, label='Forecasted Violent Crimes', color='red', linestyle='--')
    ax.fill_between(forecast_index, forecast.conf_int().iloc[:, 0], forecast.conf_int().iloc[:, 1],
                    color='pink', alpha=0.3, label='Confidence Interval')
    ax.set_title("Violent Crime Trends Over Time", fontsize=16)
    ax.set_xlabel("Year", fontsize=12)
    ax.set_ylabel("Number of Crimes", fontsize=12)
    ax.legend()
    st.pyplot(fig)

    # Dynamic explanation
    st.subheader("Explanation:")
    last_year = violent_crime_ts.index[-1]
    recent_crime = violent_crime_ts.iloc[-1]
    forecasted_crime = int(forecast.predicted_mean.iloc[0])
    st.write(f"""
        Violent crimes in the most recent year ({last_year}) were **{recent_crime}**. 
        Based on the forecast, violent crimes are expected to increase to approximately **{forecasted_crime}** 
        in the following year, with a confidence interval indicated in pink.
    """)

# Create interactive map
def create_hotspot_map(data):
    crime_map = folium.Map(location=[37.0902, -95.7129], zoom_start=4)
    for _, row in data.iterrows():
        folium.CircleMarker(
            location=[row['Latitude'], row['Longitude']],
            radius=row['violent_crime'] / 100000,  # Scale the marker size
            color='red',
            fill=True,
            fill_color='red',
            fill_opacity=0.6,
            popup=(f"<b>State:</b> {row['state_name']}<br><b>Violent Crime:</b> {row['violent_crime']}")
        ).add_to(crime_map)
    folium_static(crime_map)

    # Dynamic explanation
    st.subheader("Explanation:")
    highest_crime_state = data.loc[data['violent_crime'].idxmax()]
    st.write(f"""
        The state with the highest number of violent crimes is **{highest_crime_state['state_name']}**, 
        reporting a total of **{highest_crime_state['violent_crime']} violent crimes**. The map above 
        highlights the intensity of violent crimes across the U.S., with larger red circles indicating higher crime rates.
    """)

# Plot bar chart for crime types
def plot_crime_types(data):
    crime_type_data = data[['violent_crime', 'homicide', 'rape_legacy', 'robbery', 'property_crime']].sum()
    crime_type_df = pd.DataFrame({
        'Crime Type': crime_type_data.index,
        'Total Crimes': crime_type_data.values
    })
    fig = px.bar(
        crime_type_df,
        x='Crime Type',
        y='Total Crimes',
        title="Total Crimes by Type Nationwide",
        color='Total Crimes',
        text_auto=True
    )
    st.plotly_chart(fig)

    # Dynamic explanation
    st.subheader("Explanation:")
    most_common_crime = crime_type_df.iloc[crime_type_df['Total Crimes'].idxmax()]
    st.write(f"""
        Among all crime types, **{most_common_crime['Crime Type']}** is the most common, with a total of 
        **{int(most_common_crime['Total Crimes'])} incidents** nationwide. The bar chart provides a breakdown 
        of various crime types, helping to understand the scale of different offenses.
    """)

# Streamlit app
st.title("Crime Data Analysis and Prediction Dashboard")
st.sidebar.title("Upload Data")

# Upload files
crime_file = st.sidebar.file_uploader("Upload Crime Data CSV", type=["csv"])
state_file = st.sidebar.file_uploader("Upload State Latitude/Longitude CSV", type=["csv"])

if crime_file and state_file:
    merged_data = load_data(crime_file, state_file)

    if merged_data is not None:
        st.sidebar.success("Data loaded successfully!")
        st.sidebar.title("Navigation")
        options = st.sidebar.radio("Select a Section:", ["Home", "Crime Trends", "Crime Hotspots", "Crime Type Comparison"])

        if options == "Home":
            st.header("Overview")
            st.write("""
                Welcome to the Crime Data Analysis Dashboard! Explore historical trends, visualize crime hotspots, 
                and analyze crime types interactively. Upload your data to get started.
            """)

        elif options == "Crime Trends":
            st.header("Crime Trends Over Time")
            plot_trends(merged_data.groupby('year').agg({'violent_crime': 'sum'}).reset_index())

        elif options == "Crime Hotspots":
            st.header("Crime Hotspots Across the United States")
            create_hotspot_map(merged_data.groupby(['state_name', 'Latitude', 'Longitude'])
                               .agg({'violent_crime': 'sum'}).reset_index())

        elif options == "Crime Type Comparison":
            st.header("Comparison of Crime Types")
            plot_crime_types(merged_data)

else:
    st.warning("Please upload both crime data and state latitude/longitude CSV files to proceed.")

st.sidebar.info("Data Source: FBI Crime Data Explorer")
