import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Configuration
st.set_page_config(
    page_title="Uber Pickups Analysis - April 2014",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Title 
st.title("Uber Pickups in New York - April 2014")

st.header("Introduction")
st.write("""
The April 2014 Uber pickups dataset contains information about Uber trips in New York City, including the date and time of each trip, geographical coordinates (latitude and longitude) of the pickup locations, and the base identifier. We will analyze the data to explore temporal and geographical patterns in Uber usage to understand user behavior and service demand.
""")

# Loading and Preparing the Data
st.header("🔍 Data Loading and Preparation")

@st.cache_data
def load_data(filepath):
    data = pd.read_csv(filepath)
    data['Date/Time'] = pd.to_datetime(data['Date/Time'])
    data['hour'] = data['Date/Time'].dt.hour
    data['weekday'] = data['Date/Time'].dt.weekday
    data['month'] = data['Date/Time'].dt.month
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    data['day_name'] = data['weekday'].apply(lambda x: days[x])
    return data

data = load_data("uber-raw-data-apr14.csv")
data = data.rename(columns={'Lat': 'latitude', 'Lon': 'longitude'})

st.subheader("Data Preview")
st.write(data.head())

# Sidebar filters for geographic analysis
st.sidebar.header("Geographical Filters")
hour_filter = st.sidebar.slider("Select Hour Range", 0, 23, (0, 23))
weekday_filter = st.sidebar.multiselect("Select Days of the Week", 
                                         ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'], 
                                         default=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])

# Filter data based on selections
filtered_data = data[
    (data['hour'] >= hour_filter[0]) & 
    (data['hour'] <= hour_filter[1]) & 
    (data['day_name'].isin(weekday_filter))
]



# Analysis by Hour, Day, and Time
st.header("Temporal Analysis of Pickups")

tab1, tab2, tab3 = st.tabs(["Hour of Day", "Day of Week", "Time Series Trends"])

with tab1:
    st.subheader("Number of Pickups by Hour of the Day")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(filtered_data['hour'], bins=24, kde=False, ax=ax, color='skyblue')
    ax.set_title("Uber Pickups by Hour - April 2014")
    ax.set_xlabel("Hour of the Day")
    ax.set_ylabel("Number of Pickups")
    st.pyplot(fig)

with tab2:
    st.subheader("Number of Pickups by Day of the Week")
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Count the pickups in the filtered data
    filtered_day_counts = filtered_data['day_name'].value_counts().reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
    
    sns.barplot(x=filtered_day_counts.index, y=filtered_day_counts.values, hue=filtered_day_counts.index, palette="viridis", ax=ax, legend=False)

    ax.set_title("Uber Pickups by Day of the Week - April 2014")
    ax.set_xlabel("Day of the Week")
    ax.set_ylabel("Number of Pickups")
    plt.xticks(rotation=45)
    st.pyplot(fig)

with tab3:
    st.subheader("Pickup Trends Over Time")
    time_series = filtered_data.set_index('Date/Time').resample('h').size().reset_index(name='Pickups')
    
    fig = px.line(time_series, x='Date/Time', y='Pickups', title='Hourly Uber Pickups Over April 2014')
    fig.update_layout(xaxis_title='Date/Time', yaxis_title='Number of Pickups')
    st.plotly_chart(fig, use_container_width=True)

# Geographic Analysis
st.header("Geographical Analysis of Pickups")

#  the map
st.subheader("Map of Uber Pickup Locations")
st.map(filtered_data[['latitude', 'longitude']])

# Analysis by Base
st.header("Analysis by Uber Base")

st.subheader("Number of Pickups per Base")
base_counts = filtered_data['Base'].value_counts().reset_index()  # Use filtered data
base_counts.columns = ['Base', 'Number of Pickups']

fig = px.bar(base_counts, x='Base', y='Number of Pickups', color='Number of Pickups',
             title='Number of Pickups by Uber Base',
             labels={'Base':'Uber Base', 'Number of Pickups':'Number of Pickups'})
st.plotly_chart(fig, use_container_width=True)

# KPI
st.header("Key Metrics")

col1, col2, col3 = st.columns(3)

with col1:
    total_pickups = filtered_data.shape[0]  
    st.metric("Total Pickups", f"{total_pickups:,}")

with col2:
    peak_hour = filtered_data['hour'].mode()[0] if not filtered_data.empty else 0  
    st.metric("Peak Hour", f"{peak_hour}:00")

with col3:
    peak_day = filtered_data['day_name'].mode()[0] if not filtered_data.empty else "N/A"  
    st.metric("Peak Day", peak_day)

# Conclusion and Insights
st.header("🚀 Conclusion")

st.write("""
**Key Findings:**

- **Peak Hours:** The highest number of Uber pickups occur during the late afternoon and early evening (approximately 17:00 to 20:00), aligning with typical rush hour periods.
- **Peak Days:** Weekdays, especially Thursday and Friday, show higher pickup counts compared to weekends, indicating a higher demand for transportation during the workweek or last day of the week.

Thank you for exploring this Uber pickups analysis with us!
""")

# Footer
st.markdown("""
---
*Analysis conducted by Lina MAHDI with ❤️ using Streamlit.*
""")
