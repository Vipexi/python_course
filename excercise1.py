#! /usr/bin/python3

from PIL import Image, ImageEnhance
import numpy as np

def grayscale(colors):
    red, green, blue = colors
    return red * 0.07 + green * 0.72 + blue * 0.21
    #We could do just .333 for every color, but from wikipedia
    #tells us that mixing colors like this make picture a little 
    #bit better.

# If you have problem to use writing_file.py, 
# you can manually download picture, and save it
# to right folder.
#
#Next open image file, file needs to be in same folder
image_frame = Image.open('ROS_Crystal_Logo.png')

#next make nympy array from picture

np_image = np.array(image_frame)

#we convert image to grey scale.
#Before we have 3d array with 3 color arrays 
#after this we have 2d array in grey scale

np_image_in_grayscale = np.apply_along_axis(grayscale, 2, np_image)

#Next we convert nympy array to type uint8
#That means that every pixel in array has 8 bit value, that
#can be anything from 0-255
#In case of image usually 0 is black and 255 is white.

np_gray_image_int = np_image_in_grayscale.astype(np.uint8)

#change np array back to image
gray_image = Image.fromarray(np_gray_image_int)

filename = "ros_crystal_grey.png"
#Save image to file
gray_image.save(filename)

#.shape prints shape of n dimensional numpy array
print(np_gray_image_int.shape)

# lets crop picture a little
#we make it a square of 632, we can divide that by 8   
cropped_np_gray_image_int = np_gray_image_int[0:632,0:632]
print(cropped_np_gray_image_int.shape)

gray_image_cropped = Image.fromarray(cropped_np_gray_image_int)
filename = "ros_crystal_grey_cropped.png"

gray_image_cropped.save(filename)

print(cropped_np_gray_image_int.shape[0])
#now we know that image has resolution 632 x 632

#Next we make empty 2d numpy array
small_image = np.zeros((79,79)).astype(np.uint8)
print(small_image)

for x in range(cropped_np_gray_image_int.shape[1]):
    for y in range(cropped_np_gray_image_int.shape[0]):
        small_image[y//8,x//8] = cropped_np_gray_image_int[y,x]

#for index_x in range(79):
#    for index_y in range(79):
#        small_image_np[index_x,index_y] = cropped_np_gray_image_int[index_x, index_y]

ros_crystal_small_easy = Image.fromarray(small_image)

filename = "ros_crystal_small_easy.png"

ros_crystal_small_easy.save(filename)


"""
easy: make for loops to take one pixel from every 8x8 pixels from
cropped_np_gray_image_int and save it right place in small_image array,
make picture from array, and save file as ros_crystal_small_easy.png
return this image and code to moodle

normal: Same that easy, but now look every 8x8 pixels and save brightest
to small_image_array, and use ros_crystal_small_normal.png
return this image and code to moodle

hard: same as easy, but now look every 8x8 pixels and save average of those 
pixels to small_image array, and use ros_crystal_small_hard.png
return this image and code to moodle
"""