import os

path = os.chdir("")# insert the path of the directory of your choice
                              # between quotes inside the os.chdir

for n,file in enumerate(os.listdir(path)):
    renamedFile = f"Image#{n+1}.png" # this script is meant to output .png files
    os.rename(file, renamedFile) # change the extension name if you want to output another format
