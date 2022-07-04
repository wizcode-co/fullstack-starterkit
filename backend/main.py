""" create functions that can be deployed to Firebase Cloud Functions """

import functions_framework


class Response(dict):
    def __init__(self, status, body):
        super().__init__(self, status=status, body=body)


@functions_framework.http
def home(request):
    if request.method == 'GET':
        return Response(200, "Simple server is running")
    return Response(400, "Incorrect HTTP request type")
