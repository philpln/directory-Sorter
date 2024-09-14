import streamlit as st
from sorter import *

if 'filesToSort' not in st.session_state:
        st.session_state['filesToSort'] = 0

bar = st.progress(0)
def executeFileOrdering():
    for file in os.listdir(os.getcwd()):
        if not os.path.isdir(file):
            filename, fileExtension = os.path.splitext(file)
            # print(f"{filename} is {filename in dontTouch} in {dontTouch}")
            if filename in dontTouch:
                continue
            print(fileExtension)
            if fileExtension in extensionsAndFolders.keys():
                print("trying to move "+ os.path.join(os.getcwd(), file))
                shutil.move(os.path.join(os.getcwd(),file), os.path.join(os.getcwd(),getFolder(fileExtension)))
                st.session_state.filesToSort = st.session_state.filesToSort -1
                bar.progress(int(100*(1-(st.session_state.filesToSort/filesBeginning))))
                time.sleep(0.2)

st.header('Filesorter')
st.session_state.filesToSort = getNumberOfFilesToSort()
filesBeginning = getNumberOfFilesToSort()

st.write("Files found that need to be sorted:")
st.write(st.session_state.filesToSort)
sortButton = st.button("Start Sorting")
if sortButton:
    executeFileOrdering()
