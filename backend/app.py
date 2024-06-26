from flask import Flask, request, jsonify, send_from_directory
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
import os

app = Flask(__name__, static_folder='../frontend', static_url_path='/')

# Azure Cognitive Services credentials
subscription_key = '9d7c807d-7a92-4035-96a5-e6ed8a51300e'
endpoint = 'https://imageclassifieravanadehackathon.cognitiveservices.azure.com/'
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

@app.route('/')
def home():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/classify-image', methods=['POST'])
def classify_image():
    file = request.files['file']
    image_data = file.read()
    analysis = computervision_client.analyze_image_in_stream(image_data, visual_features=['Description', 'Tags'])
    return jsonify(analysis.as_dict())

@app.route('/rag-chatbot', methods=['POST'])
def rag_chatbot():
    query = request.json.get('query')
    # Implement RAG logic here
    response = {"answer": "This is a placeholder response."}
    return jsonify(response)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
