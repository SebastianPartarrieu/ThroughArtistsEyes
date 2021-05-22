### Script to iterate through all images in a directory and resize all of them

import argparse
import os
from PIL import Image

# Parser
parser = argparse.ArgumentParser(description='Resize all images in a given directory')
parser.add_argument('--dataroot', type=str, default='', help="The directory whose images you want resized, relative path")
parser.add_argument('--datadir', type=str, default='', help='Name for directory you want to place images in')
parser.add_argument('--size', type=int, default=256)
args = parser.parse_args()

# Get values
datapath = args.dataroot
datadir = args.datadir
image_size = args.size # this resizing method is used only for artist pics, we want 256x256 pixels

# Get all values in the given directory
all_files = os.listdir(datapath)

# Create directory
os.mkdir(datadir)

# Iterate 
for i, given_file_path in enumerate(all_files):
    if os.path.isfile(datapath+given_file_path):
        try:
            im = Image.open(datapath + given_file_path)
            im_resized = im.resize((image_size, image_size))
            im_resized.save(datadir + '/' + f'{datadir}_resized_{i}.jpg')
        except Exception as e:
            print('Probably not an image')
