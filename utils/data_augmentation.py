import numpy as np
import os 
from glob import glob
from skimage.io import imread, imsave
from skimage.transform import resize
from keras.preprocessing.image import ImageDataGenerator

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--path', type=str, default='./banque_tableaux_par_artiste_resized/')
parser.add_argument('--artist_name', type=str)
parser.add_argument('--number_generated', type=int)

args = parser.parse_args()


def augment_artist_data(path='./banque_tableaux_par_artiste_resized/', artist_name='kirchner', size=(256, 256)):
    '''
    Function to load artist data into numpy arrays.
    '''
    files = glob(os.path.join(path, artist_name+'_resized', "*.jpg"))
    n_samples = len(files)
    X = np.zeros(shape=(n_samples, size[0], size[1], 3), dtype="float32")
    for i, f in enumerate(files):
        X[i] = imread(f)
    return X

def augmented_images(X, datadir, artist='kirchner', n=10, batch_size=10):
    """
    X - input array of images
    artist - artist
    n - number of data augmented images we want to write to disk
    datadir - where we want to write these images
    batch_size - control it so n//batch_size
    """
    n_samples = X.shape[0]
    image_gen = ImageDataGenerator(width_shift_range=0.2,
                                   height_shift_range=0.2,
                                   shear_range=0.01,
                                   zoom_range=[0.9, 1.25],
                                   horizontal_flip=True,
                                   vertical_flip=False,
                                   fill_mode='reflect')
    image_flow = image_gen.flow(X,
                                save_to_dir=datadir,
                                save_prefix="augmented_"+artist,
                                save_format="jpeg",
                                batch_size=batch_size)
    count = 0
    while count < n:
        X_temp = next(image_flow)
        count += batch_size
    print('Finished writing your augmented images to disk')



if __name__ == '__main__':
    X = augment_artist_data(artist_name=args.artist_name)
    augmented_images(X, args.path+args.artist_name+'_resized',
                     artist=args.artist_name,
                     n=args.number_generated)

