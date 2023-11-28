# Import necessary libraries
import pandas as pd
import csv
import os
import sys

# Define the upload folder
UPLOAD_FOLDER = 'uploads'
csv_file_path = "data.csv"
# Add the current directory to the system path
sys.path.append(os.getcwd())


class Models:
    def __init__(self):
        # Initialize Linear Regression and Logistic Regression models and decision tree
        print("Initializing models...")

        print("Models initialized!")

        if not os.path.exists(UPLOAD_FOLDER):
            os.makedirs(UPLOAD_FOLDER)
        print("Model created!")

        updated_data = []

        # Read existing data from the CSV file and update start_angle for the first row
        with open(csv_file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if reader.line_num == 1:
                    row['start_angle'] = 10.0
                updated_data.append(row)

        updated_data_df = pd.DataFrame(updated_data)
        X_train = updated_data_df.drop(columns=["pet"])
        y_train = updated_data_df["pet"]

        print(X_train.head())
        print(y_train.head())
        print("Dataframe created")

        print("CSV file updated successfully.")

    def model(self, dataset):
        # Read existing data from the CSV file and update start_angle for the first row
        updated_data = [dataset]

        updated_data_df = pd.DataFrame(updated_data)
        print("updated_data_df\n", updated_data_df)
        print("updated_data_df\n", updated_data_df.columns)

        predictions_df = []
        print("predictions_df", predictions_df)

        return predictions_df
