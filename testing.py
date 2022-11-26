import cv2
import tensorflow as tf

def convert_image_to_array(file_path):
    image_size = 250
    image_array = cv2.imread(file_path,cv2.IMREAD_GRAYSCALE)
    resize_array = cv2.resize(image_array, (image_size,image_size))
    resize_array = resize_array.reshape(-1, image_size, image_size, 1)
    return resize_array

brands = ["audi","bmw"]

model = tf.keras.models.load_model("cnn_brand_prediction.model")

prediction = model.predict([convert_image_to_array("2023.png")])

print(brands[int(prediction)])