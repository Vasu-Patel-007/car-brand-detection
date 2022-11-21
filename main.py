import numpy as np
import matplotlib.pyplot as plt
import os
import cv2

data_directory = "../cmpsc445_final_project/cars_train"
image_size = 200
training_dataset = []

for img in os.listdir(data_directory):
    image_array = cv2.imread(os.path.join(data_directory, img), cv2.IMREAD_GRAYSCALE)
    resized_image = cv2.resize(image_array,(image_size,image_size))
    plt.imshow(resized_image,cmap="gray")
    plt.show()
    # print(image_array)
    # print(image_array.shape)
    break
    


