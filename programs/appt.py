import streamlit as st
import random
import plotly.graph_objects as go
from dirSizes import directorySizes

# Sample data
labels = []
sizes = []
colors = []

directorySizesDict = directorySizes()

# Populate labels, sizes, and colors
for key in directorySizesDict.keys():
    labels.append(key[2:])
    sizes.append(directorySizesDict[key])
    # Generate random colors for the pie chart
    r = lambda: random.randint(0, 255)
    colors.append('#%02X%02X%02X' % (r(), r(), r()))

# Create a pie chart
fig = go.Figure(data=[go.Pie(
    labels=labels, 
    values=sizes, 
    hole=0.3,
    textinfo='label+percent',  # Show both label and percentage
    marker=dict(colors=colors)  # Apply colors
)])

# Set title for the chart
fig.update_layout(title_text='Directory Sizes Pie Chart')

# Display the pie chart in Streamlit
st.plotly_chart(fig)

