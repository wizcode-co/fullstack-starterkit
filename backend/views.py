""" create local routes to your functions for testing """

from flask import Blueprint, request
import main

views = Blueprint('views', __name__)

@views.route('/', methods=['GET'])
def home():
    return main.home(request)
