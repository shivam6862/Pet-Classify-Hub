from flask import Flask, jsonify, request
from flask_cors import CORS
import os
from model import Models
app = Flask(__name__, static_url_path='/uploads', static_folder='uploads')
CORS(app)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/home', methods=['GET'])
def home():
    response_obj = [{
        "message": "successfully run the server."
    }]
    response_headers = {
        "Access-Control-Allow-Origin": "*"
    }
    return jsonify(response_obj), 200, response_headers


@app.route('/predictpetclassifyhub', methods=['POST'])
def predictpetclassifyhub():
    try:
        uploaded_files = request.files.getlist('file')

        if not uploaded_files:
            return jsonify({"message": "Missing  Images!!",
                            "title": "Image not found",
                            "status": "Info", }), 400

        dataset = []

        for uploaded_file in uploaded_files:
            filename = os.path.join(
                app.config['UPLOAD_FOLDER'], uploaded_file.filename)
            dataset.append(uploaded_file.filename)
            uploaded_file.save(filename)

        predictions = models.model(dataset=dataset)

        response_obj = {
            "predictions_dataset": "predictions_dataset",
            "about": predictions,
            "message": "Predictions saved successfully.",
            "title": "Generated by ML",
            "status": "Success",
        }

        response_headers = {
            "Access-Control-Allow-Origin": "*"
        }
        return jsonify(response_obj), 200, response_headers
    except Exception as e:
        print(e)
        return jsonify({"error": "An error occurred",
                        "about": "",
                        "message": "Predictions failed to save!",
                        "title": "Generated by ML",
                        "status": "Error", }), 500


if __name__ == "__main__":
    models = Models()
    app.run(host="localhost", port=8501)

# .\env\Scripts\activate
