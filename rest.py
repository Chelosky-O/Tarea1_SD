import requests
import json
import time

#Obtiene el id y nombre de los tragos del 11000 -> 16000
def get_by_id():
    
    for i in range(11000,16000):
        url = "http://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={}".format(i)
        #url = "http://www.thecocktaildb.com/api/json/v1/1/lookup.php?i=11000"
        start = time.time()
        response = requests.get(url)
        end = time.time()
        data = response.json()
        jsonified_data = json.dumps(data)
        
        
       
        id = i
        #print(data['drinks'])
        
        if data['drinks'] != None:
            nombre = data['drinks'][0]['strDrink']
            print(str(id) + " : " + nombre)
            print((end - start))

        #else:
         #   print(str(id) + " : " + "ERROR")
        



get_by_id()