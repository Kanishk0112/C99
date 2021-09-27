import os 
import shutil
source= input("Enter Source Folder Name")
dest=input("Enter Destination Folder Name")
source=source+"/"
dest=dest+"/"
listoffiles=os.listdir(source)
for file in listoffiles:
    shutil.copy((source+file), dest)
    