import requests
import json
import time
import random
import redis

#Obtiene el id y nombre de los tragos del 11000 -> 16000
def get_by_id():
    
    n = input("Ingrese numero de requests: ")
    i = 0
    r1=redis.Redis(host='localhost', port=6379)
    
    file = open('data.txt','w')
    
    while(i!=n):
        id = random.randint(11000,16000);
        inicio=time.time()
        dato=r1.get(id)
        if(dato== None):
            url = "http://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={}".format(id)
            #url = "http://www.thecocktaildb.com/api/json/v1/1/lookup.php?i=11000"
            response = requests.get(url)
            data = response.json()
            jsonified_data = json.dumps(data)
            
            print("Iteración: ", str(i))
            
            if data['drinks'] != None:
                nombre = data['drinks'][0]['strDrink']
                print(str(id) + " : " + nombre)
                r1.set(id, data['drinks'][0]['strDrink'])

            else:
                print(str(id) + " : " + "ERROR")
        else:
            print(str(id) + " : " + str(dato))
        final=time.time()
        print(final-inicio)
        
        file.write(str((final-inicio))+'\n')
        
        i=i+1
        



get_by_id()
