from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from .serializers import PostSerializer, CategorySerializer
from ...models import Post, Category
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

"""@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def postList(request):
    if request.method == 'GET':
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)"""
    
    
'''class PostList(APIView):
    """getting a list of posts and creating new posts"""
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    
    def get(self,request):
        """retrieving a list of posts"""
        posts = Post.objects.filter(status=True)  
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    def post(self, request):
          """creating a post with provided data"""
          serializer = PostSerializer(data=request.data)
          serializer.is_valid(raise_exception=True)
          serializer.save()
          return Response(serializer.data)'''

class PostList(ListCreateAPIView):
    """getting a list of posts and creating new posts"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)


'''@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def postDetail(request, id):
    # try:
    #     post = Post.objects.get(pk=id)
    #     serializer = PostSerializer(post)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    # except Post.DoesNotExist:
    #     return Response({"detail": "Post does not exist"}, status=status.HTTP_404_NOT_FOUND)
    post = get_object_or_404(Post, pk=id, status=True)
    if request.method == "GET":
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        post.delete()
        return Response({"Detail":"Item removed successfully."}, status=status.HTTP_204_NO_CONTENT)'''

'''class PostDetail(APIView):
    """ getting detail of the post and edit plus removing it"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    
    def get(self, request, id):
        """ retrieving the post data"""
        post = get_object_or_404(Post, pk=id, status=True)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    def put(self, request, id):
        """ editing the post data"""
        post = get_object_or_404(Post, pk=id, status=True)
        serializer = self.serializer_class(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self, request, id):
        post = get_object_or_404(Post, pk=id, status=True)
        post.delete()
        return Response({"Detail":"Item removed successfully."}, status=status.HTTP_204_NO_CONTENT)'''

class PostDetail(RetrieveUpdateDestroyAPIView):
    """getting detail of the post and edit plus removing it"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)

# Example for Viewset in CBV
class PostModelViewSet(viewsets.ModelViewSet):
    """getting a list of posts and creating new posts"""
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category', 'author', 'status']
    search_fields = ['title', 'content']

class CategoryModelViewSet(viewsets.ModelViewSet):
    """getting a list of categories and creating new categories"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
