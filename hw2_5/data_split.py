import os
import shutil

datadir = 'PetImages/test'
full_path = 'PetImages'
f = os.listdir(datadir)

count = 0
for fname in f :
    newname = 'test' + str(count) + '.jpg'
    os.rename(os.path.join(datadir , fname) , os.path.join(datadir , newname))
    print(fname , ' ----> ' , newname)
    #if count < 10000 :
        #shutil.move(os.path.join(datadir , newname) ,full_path + "./train/Dog")
    #else :
        #shutil.move(os.path.join(datadir , newname) ,full_path + "./test/Dog")
    count += 1    
"""datadir = 'PetImages/Trash/Cat'
full_path = 'PetImages/Trash'
f = os.listdir(datadir)

count = 0
for fname in f :
    newname = str(count) + '.jpg'
    os.rename(os.path.join(datadir , fname) , os.path.join(datadir , newname))
    print(fname , ' ----> ' , newname)
    if count < 7 :
        shutil.move(os.path.join(datadir , newname) ,full_path + "./train/Cat")
    else :
        shutil.move(os.path.join(datadir , newname) ,full_path + "./test/Cat")
    count += 1"""