from flask import Blueprint, request
from . import Response

views = Blueprint('views', __name__)


@views.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        return Response(200, "Simple server is running")
    return Response(400, "Incorrect HTTP request type")
