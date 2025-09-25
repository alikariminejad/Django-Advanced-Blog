from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def postList(request):
    return Response("ok")

@api_view(['GET'])
def postDetail(request, id):
    return Response({"id": id})