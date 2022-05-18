# Create your views here.
from rest_framework import status
from django.conf.urls.static import static
from projectkafka.consumer import Consumer
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def getAllApi(request):
    con = Consumer()
    msg = con.run()
    if msg:
        return Response(msg)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_by_computation_resource_type(request):
    con = Consumer()
    msg = con.run()
    messages = []
    if msg:
        for temp in msg:
            if temp['entity'] == "ComputationResourceType":
                messages.append(temp)
        return Response(messages)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_by_resource(request):
    con = Consumer()
    msg = con.run()
    messages = []
    if msg:
        for temp in msg:
            if temp['entity'] == "ComputationResource":
                messages.append(temp)
        return Response(messages)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_by_customer(request):
    con = Consumer()
    msg = con.run()
    messages = []
    if msg:
        for temp in msg:
            if temp['entity'] == "Customer":
                messages.append(temp)
        return Response(messages)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


