from django.shortcuts import render, get_object_or_404
from .models import *
from rest_framework import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.

class Query(APIView):
    def get(self,request,category):
        item=Items.objects.filter(category=category)
        if(item.exists()):
            serializer=ItemSerializer(item,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response([],status=status.HTTP_400_BAD_REQUEST)
    
class SortQuery(APIView):
    def get(self,request):
        item=Items.objects.all().order_by('-price')
        serializer=ItemSerializer(item,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class ItemCreate(APIView):
    def post(self,request):
        serializer=ItemSerializer(data=request.data)
        if(serializer.is_valid()):
            barcode=serializer.validated_data['barcode']
            if(Items.objects.filter(barcode=barcode).exists()):
                return Response({"barcode":["Item with this barcode already exist"]},status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        items=Items.objects.all()
        serializer=ItemSerializer(items,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def delete(self,request,pk):
        try:
            item=Items.objects.get(pk=pk)
        except Items.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        item.delete()
        return Response([],status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk):
        item = Items.objects.filter(pk=pk).first()     #.first() retrieves the first item if it exists, or None if it doesn’t.
        if item is None:
            return Response({"detail": "Item not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)