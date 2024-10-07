import streamlit as st

cv_page = st.Page(
    page="./cv.py",  
    title="My Curriculum vitae",
    default=True,
)

uber_page = st.Page(
    page="./uber.py",
    title="Uber dataset",
    default=False,
)

gym_page = st.Page(
    page="./gym.py",
    title="Gym Exercises dataset",
    default=False,
)

pg = st.navigation(pages=[cv_page, uber_page,gym_page])

pg.run()
