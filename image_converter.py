import numpy as np
import matplotlib.pyplot as plt
import os
import cv2
import csv
import pickle

def list_of_list_to_list(temp):
    flat_list = []
    for inner_list in temp:
        for item in inner_list:
            flat_list.append(item)
    return flat_list
    

data_directory = "../brand_identification/" # path to the training dataset folder
image_size = 250 # image size to convert all the images into 
training_dataset = [] # all the images will be converted to array and will be appended to this list
brands = ["audi","bmw"]


# csv_reader1 = csv.reader(brand)
# csv_reader2 = csv.reader(label)

# temp1 = list(csv_reader1)
# temp2 = list(csv_reader2)

# brand = list_of_list_to_list(temp1)
# label = list_of_list_to_list(temp2)

# for i in range(0,11):
#     print(int(label[i])-1)

for each_brand in brands:
    # this for loop basically open each image in the folder and do the steps below and add it to training dataset[]
    file_path = os.path.join(data_directory,each_brand)
    label_num = brands.index(each_brand)
    #print(label_num)
    for each_image in os.listdir(file_path):
        try:
            image_array = cv2.imread(os.path.join(file_path, each_image), cv2.IMREAD_GRAYSCALE) #read image and gray_scale it
            resized_image = cv2.resize(image_array,(image_size,image_size)) # resize the image
            # plt.imshow(resized_image,cmap="gray") # debugging purpose
            # plt.show() # debugging purpose
            # print(image_array) # debugging purpose
            # print(resized_image.shape) # debugging purpose
            training_dataset.append([resized_image,label_num])
        except Exception as e:
            pass
print(len(training_dataset))
    
import random
random.shuffle(training_dataset)


x = []
y = []

for feature, label in training_dataset:
    x.append(feature)
    y.append(label)

x = np.array(x).reshape(-1,image_size,image_size,1) # have to convert it to array since NN doesn't take list as input



picke_output = open("x_saved","wb")
pickle.dump(x,picke_output)
picke_output.close()


picke_output = open("y_saved","wb")
pickle.dump(y,picke_output)
picke_output.close()


