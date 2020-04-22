# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import service_pb2 as service__pb2


class ChatStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.stream = channel.unary_stream(
        '/grpc.Chat/stream',
        request_serializer=service__pb2.Empty.SerializeToString,
        response_deserializer=service__pb2.Message.FromString,
        )
    self.send_message = channel.unary_unary(
        '/grpc.Chat/send_message',
        request_serializer=service__pb2.Message.SerializeToString,
        response_deserializer=service__pb2.Empty.FromString,
        )


class ChatServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def stream(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def send_message(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ChatServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'stream': grpc.unary_stream_rpc_method_handler(
          servicer.stream,
          request_deserializer=service__pb2.Empty.FromString,
          response_serializer=service__pb2.Message.SerializeToString,
      ),
      'send_message': grpc.unary_unary_rpc_method_handler(
          servicer.send_message,
          request_deserializer=service__pb2.Message.FromString,
          response_serializer=service__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'grpc.Chat', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
