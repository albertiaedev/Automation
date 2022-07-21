import os, sys, shutil, time
from random import randint

#This is the folder to store the downloads
download = "/home/jahr/Descargas"

#The download folder can be changed
while True:
    if os.path.exists('docs') == True:
        pass
    else:
        os.mkdir('docs')
        continue

    if os.path.exists('vids') == True:
        pass
    else:
        os.mkdir('vids')
        continue

    if os.path.exists('img') == True:
        pass
    else:
        os.mkdir('img')
        continue

docs = "/home/jahr/Python/Automation/docs"
ext_docs = ['.doc','.docx','.xlm','.pptx','.pdf','.epub','.txt']

vids = "/home/jahr/Python/Automation/vids"
ext_vids = ['.wmv','.mp4']

img = "/home/jahr/Python/Automation/img"
ext_img = ['.png','.jpg','.jpeg','.gif','.ico']

def redirect(archive, ext):
    for i in ext_docs:
        if ext == i:
            shutil.move(download+archive,docs)
    for i in ext_vids:
        if ext == i:
            shutil.move(download+archive,vids)
    for i in ext_img:
        if ext == i:
            shutil.move(download+archive,img)
