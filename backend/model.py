# Import necessary libraries
import numpy as np
from tensorflow import keras
import os
import sys
import cv2

# Define the upload folder
UPLOAD_FOLDER = 'uploads'
csv_file_path = "data.csv"
# Add the current directory to the system path
sys.path.append(os.getcwd())


class Models:
    def __init__(self):
        # Initialize Linear Regression and Logistic Regression models and decision tree
        print("Initializing models...")
        self.image_size_pixels = 120
        self.cnn_model = keras.models.Sequential([
            keras.layers.Conv2D(filters=32, kernel_size=3,
                                input_shape=(self.image_size_pixels, self.image_size_pixels, 3), activation='relu'),
            keras.layers.MaxPooling2D(pool_size=2),
            keras.layers.Conv2D(filters=64, kernel_size=3, activation='relu'),
            keras.layers.MaxPooling2D(pool_size=2),
            keras.layers.Conv2D(filters=128, kernel_size=3, activation='relu'),
            keras.layers.MaxPooling2D(pool_size=2),
            keras.layers.Flatten(),
            keras.layers.Dense(64, activation='relu'),
            keras.layers.Dense(1, activation='sigmoid')
        ])
        self.cnn_model.compile(optimizer='adam',
                               loss='binary_crossentropy', metrics=['accuracy'])

        print("Models initialized!")

        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)
        folder_path_train = "./data"
        current_directory = os.getcwd()
        full_path_train = os.path.join(current_directory, folder_path_train)
        full_path_train = os.path.normpath(full_path_train)
        print("full_path_train", full_path_train)

        train_images_df = []
        train_labels_df = []
        for filename in os.listdir(full_path_train):
            if filename.endswith(".jpg"):
                image_path = os.path.join(full_path_train, filename)
                if len(train_images_df) % 100 == 0:
                    print(len(train_images_df))
                img = cv2.imread(image_path)
                train_images_df.append(img)
                train_labels_df.append(filename.split(".")[0])
        print("Shape of images array:", len(train_images_df))
        print("Shape of labels array:", train_labels_df[0:10])
        print("Shape of labels array:", train_labels_df[:10])

        train_labels_df = np.array(train_labels_df)
        train_labels_df[train_labels_df == 'cat'] = 0
        train_labels_df[train_labels_df == 'dog'] = 1
        train_labels_df = train_labels_df.astype(np.int32)
        print(train_labels_df[0:10])
        print(train_labels_df[190:])

        train_images_df = [cv2.resize(
            img, (self.image_size_pixels, self.image_size_pixels)) for img in train_images_df]
        train_images_df = np.array(train_images_df)
        train_images_df = train_images_df / (self.image_size_pixels-1)

        self.cnn_model.fit(train_images_df, train_labels_df, epochs=20,
                           batch_size=16, verbose=1, validation_split=0.15)
        print("Model worked successfully.")

    def model(self, dataset):
        print("dataset", dataset)

        folder_path_test = "./uploads"
        print("folder_path_test", folder_path_test)
        current_directory = os.getcwd()
        full_path_test = os.path.join(current_directory, folder_path_test)
        full_path_test = os.path.normpath(full_path_test)
        print("full_path_test", full_path_test)

        test_images_df = []
        for filename in dataset:
            image_path = os.path.join(full_path_test, filename)
            print("image_path", image_path)
            img = cv2.imread(image_path)
            test_images_df.append(img)

        print("Shape of images array:", len(test_images_df))
        test_images_df = [cv2.resize(
            img, (self.image_size_pixels, self.image_size_pixels)) for img in test_images_df]

        test_images_df = np.array(test_images_df)
        test_images_df = test_images_df / (self.image_size_pixels-1)
        print("test_images_df shape :- ", test_images_df.shape)

        y_classes_x_test_df = self.cnn_model.predict(test_images_df)
        y_predicted_x_test_df = np.round(y_classes_x_test_df).astype(
            int).reshape(test_images_df.shape[0])
        print("y_predicted_x_test_df", y_predicted_x_test_df)

        y_predicted_x_test_df = ','.join(
            [str(elem) for elem in y_predicted_x_test_df])

        print("predictions", y_predicted_x_test_df)

        return y_predicted_x_test_df
