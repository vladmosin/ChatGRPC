from abc import abstractmethod


class MessageSubscriber:

    @abstractmethod
    def receive_message(self, text, date, name):
        pass
