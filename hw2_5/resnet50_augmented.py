import os
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Flatten, Dense, Dropout
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.optimizers import Adam
import datetime
import matplotlib.pyplot as plt
ImageDataGenerator = tf.keras.preprocessing.image.ImageDataGenerator

datasetdir = "PetImages/small_train"
os.chdir(datasetdir)  ##開啟檔案位置

imgdatagen = ImageDataGenerator(validation_split = 0.2)

batch_size = 4

height, width = (128,128)

train_dataset = imgdatagen.flow_from_directory(os.getcwd(),target_size = (height, width), classes = ('Cat','Dog'),batch_size = batch_size,subset = 'training')

val_dataset = imgdatagen.flow_from_directory(os.getcwd(),target_size = (height, width), classes = ('Cat','Dog'),batch_size = batch_size,subset = 'validation')


resnet = ResNet50(include_top=False , weights='imagenet', input_tensor=None, pooling = 'avg' ,input_shape=(height,width,3) )

x = resnet.output
x = Flatten()(x)

# 增加 DropOut layer
x = Dropout(0.5)(x)

# 增加 Dense layer，以 softmax 產生個類別的機率值
output_layer = Dense(2, activation='softmax', name='softmax')(x)

# 設定凍結與要進行訓練的網路層
net_final = Model(inputs=resnet.input, outputs=output_layer)
for layer in net_final.layers[:2]:
    layer.trainable = False
for layer in net_final.layers[2:]:
    layer.trainable = True

# 使用 Adam optimizer，以較低的 learning rate 進行 fine-tuning
net_final.compile(optimizer=Adam(lr=1e-5),
                  loss='categorical_crossentropy', metrics=['accuracy'])


# 輸出整個網路結構
print(net_final.summary())
logdir = os.path.join("hw2_aug_logs", datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
tensorboard_callback = tf.keras.callbacks.TensorBoard(logdir, histogram_freq=0 ,write_graph = False,
                                                        update_freq = batch_size)
# 訓練模型
net50 = net_final.fit_generator(train_dataset ,
                                steps_per_epoch = train_dataset.samples // batch_size ,
                                validation_data = val_dataset , 
                                validation_steps = val_dataset.samples // batch_size,
                                epochs = 5 ,
                                callbacks = [tensorboard_callback])

# 儲存訓練好的模型
net_final.save('model-resnet50-final_ver2_aug.h5')