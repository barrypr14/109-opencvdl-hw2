import os
import matplotlib.pyplot as plt
import matplotlib.image as img
import glob
import re
import shutil
#from tensorflow import keras
#ImageDataGenerator = keras.preprocessing.image.ImageDataGenerator

datasetdir = "PetImages"

os.chdir(datasetdir)  ##開啟檔案位置

"""plt.subplot(1,2,1)
plt.imshow(img.imread('Cat/0.jpg'))
plt.subplot(1,2,2)
plt.imshow(img.imread('Dog/0.jpg'))
plt.show()""" #顯示照片樣貌
########################################### 查看來搞笑的訓練資料
for i in range(10) :
    im = img.imread('Cat/{}.jpg'.format(i))
    print('image shape ' , im.shape , ' maxium color level' , im.max())

bad_dog_ids = [5604, 6413, 8736, 8898, 9188, 9517, 10161, 10190, 10237, 10401, 10797, 11186]
bad_cat_ids = [2939, 3216, 4688, 4833, 5418, 6215, 7377, 8456, 8470, 11565, 12272]

def load_images(ids , classes) :
    images = []
    dirname = classes 
    for theid in ids :
        fname = '{dirname}/{theid}.jpg'.format(dirname=dirname,theid=theid)
        im = img.imread(fname)
        images.append(im)
    return images

#bad_dogs = load_images(bad_dog_ids , 'Dog')
#bad_cats = load_images(bad_cat_ids , 'Cat')

def plot_images(images, ids):
    ncols, nrows = 4, 3
    fig = plt.figure( figsize=(ncols*3, nrows*3), dpi=90)
    for i, (img, theid) in enumerate(zip(images,ids)):
      plt.subplot(nrows, ncols, i+1)
      plt.imshow(img)
      plt.title(str(theid))
      plt.axis('off')

#plot_images(bad_dogs, bad_dog_ids)
plt.show()
############################### 清除錯誤訓練資料集
pattern = re.compile(r'(\d+)\..*')

def trash_path(dirname) :
    return os.path.join('../Trash' , dirname)

def cleanup(ids , dirname) :
    #os.chdir(datasetdir)
    #save當前工作目錄
    oldpwd = os.getcwd()
    #進入dog/cat資料夾
    os.chdir(dirname)
    #創造垃圾桶
    trash = trash_path(dirname)
    #若之前存在過trash的資料夾，先刪除，重新建立
    if os.path.isdir(trash) :
        shutil.rmtree(trash)
    os.makedirs(trash,exist_ok=True)
    #loop dogs/cats file
    fnames = os.listdir()
    for fname in fnames :
        m = pattern.match(fname)
        if m : 
            the_id = int(m.group(1))
            if the_id in ids :
                print('moving to {} : {}'.format(trash,fname))
                shutil.move(fname,trash) #可是明明沒有print出來過怎麼不見了
    #going back to root directory
    os.chdir(oldpwd)

def restore(dirname) :
    os.chdir(datasetdir)
    oldpwd = os.getcwd()
    os.chdir(dirname)
    trash = trash.path(dirname)
    print(trash)
    for fname in os.listdir(trash) :
        fname = os.path.join(trash,fname)
        print('restoring' , fname)
        print(os.getcwd())
        shutil.move(fname , getcwd())
    os.chdir(oldpwd)

cleanup(bad_cat_ids , 'Cat') ##不小心刪了
cleanup(bad_dog_ids , 'Dog')
