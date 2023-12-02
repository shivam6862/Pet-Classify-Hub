# Pet Classify Hub

## Overview

Pet Classify Hub is an application designed for classifying images of pets, specifically cats and dogs. This project utilizes a user-friendly web interface built with Next.js for the frontend and a backend server powered by Flask. The classification models are implemented using TensorFlow, including both Artificial Neural Network (ANN) and Convolutional Neural Network (CNN) models.

## Features

- User-friendly web interface for uploading and classifying pet images.
- Backend server for handling image classification requests.
- Model training and testing functionality for users who want to experiment with new models.

## Technologies Used

- Next.js: A React framework for building user interfaces.
- Flask: A lightweight web application framework for Python.
- Python: The programming language used for the backend and model training.
- TensorFlow: An open-source machine learning framework used for implementing ANN and CNN models.

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/shivam6862/Pet-Classify-Hub.git
   ```

2. **Install dependencies:**

   ```bash
   cd Pet-Classify-Hub/frontend
   npm install
   ```

   ```bash
   cd Pet-Classify-Hub/backend
   pip install -r requirements.txt
   ```

3. **Run the development server:**

   ```bash
   npm run dev
   ```

   ```bash
   cd backend
   python main.py
   ```

   The app will be accessible at `http://localhost:3000`.

## Usage

1. **Navigate to the web interface in your browser.**

2. **Upload an image in the app.**

3. **Click the "Recognize" button to see the model's prediction.**

4. **Explore the training section to train and test new models.**

## Training Models

To train new models, follow these steps:

1. **Prepare a dataset of cat and dog images.**

2. **Place the dataset in the `data` directory.**

3. **Use the training functionality in the app to train and test new models.**

## Contributing

If you'd like to contribute to this project, please follow the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Special thanks to shivam6862 for contributing to the project.
