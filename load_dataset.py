import glob, os
import numpy as np
from skimage.io import imread
from skimage.transform import resize
from tqdm import tqdm


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