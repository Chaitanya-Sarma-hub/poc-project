import json
import threading

from kafka import KafkaConsumer


class Consumer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.stop_event = threading.Event()

    def stop(self):
        self.stop_event.set()

    def run(self):
        consumer = KafkaConsumer(
            #'topic:poc',
            'poc',
            bootstrap_servers='localhost:9092',
            auto_offset_reset='earliest'
        )
        messages = []
        for message in consumer:
            #message = (json.dumps(message))
            messages.append(message)
        return messages
