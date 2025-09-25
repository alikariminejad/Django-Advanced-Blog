from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from ...models import Post
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def postList(request):
    return Response("ok")

@api_view(['GET'])
def postDetail(request, id):
    # try:
    #     post = Post.objects.get(pk=id)
    #     serializer = PostSerializer(post)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    # except Post.DoesNotExist:
    #     return Response({"detail": "Post does not exist"}, status=status.HTTP_404_NOT_FOUND)
    post = get_object_or_404(Post, pk=id)
    serializer = PostSerializer(post)
    return Response(serializer.data)