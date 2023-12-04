from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from app.models import *
from app.serializers import *
from rest_framework.response import Response

class productData(APIView):
    def get(self,request,pid):
        Pdata=product.objects.all()
        PJSON=productModelSerializers(Pdata,many=True)
        return Response(PJSON.data)
    
    
    def post(self,request,pid):
        CJSON=request.data
        PUD=productModelSerializers(data=CJSON)
        if PUD.is_valid():
            PUD.save()
            return Response({'message':'product is created'})
        return Response({'message':'product is not created'})
    
     
    def put(self,request,pid):
        CJSD=request.data
        PO=product.objects.get(pid=CJSD['pid'])
        PD=productModelSerializers(PO,data=CJSD)
        if PD.is_valid():
            PD.save()
            return Response({'message':'Product is Updated'})
        return Response({'Failed':'Product is not Updated'})
    
    
    def patch(self,request,pid):
        CJSD=request.data
        PO=product.objects.get(pid=CJSD['pid'])
        PD=productModelSerializers(PO,data=CJSD,partial=True)
        if PD.is_valid():
            PD.save()
            return Response({'message':'Product is Updated'})
        return Response({'Failed':'Product is not Updated'})
    
    def delete(self,request,pid):
        PO=product.objects.get(pid=pid)
        PO.delete()
        return Response({'message':'Product delete sucessfully'})
        
    