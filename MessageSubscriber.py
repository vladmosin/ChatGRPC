from abc import abstractmethod


class MessageSubscriber:

    @abstractmethod
    def receive_message(self, message):
        pass
