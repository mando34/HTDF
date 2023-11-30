# pip install python-mnist
# pip install keras-ocr


# HANDWRITTING RNN MODEL

import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.utils import to_categorical
from keras_ocr.datasets import emnist

# Load the EMNIST dataset (handwritten letters)
(x_train, y_train), (x_test, y_test) = emnist.load_data()

# Normalize pixel values to be between 0 and 1
x_train, x_test = x_train / 255.0, x_test / 255.0

# Convert class vectors to binary class matrices
y_train = to_categorical(y_train, 27)  # 27 classes for letters (26 letters + 1 for unknown)
y_test = to_categorical(y_test, 27)

# Define the RNN model
model = models.Sequential()
model.add(layers.SimpleRNN(128, input_shape=(28, 28)))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(27, activation='softmax'))

# Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

# Save the model
model.save("handwritten_text_recognition_rnn_letters_model.h5")


