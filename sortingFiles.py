import os
import shutil

unknown="Unknown/"
doc="Documents/"
zip="Compressed/"
exe="Executives/"
photo="Images/"
vid="Videos/"
music="Music/"
dirx=""

docf=(".doc","docx",".elsx",".ppt",".pptx",".xls",".db",".txt",".pdf")
zipf=(".tar",".rar",".zip",".xz")
exef=(".exe",".deb",".rep",".iso",".appimage")
photof=(".png",".jpg","jpeg","gif")
vidf=(".mp4",".3gp",".mov",".avi",'.flv',".mkv")
musicf=(".mp3",".wav",".aac")

list_of_items=[doc,zip,exe,photo,vid,music,unknown]


dir= input("Please give the download path(e.g. /home/linux/Downloads/): ")

while True:
    if not dir.endswith("/"):
        dir=dir+"/"
    if not os.path.exists(dir):
        print("The following path doesn't exsists...")
        break
    else:
        print("Path found! Making changes please wait...\n")
#MAKES THE DIRECTORIES IF NOT PRESENT IN THE GIVEN PATH
    for item in list_of_items:
        dirx= dir+item
        if not os.path.exists(dirx):
            os.mkdir(dirx)
#GET THE FILES AND PLACE THEM IN ORDER
    for file in os.listdir(dir):
        filex=dir+file
        fileExt=dir+file.lower()

        if not os.path.isdir(filex):
            print("Moving ",filex)
            if fileExt.endswith(docf):
                dirx=dir+doc+file
                
            elif fileExt.endswith(zipf):
                dirx=dir+zip+file
                
            elif fileExt.endswith(vidf):
                dirx=dir+vid+file
                
            elif fileExt.endswith(musicf):
                dirx=dir+music+file
                
            elif fileExt.endswith(exef):
                dirx=dir+exe+file
                
            elif fileExt.endswith(photof):
                dirx=dir+photo+file
                
            else:
                dirx=dir+unknown+file
            if not os.path.exists(dirx):
                shutil.move(filex,dirx)
            else:
                print("File already exsits on the destination..\nRenaming file with (copy) and keeping both...")
                shutil.move(filex,dirx+"(copy)")
    break
