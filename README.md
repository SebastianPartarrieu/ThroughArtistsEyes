# MOVIE_Projet

## Description
Through Artists' Eyes is a VR application coded by four students at Mines ParisTech. We are a team of art lovers who wanted to keep culture alive during the pandemic.
The goal of this app is to bring the artists' universe to people at home. We designed an interactive experience that transforms your perception of real landscapes and cities by painting these scenes with the style of an artist, thanks to machine learning algorithms such as CycleGAN.

We also conducted rigorous user studies to make sure our VR application is safe and does not provoke motion sickness.

Be prepare to see Miami through Monet's eyes, or the ESA platform through Picasso's!

## Installation
All you need is a VR headset, Unity and Steam VR (not much, right :) ).
Use Unity Hub to launch the folder Through Artists' eyes that you can get here : https://drive.google.com/drive/folders/1yee5ryRelxaWK3T8dNSINO-zR2XzHX5K?usp=sharing

Launch Steam VR (accept all requirements) and put your headset on. You will hear a small tutorial in the beginning of your experience. 

You will then be able to navigate between the different scenes thanks to your right pointer.

## Structure
- as mentioned above, everything regarding the VR application can be found in the google drive
- datasets : contains training, testing and results for style transfer models 
- utils : contains pieces of code to manipulate and download different images
 > fetching_pictures.py allows you to automatically download datasets of images from Flickr's API. Get yourself an API key, change the right paths and add the key to the script and you're good to go. This is particularly helpful if you would like to apply style transfer to a very specific kind of dataset or you simply need lots of images to train your model.
 > data_augmentation.py, rather than performing the data augmentation on the fly (with an image generator object in keras for example) this script allows you to perform different operations and save the augmented images to disk. Although this may be inefficient in terms of memory, we can use exactly the same datasets for the different models to compare performance. We also don't need to modify pre-existing code to add image augmentation in the pipeline. We can just add the augmented image to the directory with the 'normal' images.
 > modify_images.py and resize.py are for, as the name suggests, resizing and modifying pictures. These were useful for working with images of similar dimensions and also performing a little trick to get rid of border effects produced by some of our style transfer algorithms. 
- models : contains scripts, notebooks and pieces of code containing the different style transfer models we used to create our different universes. Models include CycleGAN, fast neural style transfer, and 'vanilla' style transfer. Better detailed use guide incoming...

**To learn more about the style transfer aspect of this project:** see [this post](https://sebastianpartarrieu.github.io/projects/2_project/)


