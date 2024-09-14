import shutil
import os
import time

extensionsAndFolders = {
    '.txt':'textfiles',
    '.py':'programs',
    '.png':'pngs',
    '.jpeg':'jpegs',
    '.gif':'gifs',
    '.psd':'photoshop',
    '.mp4':'videos',
    '.pdf':'pdfs',
    '.ipynb':'programs',
    '.mov':'videos'
}

def checkIfAllFolders():
    for foldername in extensionsAndFolders.values():
        if not os.path.isdir(foldername):
            os.mkdir(foldername)


dontTouch = ["app","sorter","dirSizes",'.DS_Store']
def getFolder(extension):
    return extensionsAndFolders[extension]

def getNumberOfFilesToSort():
    filesandFolders = os.listdir(os.getcwd())
    onlyFiles = [x for x in filesandFolders if not os.path.isdir(x)]
    # onlyFiles = [x for x in onlyFiles if x in extensionsAndFolders.keys()]
    print(onlyFiles)
    numberOfFiles = len(onlyFiles) -(len(dontTouch))
    return numberOfFiles

#print(os.listdir(os.getcwd()))
def executeFileOrderingStandalone():
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
