from django.shortcuts import render, get_object_or_404
from .models import *
from rest_framework import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
class ItemCreate(APIView):
    def post(self,request):
        serializer=ItemSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        items=Items.objects.all()
        serializer=ItemSerializer(items,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def delete(self,request):
        item_id=request.data.get('id')
        item=get_object_or_404(Items,id=item_id)
        item.delete()
        return Response([],status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk):
        item=get_object_or_404(Items,id=pk)
        serializer=ItemSerializer(item,data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)