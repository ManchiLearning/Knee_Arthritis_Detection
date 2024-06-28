import glob, os
import numpy as np
from skimage.io import imread
from skimage.transform import resize
from tqdm import tqdm
import tensorflow as tf
from tensorflow.keras.preprocessing import image_dataset_from_directory
import matplotlib.pyplot as plt

def load_dataset(dataset_path=os.path.join("data","raw")):
    imgs = []
    labels = []
    names = []
    i=0
    for directory in glob.glob(os.path.join(dataset_path,"*")):
        print("Loading", directory)
        for file in tqdm(glob.glob(os.path.join(directory, '*.png'))):

            img = imread(file,as_gray=True)
            imgs.append(resize(img, (162,300), anti_aliasing=True))
            labels.append(i)
            names.append(os.path.split(directory)[1])
        i+=1
    return np.array(imgs), np.array(labels), names

def load_dataset_tensorflow(dataset_path=os.path.join("data","raw"),**kwargs):
    if not "subset" in kwargs:
        raise ValueError("Please provide a subset parameter (train, valid, both)")
    
    if kwargs["subset"] == "both" and not "validation_split" in kwargs:
        raise ValueError("Please provide a validation_split parameter")
    
    return image_dataset_from_directory(dataset_path,color_mode="grayscale",seed=42,label_mode="categorical",batch_size=32,**kwargs)

def plot_accuraccy_loss(history):
    data = history.history
    fig,ax = plt.subplots(1,2,figsize=(10,5))
    ax[0].plot(data['accuracy'],label='accuracy')
    ax[0].plot(data['val_accuracy'],label='val_accuracy')
    ax[0].set_xlabel('Epoch')
    ax[0].set_ylabel('Accuracy')
    ax[0].set_title("Accuracy vs epochs")
    ax[0].legend()
    ax[1].plot(data['loss'],label='loss')
    ax[1].plot(data['val_loss'],label='val_loss')
    ax[1].set_xlabel('Epoch')
    ax[1].set_title("Loss vs epochs")
    ax[1].set_ylabel('Loss')
    ax[1].legend()
    plt.show()