
class registroInventario:
    def __init__(self,nombre,apellido,correo,contrasena ):

        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.contrasena = contrasena


    def formato_doc(self):
        return{
            
            'nombre': self.nombre,
            'apellido': self.apellido,
            'correo': self.correo,
            'contrasena':self.contrasena
    
        }   
