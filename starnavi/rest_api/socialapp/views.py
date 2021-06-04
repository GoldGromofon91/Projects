from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Post, Likes
from .serializers import PostSerializer


class IndexView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        return Response({'Hello':'Please check README'})


class PostView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        post_obj = Post.objects.all()
        serializer = PostSerializer(post_obj,many=True)
        return Response({'post':serializer.data})

    def post(self,request):
        post = request.data.get('post')
        serializer = PostSerializer(data=post)
        if serializer.is_valid(raise_exception=True):
            post_save = serializer.save()
            return Response({'success':f'Post{post_save.title}'})

    #TODO заглушки на put,patch,delete