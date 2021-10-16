#Programa agenda de contactos
#Metodos: leer, agregar, actualizar y ejecutar
class Agenda: 


    contactos{"data":[]}
    identificador = 0

    #metdos(acciones que realizan )
    def leer(self):
        for i in self.contactos:  #checar esto for i in 
            print("Nombre: ",i["nombre"])
            print("Telefono: ", i["telefono"])
            print("Direccion: ", i ["direccion"])

    def agregar(self):
        #diccionario ["calve"]= valor
        datos = {}
        nombre_inp =input("Ingresa el nombre del nuevo contactos: ")
        telefono_inp =input("Ingrese el telfono del nuevo contacto :")
        direccion_inp= input("Ingrese la direccion: ")
        self.identificador = self.identificador + 1
        data["id"] = self.identificador
        datos["nombre"]= nombre_inp
        datos["telefono"] = telefono_inp
        datos["direccion"] = direccion_inp
    def editar(self):
        for i in self.contactos:
            if(i["id"]==ident):
                #diccionario["clave"] = valor


