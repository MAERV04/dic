meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "AFK": "fuera del teclado",
            "BOOMER":"Muy viejo y no quiere entender a lo jovenes",
            "BASADO": "tiene a su disposicion toda la verdad",
            "CREEPY": "Tenebroso o de miedo",
            "GG":" buena partida",
            "NT":"Buen intento",
            "EZ":"Facil",
            "bad tm8":"mal compañero de emparejamiento"
            }
            
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print("el significado de", word, "es", meme_dict[word])
else:
    print("lo siento la palabra no se encuentra en el diccionario")
