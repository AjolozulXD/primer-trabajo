meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            }
word = input("Escribe la palabra que no entiendas (con mayúsculas): ")
if word in meme_dict.keys():
    print (meme_dict[word])
else :
    print ("No se encontró esa palabra")
