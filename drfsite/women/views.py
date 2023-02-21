from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Women
from .serializers import WomenSerializer


# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer


class WomenAPIView(APIView):
    def get(self, request):
        womens = Women.objects.all().values('title', 'content', 'category')
        return Response({'womens': womens})

    def post(self, request):
        data_to_model = Women.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            category_id=request.data['category_id']
        )
        return Response({'created woman': model_to_dict(data_to_model)})
