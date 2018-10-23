from rest_framework.decorators import api_view
from rest_framework.response import Response
from .file_helper import file_get_contents

@api_view(['GET'])
def status(request):
    version=file_get_contents("../VERSION")
    print (version)
    return Response({
    "name":"notification-microservice",
    "online": True,
    "version":version,
})

def file_get_contents(filename):
    with open(filename) as f:
        return f.read()
