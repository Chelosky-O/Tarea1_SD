import requests
import json
import time
import random

#Obtiene el id y nombre de los tragos del 11000 -> 16000
def get_by_id():
    max_time = 0.0
    max_i = 0
    x = input("Ingrese numero de requests: ")
    
    file = open('data.txt','w')
    
    for i in range(0,int(x)):
        random_n = random.randint(11000,16000)
        url = "http://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={}".format(random_n)
        #url = "http://www.thecocktaildb.com/api/json/v1/1/lookup.php?i=11000"
        start = time.time()
        response = requests.get(url)
        end = time.time()
        data = response.json()
        jsonified_data = json.dumps(data)
        
        
       
        id = random_n
        #print(data['drinks'])
        
        if data['drinks'] != None:
            nombre = data['drinks'][0]['strDrink']
            print(str(i) + " : " + str(id) + " : " + nombre)
            
        
        else:
            print(str(i) + " : " + str(id) + " : " + "ERROR")
        
        print((end - start))
        
        if (end - start) > max_time:
            max_time = (end - start)
            max_i = i
        
        file.write(str((end - start))+'\n')
        
    print("TIEMPO MAXIMO: " + str(max_time) + " INDICE: " + str(max_i))

get_by_id()