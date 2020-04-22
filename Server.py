import time

import grpc
from concurrent import futures

import resources.service_pb2 as service
import resources.service_pb2_grpc as rpc


class Server(rpc.ChatServicer):
    def __init__(self):
        self.chats = []

    def stream(self, request, context):
        processed = 0
        while True:
            while processed < len(self.chats):
                chat = self.chats[processed]
                processed += 1
                yield chat

    def send_message(self, message, context):
        self.chats.append(message)
        return service.Empty()


def serve(port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    rpc.add_ChatServicer_to_server(Server(), server)
    server.add_insecure_port('[::]:{}'.format(port))
    server.start()

    while True:
        time.sleep(10000)
