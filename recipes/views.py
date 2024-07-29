from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.exceptions import ValidationError
from .models import Recipe
from .serializers import RecipeSerializer

class RecipeListCreate(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def create(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            print(e)
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class RecipeListByUser(generics.ListAPIView):
    serializer_class = RecipeSerializer

    def get_queryset(self):
        user_uid = self.kwargs['uid']
        return Recipe.objects.filter(uid=user_uid)

class RecipeUpdateByNameAndUid(generics.UpdateAPIView):
    serializer_class = RecipeSerializer
    lookup_field = 'name'

    def get_queryset(self):
        name = self.kwargs['name']
        uid = self.kwargs['uid']
        return Recipe.objects.filter(name=name, uid=uid)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            return Response(e.detail, status=status.HTTP_400_BAD_REQUEST)
        self.perform_update(serializer)
        return Response(serializer.data)
    
class RecipeDeleteByNameAndUid(generics.DestroyAPIView):
    serializer_class = RecipeSerializer
    lookup_field = 'name'

    def get_queryset(self):
        name = self.kwargs['name']
        uid = self.kwargs['uid']
        return Recipe.objects.filter(name=name, uid=uid)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_queryset().first()
        if not instance:
            raise NotFound("Recipe not found")
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)