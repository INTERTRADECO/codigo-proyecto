from pymongo import MongoClient
import certifi


MONGO='mongodb+srv://brayancristancho09:E4OjJ1TiZbJQ26RF@brayan.3ge2wml.mongodb.net/?retryWrites=true&w=majority&appName=brayan'
certificado=certifi.where() 


def conexionbd ():
    try:
        client= MongoClient(MONGO,tlsCAFile=certificado)
        bd = client["bd_personas"] 
        print('conexion exitosa')
    except ConnectionError:
        print('error de conexion')
    return bd


conexionbd()