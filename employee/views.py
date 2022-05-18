from django.shortcuts import render

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from kafka import KafkaConsumer
from json import loads
import json
# Create your views here.
class HelloView(APIView):
    #authentication_classes = (TokenAuthentication)
    permission_classes = (IsAuthenticated,)


    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


