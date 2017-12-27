import json



with open('./datos/sample.txt') as file:
    for line in file:
        tweets = json.loads(line) #Por cada fila cargo un JSON
        try:
            print tweets['place'] #Imprimo el atributo 'place' dentro del try y except
        except:
           print("No existen datos")


