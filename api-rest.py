import requests
import json
import time
import random
import redis

def getfromDocker(id, puerto):
    r=redis.Redis(host='localhost', port=puerto)
    cocktail=r.get(id)
    if(cocktail== None):
        searchBackend(id, puerto)
    else:
         print(str(id) + " : " + str(cocktail))
        
def searchBackend(id, puerto):
    r = redis.Redis(host='localhost', port=puerto)
    url = "http://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={}".format(id)
    #url = "http://www.thecocktaildb.com/api/json/v1/1/lookup.php?i=11000"
    response = requests.get(url)
    data = response.json()
    jsonified_data = json.dumps(data)
            
            
    if data['drinks'] != None:
        nombre = data['drinks'][0]['strDrink']
        print(str(id) + " : " + nombre)
        r.set(id, data['drinks'][0]['strDrink'])
    else:
        nombre = "ERROR"
        print(str(id) + " : " + nombre)
        r.set(id, nombre)

#Obtiene el id y nombre de los tragos del 11000 -> 16000
def get_by_id():
    
    n = int(input("Ingrese numero de requests: "))
    i = 0
    file = open('data.txt','w')
    while(i<=n):
        print("Iteración: ", str(i))
        id = random.randint(11000,16000);
        inicio=time.time()
        if (id>=11000 and id<12000):
            getfromDocker(id, 6379)
        elif (id>=12000 and id<14000):
            getfromDocker(id, 6380)
        else:
             getfromDocker(id, 6381)
        final=time.time()
        print(final-inicio)
        i=i+1
        file.write(str((final-inicio))+'\n')
        



get_by_id()
