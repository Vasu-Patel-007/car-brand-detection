import numpy as np
import matplotlib.pyplot as plt
import os
import cv2

data_directory = "../cmpsc445_final_project/cars_train" # path to the training dataset folder
image_size = 200 # image size to convert all the images into 
training_dataset = [] # all the images will be converted to array and will be appended to this list

for img in os.listdir(data_directory):
    # this for loop basically open each image in the folder and do the steps below and add it to training dataset[]
    
    image_array = cv2.imread(os.path.join(data_directory, img), cv2.IMREAD_GRAYSCALE) #read image and gray_scale it
    resized_image = cv2.resize(image_array,(image_size,image_size)) # resize the image
    # plt.imshow(resized_image,cmap="gray") # debugging purpose
    # plt.show() # debugging purpose
    # # print(image_array) # debugging purpose
    # # print(image_array.shape) # debugging purpose
    break
    


