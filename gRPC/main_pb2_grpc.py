# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import main_pb2 as main__pb2


class DataStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.getCocktailName = channel.unary_unary(
                '/mypackage.Data/getCocktailName',
                request_serializer=main__pb2.cocktailId.SerializeToString,
                response_deserializer=main__pb2.cocktailName.FromString,
                )


class DataServicer(object):
    """Missing associated documentation comment in .proto file."""

    def getCocktailName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DataServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'getCocktailName': grpc.unary_unary_rpc_method_handler(
                    servicer.getCocktailName,
                    request_deserializer=main__pb2.cocktailId.FromString,
                    response_serializer=main__pb2.cocktailName.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mypackage.Data', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Data(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def getCocktailName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/mypackage.Data/getCocktailName',
            main__pb2.cocktailId.SerializeToString,
            main__pb2.cocktailName.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)