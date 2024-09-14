import streamlit as st
from sorter import *
import random
import plotly.graph_objects as go
from dirSizes import *
from pprint import pprint

if 'filesToSort' not in st.session_state:
        st.session_state['filesToSort'] = 0
if 'filesBeginning' not in st.session_state:
        st.session_state['filesBeginnning'] = 0

# Function to execute file ordering
def executeFileOrdering():
    for file in os.listdir(os.getcwd()):
        if not os.path.isdir(file):
            filename, fileExtension = os.path.splitext(file)
            
            # Skip files in dontTouch list
            if filename in dontTouch:
                continue

            # Handle file extensions and move files
            if fileExtension in extensionsAndFolders:
                destination_folder = getFolder(fileExtension)
                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)
                print("Moving " + os.path.join(os.getcwd(), file))
                shutil.move(os.path.join(os.getcwd(), file), os.path.join(destination_folder, file))
                st.session_state.filesToSort -= 1
                displayFiles.write(f"Files found that need to be sorted: {st.session_state.filesToSort}")
                bar.progress(int(100 * (1 - (st.session_state.filesToSort / st.session_state.filesBeginning))))
                time.sleep(0.2)
            else:
                # Handle files without extensions or unknown types
                st.session_state.filesToSort -= 1
                displayFiles.write(f"Files found that need to be sorted: {st.session_state.filesToSort}")
                bar.progress(int(100 * (1 - (st.session_state.filesToSort / st.session_state.filesBeginning))))

# Streamlit UI elements

st.header('Filesorter')
st.session_state.filesToSort = getNumberOfFilesToSort()
st.session_state.filesBeginning = st.session_state.filesToSort  # Corrected initialization

displayFiles = st.empty()
displayFiles.write(f"Files found that need to be sorted: {st.session_state.filesToSort}")
bar = st.progress(0)
sortButton = st.button("Start Sorting")
if sortButton:
    checkIfAllFolders()
    executeFileOrdering()


import plotly.graph_objects as go
from dirSizes import directorySizes
def get_data():
    # Fetch fresh data
    directorySizesDict = directorySizes()
    
    # Initialize lists
    labels = []
    sizes = []
    colors = []

    # Populate lists
    for key, size in directorySizesDict.items():
        labels.append(key)
        sizes.append(size)
        # Generate a random color for each slice
        r = lambda: random.randint(0, 255)
        colors.append('#%02X%02X%02X' % (r(), r(), r()))

    return labels, sizes, colors

# Streamlit app
st.title('Directory Sizes Pie Chart')

# Get fresh data for the pie chart
labels, sizes, colors = get_data()

# # Debug outputs
# st.write("Labels:", labels)
# st.write("Sizes:", sizes)
# st.write("Colors:", colors)

# Create a pie chart
fig = go.Figure(data=[go.Pie(
    labels=labels, 
    values=sizes, 
    hole=0.3,
    textinfo='label+percent',
    marker=dict(colors=colors)
)])

# Set title for the chart
fig.update_layout(title_text='Directory Sizes Pie Chart')

# Display the pie chart in Streamlit
st.plotly_chart(fig)