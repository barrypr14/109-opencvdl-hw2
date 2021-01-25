from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image
import numpy as np
import random
import cv2
np.set_printoptions(precision=4 , suppress= True)
net = load_model('PetImages/train/model-resnet50-final_ver2.h5')
#net.summary()
name = random.randint(0,1)
if name == 0 :
    tt = 'c'
    rd = random.randint(10000,12487)
else :
    tt = 'test'
    rd = random.randint(0,2488)

file_path = 'PetImages/test/' + str(tt) + str(rd) + '.jpg'
img= image.load_img(file_path , target_size=(128,128))
img_tensor = image.img_to_array(img)
img_tensor_exp = np.expand_dims(img_tensor , axis = 0)
#img_tensor_exp/=255


#print(img_tensor_exp.shape)
#print(img_tensor.shape)
prediction = net.predict(img_tensor_exp)
img_tensor_exp/=255
print(prediction)

if prediction[0][0] > prediction[0][1] :
    print('Cat')
    cv2.imshow('Class:Cat' , img_tensor)
    cv2.waitKey(0)
    cv2.destroyWindow('Class=Cat')
else :
    print('Dog')
    cv2.imshow('Class:Dog' , img_tensor)
    cv2.waitKey(0)
    cv2.destroyWindow('Class=Dog')
