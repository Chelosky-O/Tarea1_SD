import requests
import json

def get_by_id():
    
    for i in range(11000,16000):
        url = "http://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={}".format(i)
        #url = "http://www.thecocktaildb.com/api/json/v1/1/lookup.php?i=11000"
        response = requests.get(url)
        data = response.json()
        jsonified_data = json.dumps(data)
        
        
       
        id = i
        #print(data['drinks'])
        
        if data['drinks'] != None:
            nombre = data['drinks'][0]['strDrink']
            print(str(id) + " : " + nombre)

        #else:
         #   print(str(id) + " : " + "ERROR")
        



get_by_id()