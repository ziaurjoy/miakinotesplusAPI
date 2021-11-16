from django.shortcuts import render

# Create your views here.


from copy import Error
from django.db.models.query import QuerySet
from blog.serializers import PostSirializer
from blog.models import Post

from rest_framework import status
from rest_framework.generics import get_object_or_404, Http404
from rest_framework.response import Response
from rest_framework import serializers, viewsets
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.



class PostViewSet(viewsets.ViewSet):

    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def list(self, request):
        try:
            queryset = Post.objects.all()
            serializer = PostSirializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


    def create(self, request):
        try:
            serializer = PostSirializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
  

    def retrieve(self, request, pk=None):
        try:
            queryset = Post.objects.all()
            get_Post = get_object_or_404(queryset, pk=pk)
            serializer = PostSirializer(get_Post)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
    

    def update(self, request, pk=None):
        try:
            queryset = Post.objects.all()
            get_post = get_object_or_404(queryset, pk=pk)
            serializer = PostSirializer(get_post, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
 
    
    def delete(self, request, pk=None):
        try:
            queryset = Post.objects.all()
            get_post = get_object_or_404(queryset, pk=pk)
            get_post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except AttributeError:
            return Response(status=status.HTTP_204_NO_CONTENT)



post_list = PostViewSet.as_view({'get': 'list'})
post_details = PostViewSet.as_view({'get': 'retrieve'})
post_create = PostViewSet.as_view({'post': 'create'})
post_update = PostViewSet.as_view({'put': 'update'})
post_delete = PostViewSet.as_view({'delete': 'delete'})