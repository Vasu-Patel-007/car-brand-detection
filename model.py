import pickle
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D

pickle_load = open("x_saved","rb")
x = pickle.load(pickle_load)

pickle_load = open("y_saved","rb")
y = pickle.load(pickle_load)

y = np.array(y)
# print(x)
# print(y)

x = x/255.0

model = Sequential()

model.add(Conv2D(64 , (3,3), input_shape = x.shape[1:]))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Conv2D(64 , (3,3)))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Flatten())
model.add(Dense(64))

#output layer
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss="categorical_crossentropy",
                    optimizer="adam",
                    metrics=['accuracy'])

model.fit(x,y,batch_size=32, epochs=10,validation_split=.10)
