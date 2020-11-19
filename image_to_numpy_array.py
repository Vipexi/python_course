#! /usr/bin/python3

from PIL import Image
import numpy as np

image_frame = Image.open('ROS_Crystal_Logo.png')
np_image = np.array(image_frame)
print(np_image.shape)

np_image_turned = np.moveaxis(np_image, 1, 0)
print(np_image_turned.shape)

turned_image = Image.fromarray(np_image_turned)
filename = "ros_crysral_turned.png"
turned_image.save(filename)