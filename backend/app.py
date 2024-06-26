
from flask import Flask, request, jsonify
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
import os

app = Flask(__name__)
subscription_key = '9d7c807d-7a92-4035-96a5-e6ed8a51300e'

endpoint = 'https://imageclassifieravanadehackathon.cognitiveservices.azure.com/'
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

@app.route('/')
def home():
    return "Radiology Assistant App!"

@app.route('/classify-image', methods=['POST'])
def classify_image():
    file = request.files['file']
    image_data = file.read()
    result = computervision_client.analyze_image_in_stream(image_data)
    return jsonify(result.as_dict())

@app.route('/rag-chatbot', methods=['POST'])
def rag_chatbot():
    query = request.json.get('query')
    # Implement RAG logic here
    response = {"answer": "This is a placeholder response."}
    return jsonify(response)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
