import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Title and Introduction
st.title("🏋️‍♂️ Gym Exercises  Visualizations")
st.write("""
## About the Dataset
This dataset analyzes gym exercises to help you stay fit and healthy. It provides insights into exercise types, body parts targeted, and more.
         

### 🔍  Dataset Overview
The dataset includes various exercises, their types, body parts targeted, equipment, and difficulty levels.
""")

# Load the CSV file
@st.cache_data
def load_data(filepath):
    data = pd.read_csv(filepath)
    return data

gym_data = load_data('megaGymDataset.csv')

st.write(gym_data.head())

# WordCloud for Body Parts
st.markdown("---")

st.subheader("Word Cloud of Body Parts Targeted by Exercises")

st.write("""
Let's see which body parts are highlighted by the exercises in our dataset! 

""")
text = gym_data["BodyPart"].unique()
wordcloud = WordCloud(max_words=1000000, background_color="black").generate(str(text))
plt.figure(figsize=(13, 13))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
st.pyplot(plt)


# Pie Charts for Body Parts by Exercise Type
st.markdown("---")
st.subheader("Distribution of Exercises by Body Part")
st.write("""
Now, let’s explore how different exercise types target various body parts! ✨
""")
exercise_types = gym_data['Type'].unique()

#calculer combien d lignes on aura besoin pour representer
num_exercise_types = len(exercise_types)
num_rows = (num_exercise_types + 1) // 2  # 2 chart / ligne

#  subplots
fig = make_subplots(rows=num_rows, cols=2, specs=[[{"type": "domain"}, {"type": "domain"}] for _ in range(num_rows)])

# create pie charts
for i, exercise_type in enumerate(exercise_types):
    body_part_data = gym_data[gym_data['Type'] == exercise_type]['BodyPart'].value_counts().reset_index()
    body_part_data.columns = ['BodyPart', 'Count']  
    
    # Add pie chart for each type
    fig.add_trace(go.Pie(values=body_part_data['Count'], 
                         labels=body_part_data['BodyPart'], 
                         title=f"Body Parts Distribution for {exercise_type}",
                         marker=dict(line=dict(color='#FFFFFF', width=2.5))),
                  row=i // 2 + 1, col=i % 2 + 1)


fig.update_layout(height=600 + (num_rows - 2) * 100, showlegend=True)
st.plotly_chart(fig)



# levels par type
st.markdown("---")
st.subheader("Distribution of Exercises by Type and Level")

st.write("""
Next, let’s take a look at how these exercises are spread across different difficulty levels! 🎯💪
""")
# subplots
fig_levels = make_subplots(rows=num_rows, cols=2, specs=[[{"type": "domain"}, {"type": "domain"}] for _ in range(num_rows)])

for i, exercise_type in enumerate(exercise_types):
    level_data = gym_data[gym_data['Type'] == exercise_type]['Level'].value_counts().reset_index()
    level_data.columns = ['Level', 'Count'] 
    
    # Add pie chart for each type
    fig_levels.add_trace(go.Pie(values=level_data['Count'], 
                                 labels=level_data['Level'], 
                                 title=f"Difficulty Levels for {exercise_type}",
                                 marker=dict(line=dict(color='#FFFFFF', width=2.5))),
                         row=i // 2 + 1, col=i % 2 + 1)

fig_levels.update_layout(height=600 + (num_rows - 2) * 100, showlegend=True)
st.plotly_chart(fig_levels)



# Bar Chart of Exercises by Body Part
st.markdown("---")
st.subheader("🔍 Exercises by Body Part")
st.write("""
Let's see what the most popular body parts are in terms of available exercises!
""")


body_part_counts = gym_data['BodyPart'].value_counts().reset_index()
body_part_counts.columns = ['BodyPart', 'Count']

fig2 = go.Figure(data=[go.Bar(x=body_part_counts['BodyPart'], y=body_part_counts['Count'], marker=dict(color='purple'))])
fig2.update_layout(title='Number of Exercises by Body Part',
                   xaxis_title='Body Part',
                   yaxis_title='Number of Exercises',
                   xaxis_tickangle=-45)
st.plotly_chart(fig2)



#  Pie Chart of Exercise Difficulty Levels
st.markdown("---")
st.subheader("Distribution of Exercise Difficulty Levels")

st.write("""
Let’s break down how exercises are distributed across various difficulty levels! 
""")

level_counts = gym_data['Level'].value_counts().reset_index()
level_counts.columns = ['Level', 'Count']

# pie chart for difficulty levels
fig3 = go.Figure(data=[go.Pie(values=level_counts['Count'], 
                                labels=level_counts['Level'], 
                                marker=dict(line=dict(color='#FFFFFF', width=2.5)))])
fig3.update_layout(title='Distribution of Exercise Difficulty Levels')
st.plotly_chart(fig3)



# Bar Chart of Equipment Used
st.markdown("---")
st.subheader("Equipment Used in Exercises")

st.write("""
Finally, let’s discover what types of equipment are commonly used in exercises! 
""")


equipment_counts = gym_data['Equipment'].value_counts().reset_index()
equipment_counts.columns = ['Equipment', 'Count']

fig4 = go.Figure(data=[go.Bar(x=equipment_counts['Equipment'], y=equipment_counts['Count'], marker=dict(color='pink'))])
fig4.update_layout(title='Equipment Used in Exercises',
                   xaxis_title='Equipment',
                   yaxis_title='Number of Exercises',
                   xaxis_tickangle=-45)
st.plotly_chart(fig4)


# Conclusion
st.markdown("---")
st.header("🚀 Conclusion")
st.write("""
Through this analysis, we have visualized key aspects of gym exercises, including targeted body parts, types, difficulty levels, and equipment used. 
Utilizing this data can aid individuals in crafting tailored workout routines to meet their fitness goals. 🏆💪
""")

# Footer
st.write("Analysis conducted by Lina MAHDI with ❤️ using Streamlit and Plotly.")
