from flask import Blueprint, request, jsonify
from services.gcs_service import upload_file_to_gcs, list_files_in_gcs

file_blueprint = Blueprint('file', __name__)

@file_blueprint.route('/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    if file:
        upload_file_to_gcs(file)
        return jsonify({'message': 'File uploaded successfully'}), 200
    return jsonify({'message': 'No file uploaded'}), 400

@file_blueprint.route('/files', methods=['GET'])
def list_files():
    files = list_files_in_gcs()
    return jsonify(files), 200
