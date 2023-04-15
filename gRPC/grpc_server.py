from concurrent import futures
import requests
import redis
import grpc
import time

import main_pb2_grpc
import main_pb2

redis_host = 'localhost'
redis_port = 6379

class GreeterService(main_pb2_grpc.DataServicer):
    def __init__(self):
        self.redis1 = redis.StrictRedis(host=redis_host,
                                       port=redis_port,
                                       charset="utf-8",
                                       decode_responses=True,
                                       db=0)

        self.redis2 = redis.StrictRedis(host=redis_host,
                                    port=6380,
                                    charset="utf-8",
                                    decode_responses=True,
                                    db=0)

        self.redis3 = redis.StrictRedis(host=redis_host,
                                    port=6381,
                                    charset="utf-8",
                                    decode_responses=True,
                                    db=0)
        pass

    def getCocktailName(self, request, context):
        print("mensaje recibido! ")

        index = request.id

        if(index>=11000 and index<12000):
            cache_search = self.redis1.get(index)
        if(index >= 12000 and index < 14000):
            cache_search = self.redis2.get(index)
        if(index >= 14000 and index < 16000):
            cache_search = self.redis2.get(index)

        #caso 1, está en cache
        if cache_search != None:
            print("Dato encontrado en cache!")
            print("Cache" + str(cache_search))
            cocktail_response = main_pb2.cocktailName(name=str(cache_search))

            return(cocktail_response)
        #'Caso 2, no está en cache (Sacar el json, formatearlo y dejarlo listo)

        url = "http://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={}".format(index)
        response = requests.get(url)
        data = response.json()["drinks"]

        if(data == None):
            if(index>=11000 and index<12000):
                self.redis1.set(index, "None")
            if(index >= 12000 and index < 14000):
                self.redis2.set(index, "None")
            if(index >= 14000 and index < 16000):
                self.redis3.set(index, "None")

            print("Respondiendo... : " + "None")
            cocktail_response = main_pb2.cocktailName(name="None")

        else:
            data = data[0]["strDrink"]
            if (index >= 11000 and index < 12000):
                self.redis1.set(index, str(data))
            if (index >= 12000 and index < 14000):
                self.redis2.set(index, str(data))
            if (index >= 14000 and index < 16000):
                self.redis3.set(index, str(data))

            print("Respondiendo... : " + data)
            cocktail_response = main_pb2.cocktailName(name = str(data))

        return cocktail_response
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    main_pb2_grpc.add_DataServicer_to_server(GreeterService(), server)
    server.add_insecure_port("localhost:50051")
    server.start()
    print("Servidor gRPC en ejecución...")
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
