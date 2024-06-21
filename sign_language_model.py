import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import zipfile
import os

# Download and extract the dataset

with zipfile.ZipFile('master.zip', 'r') as zip_ref:
    zip_ref.extractall()

# Set up paths - Verify this path is correct after extracting the zip file
base_dir = 'Sign-Language-Digits-Dataset-master/Dataset'
train_dir = os.path.join(base_dir, '')
test_dir = os.path.join(base_dir, '')

# Check if the training directory exists
if not os.path.exists(train_dir):
    print("Training directory not found. Please check the path and extraction.")
else:
    # Preprocess data
    train_datagen = ImageDataGenerator(rescale=1./255)
    test_datagen = ImageDataGenerator(rescale=1./255)

    train_generator = train_datagen.flow_from_directory(
        train_dir,
        target_size=(64, 64),
        batch_size=32,
        color_mode='grayscale',
        class_mode='categorical'
    )

    test_generator = test_datagen.flow_from_directory(
        test_dir,
        target_size=(64, 64),
        batch_size=32,
        color_mode='grayscale',
        class_mode='categorical'
    )

    # Define the model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 1)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')  # Adjust number of classes if necessary
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_generator, epochs=10, validation_data=test_generator)

# Save the model
model.save('sign_language_model.h5')