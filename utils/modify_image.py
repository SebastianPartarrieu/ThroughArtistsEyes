#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 13:13:37 2020

@author: sophierossi
"""

import scipy.misc, numpy as np, os, sys
import imageio
from PIL import Image

def size_up(img_path, output_name, output_path, intermed_path):
    start = imageio.imread(img_path, pilmode='RGB')
    length, width = start.shape[0], start.shape[1] #inversion des noms 
    # copie des 50 pixels en haut
    up = start[0:50, :]
    # copie des 50 pixels en bas
    down = start[length - 50:, :]
    
    # nouvelle image intermediaire
    intermed_array = np.concatenate((up, start, down), axis = 0)
    intermed = imageio.imwrite(intermed_path, intermed_array)
    intermediate = imageio.imread(intermed_path, pilmode = "RGB")
    
    # copie des 50 pixels à gauche
    left = intermediate[:,:50]
    # copie des 50 pixels à droite
    right = intermediate[:, width - 50:]
    
    # image finale agrandie
    final_array = np.concatenate((left, intermediate, right), axis = 1)
    final_path = output_path + "/"+output_name
    final = imageio.imwrite(final_path, final_array)

def size_down(img_path, output_name, output_path):
    start = imageio.imread(img_path, pilmode='RGB')
    length, width = start.shape[0], start.shape[1]
    final_array = start[50:length -50, 50: width-50]
    final_path = output_path + "/"+output_name
    final = imageio.imwrite(final_path, final_array)


# size_down("/Users/sophierossi/Desktop/final.jpg", "la_muse_reverse.jpg", "/Users/sophierossi/Desktop" )

# DEFINITION OF PATHS

size_up("/Users/sophierossi/Desktop/bedroom.jpg", "bedroom_big.jpg","/Users/sophierossi/Desktop", "/Users/sophierossi/Desktop/intermed_useless/test.jpg")
input_dir_path = "/Users/sophierossi/Desktop/dataset_360_towns"

# to size up a whole directory
L = os.listdir(input_dir_path)
output_path = "/Users/sophierossi/Desktop/sized_up_imgs"
intermed_path = "/Users/sophierossi/Desktop/intermed_useless/test.jpg"
reverse_path = "/Users/sophierossi/Desktop/sized_down_imgs"
for name in L:
    img_path = input_dir_path + "/"+name
    len_name = len(name)
    output_name = name[:len_name-4]+"_sized_up.jpg"
    size_up(img_path, output_name, output_path, intermed_path)

# to size down a whole directory
L_2 = os.listdir(output_path)
for name in L_2:
    img_path = output_path+"/"+name
    len_name = len(name)
    output_name = name[:len_name-4]+"_reversed.jpg"
    size_down(img_path, output_name, reverse_path)