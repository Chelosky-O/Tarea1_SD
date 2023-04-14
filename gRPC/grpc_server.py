from concurrent import futures
import requests

import grpc

import main_pb2_grpc
import main_pb2

'Aqui implentar puerto y nombre redis'


class GreeterService(main_pb2_grpc.DataServicer):

    def getCocktailName(self, request, context):
        '''sacar context '''
        print("mensaje recibido! ")
        index = request.id
        #'caso 1, está en caché'
        #'Caso 2, no está en caché

        '''Sacar el json, formatearlo y dejarlo listo'''

        url = "http://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={}".format(index)
        response = requests.get(url)
        data = response.json()["drinks"]
        #print(data)
       #data = response.json()["drinks"][0]["strDrink"]

        if(data == None):
            print("Respondiendo... : " + "None")
            cocktail_response = main_pb2.cocktailName(name="None")
        else:
            data = data[0]["strDrink"]
            print("Respondiendo... : " + data)
        #"Esta es la respuesta de la api que debería contar en el timer, el resto es obtener la info"
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
