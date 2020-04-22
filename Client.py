from resources.service_pb2_grpc import ChatServicer
from MessageSubscriber import MessageSubscriber
import grpc
import resources.service_pb2_grpc as rpc
import threading
import resources.service_pb2 as service_entities


class Client:

    def __init__(self, address: str = 'localhost:11912'):
        self.subsciber = None
        channel = grpc.insecure_channel(address)
        self.connection = rpc.ChatStub(channel)

        self.listening_thread = threading.Thread(target=self.listen_server_messages, daemon=True)
        self.listening_thread.start()

    def listen_server_messages(self):
        for message in self.connection.stream(service_entities.Empty()):
            self.subscriber.receive_message(message.text, message.date, message.name)

    def send_message(self, text, date, name) -> bool:
        message = service_entities.Message()
        message.text = text
        message.date = date
        message.name = name
        self.connection.send_message(message)
        return True
