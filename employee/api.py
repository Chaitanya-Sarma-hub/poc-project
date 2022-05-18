from rest_framework import generics

from projectkafka.producer import kafka_producer
from .serializer import CustomerSerializer, ComputationResourceSerializer, ComputationResourceTypeSerializer
from .models import Customer, ComputationResource, ComputationResourceType
#from pythonProject2 import Producer
#from pythonProject2.employee.producer import kafka_producer
from datetime import datetime





class ComputationResourceTypeCreateApi(generics.CreateAPIView):
    queryset = ComputationResourceType.objects.all()
    serializer_class = ComputationResourceTypeSerializer
    now = datetime.now().time()

    x = {
        "operation": "Create",
        # "user": ComputationResourceType.partnumber,
        "timestamp": now,
        "status": "success",
        "entity": "ComputationResourceType"
    }
    # msg = json.dumps(x)
    msg = x
    # print(type(x))
    pro = kafka_producer('poc')
    pro.send_message(msg)
    print(msg)


class ComputationResourceTypeApi(generics.ListAPIView):
    queryset = ComputationResourceType.objects.all()
    serializer_class = ComputationResourceTypeSerializer


class ComputationResourceTypeUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = ComputationResourceType.objects.all()
    serializer_class = ComputationResourceTypeSerializer

    now = datetime.now().time()
    x = {
        "operation": "Update",
        # "user": ComputationResourceType.partnumber,
        "timestamp": now,
        "status": "success",
        "entity": "ComputationResourceType"
    }
    # msg = json.dumps(x)
    msg = x
    # print(type(x))
    pro = kafka_producer('poc')
    pro.send_message(msg)
    print(msg)


class ComputationResourceTypeDeleteApi(generics.DestroyAPIView):
    queryset = ComputationResourceType.objects.all()
    serializer_class = ComputationResourceTypeSerializer
    now = datetime.now().time()
    x = {
        "operation": "Delete",
        # "user": ComputationResourceType.partnumber,
        "timestamp": now,
        "status": "success",
        "entity": "ComputationResourceType"
    }
    # msg = json.dumps(x)
    msg = x
    # print(type(x))
    # Producer.run(msg)
    pro = kafka_producer('poc')
    pro.send_message(msg)
    print(msg)


class ComputationResourceCreateApi(generics.CreateAPIView):
    queryset = ComputationResource.objects.all()
    serializer_class = ComputationResourceSerializer
    now = datetime.now().time()
    x = {
        "operation": "Create",
        # "user": ComputationResource.name,
        "timestamp": now,
        "status": "success",
        "entity": "ComputationResource"
    }
    # msg = json.dumps(x)
    # Producer.run(msg)
    msg = x
    # print(type(x))
    pro = kafka_producer('poc')
    pro.send_message(msg)
    print(msg)


class ComputationResourceApi(generics.ListAPIView):
    queryset = ComputationResource.objects.all()
    serializer_class = ComputationResourceSerializer


class ComputationResourceUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = ComputationResource.objects.all()
    serializer_class = ComputationResourceSerializer
    now = datetime.now().time()
    x = {
        "operation": "Update",
        # "user": ComputationResource.name,
        "timestamp": now,
        "status": "success",
        "entity": "ComputationResource"
    }
    # msg = json.dumps(x)
    # Producer.run(msg)
    msg = x
    # print(type(x))
    pro = kafka_producer('poc')
    pro.send_message(msg)
    print(msg)


class ComputationResourceDeleteApi(generics.DestroyAPIView):
    queryset = ComputationResource.objects.all()
    serializer_class = ComputationResourceSerializer
    now = datetime.now().time()
    x = {
        "operation": "Delete",
        # "user": ComputationResource.name,
        "timestamp": now,
        "status": "success",
        "entity": "ComputationResource"
    }
    # msg = json.dumps(x)
    # producer.run(msg)
    msg = x
    # print(type(x))
    pro = kafka_producer('poc')
    pro.send_message(msg)
    print(msg)


class CustomerCreateApi(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    now = datetime.now().time()
    x = {
        "operation": "Create",
        # "user": Customer.name,
        "timestamp": now,
        "status": "success",
        "entity": "Customer"
    }
    # msg = json.dumps(x)
    msg = x
    # print(type(x))
    # Producer.run(msg)
    pro = kafka_producer('poc')
    pro.send_message(msg)
    print(msg)


class CustomerApi(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerUpdateApi(generics.RetrieveUpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    now = datetime.now().time()
    x = {
        "operation": "Update",
        # "user": Customer.name,
        "timestamp": now,
        "status": "success",
        "entity": "Customer"
    }
    # msg = json.dumps(x)
    # Producer.run(msg)
    msg = x
    # print(type(x))
    pro = kafka_producer('poc')
    pro.send_message(msg)
    print(msg)


class CustomerDeleteApi(generics.DestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    now = datetime.now().time()
    x = {
        "operation": "Create",
        # "user": Customer.name,
        "timestamp": now,
        "status": "success",
        "entity": "Customer"
    }
    # msg = json.dumps(x)
    msg = x
    # print(type(x))
    # Producer.run(msg)
    pro = kafka_producer('poc')
    pro.send_message(msg)
    print(msg)