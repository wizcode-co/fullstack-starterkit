from flask import Blueprint, request, jsonify
from flask_cors import cross_origin

views = Blueprint('views', __name__)


@views.route('/', methods=['GET'])
@cross_origin()
def home():
    if request.method == 'GET':
        response = jsonify(message="Simple server is running")

        response.content_type = "application/json"
        return response
    return ""
