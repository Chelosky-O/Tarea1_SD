import main_pb2_grpc
import main_pb2
import grpc
import json
import random
from google.protobuf.json_format import MessageToJson

class DataClient(object):
    def __init__(self):
        self.host = 'server'
        self.server_port = '50051'
        #self.channel = grpc.insecure_channel('{}:{}'.format(self.host, self.server_port))
        self.channel = grpc.insecure_channel('localhost:50051')
        self.stub = main_pb2_grpc.DataStub(self.channel)

    def getCocktailNames(self, id):

        request = main_pb2.cocktailId(id = int(id))
        reply = self.stub.getCocktailName(request)
        return reply


print("Ingresa el numero de request: ")
cantidad = input()
for x in range(0,int(cantidad)):
    id = random.randint(11000, 16000)
    print(id)
    client = DataClient()
    response = client.getCocktailNames(id)
    response = MessageToJson(response)
    response = json.loads(response)
    print(response)