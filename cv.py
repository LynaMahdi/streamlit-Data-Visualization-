import streamlit as st
import pydeck as pdk
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
from PIL import Image

profile_pic_path = "./ddbf063f77dce418a204acafc6406821.jpg"
NAME = "Lina MAHDI"
DESCRIPTION = """
Big data and machine learning student.
"""
EMAIL = "linamahdi001@gmail.com"

# Load profile picture
profile_pic = Image.open(profile_pic_path)

# Layout with two columns
col1, col2 = st.columns(2, gap="medium")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write("📫", EMAIL)
    st.write("👩‍💻 [Github](https://github.com/Lynamahdi)")
    st.write("☎️", "0777777777")
    st.write("📍", "Paris, France")

st.write('\n')

# Skills section
st.subheader("Skills")
st.write(
    """
- 📊 Data science: Python (Scikit-learn, Keras, Pandas, R, TensorFlow), SQL
- 👩‍💻 Web Development: HTML, CSS, JavaScript, PHP, ReactJS, Django
- 🗄️ Databases: SQL, NoSQL, MySQL, PostgreSQL, MongoDB
"""
)

st.write('\n')

# Experiences and Projects section
st.subheader("Experiences and Projects")
st.write("---")
st.markdown("**Data Science Internship at SFR**")
st.markdown("""
- Participated in the integration and optimization of **Machine Learning** models to improve forecasting and decision support tools.
""")
st.markdown("**Technologies:** GCP, Python, Vertex AI, BigQueryML, Power BI")

st.write("---")
st.markdown("**Business Intelligence Development Internship**")
st.markdown("""
- Implemented a **Business Intelligence** solution using **Apache Superset**.
""")
st.markdown("**Technologies:** Apache Superset, ReactJS, Django")

st.write("---")
st.markdown("**Treasure Map Exploration Project**")
st.markdown("""
- Developed an application to simulate explorations on a treasure map.
""")
st.markdown("**Technologies:** Java multithreading, Java Swing")
st.write("---")
