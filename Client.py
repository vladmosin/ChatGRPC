from resources.service_pb2_grpc import ChatServicer
from MessageSubscriber import MessageSubscriber
import grpc
import resources.service_pb2_grpc as rpc
import threading
import resources.service_pb2 as service_entities


class Client:

    def __init__(self, subscriber: MessageSubscriber, address: str = 'localhost:11912'):
        self.subscriber = subscriber
        channel = grpc.insecure_channel(address)
        self.connection = rpc.ChatStub(channel)

        self.listening_thread = threading.Thread(target=self.listen_server_messages, daemon=True)
        self.listening_thread.start()

    def listen_server_messages(self):
        for message in self.connection.receive_message(service_entities.Empty()):
            self.subscriber.receive_message(message)

    def send_message(self, message_text, data, name):
        message = service_entities.Message()
        message.text = message_text
        message.data = data
        message.name = name
        self.connection.send_message(message)
