from abc import ABCMeta, abstractmethod
class Animal(object):
    
    def __init__(self,tipo,mamifero,descripcion,apodo):
        self.tipo=tipo
        self.mamifero=mamifero
        self.descripcion=descripcion
        self.apodo=apodo
        
    def getTipo():
        return self.tipo
    
    def setTipo(self, tipo):
        self.tipo= tipo

    def getDescripcion():
        return descripcion

    def setDescripcion(self, descripcion):
        self.descripcion= descripcion
        
    def getMamifero():
        return self.mamifero

    def setMamifero(self,mamifero):
        self.mamifero=mamifero

    def getApodo():
        return self.apodo

    def setApodo(self, apodo):
        self.apodo= apodo

class Invertebrado(Animal):
    invertebrado="Invertebrado"
    def __init__(invertebrado):
        super().setInvertebrado()
            
    def setTipo(invertebrado):
        self.invertebrado=invertebrado;
    def getTipo():
        return invertebrado

class Vertebrado(Animal):
    tipo="Vertebrado"
    def __init__(tipo):
        super().setVertebrado()
        super().getVertebrado()

        
    def setTipo(tipo):
        self.tipo=tipo;
    def getTipo():
        return tipo

class Mamifero(Vertebrado):
    mamifero="Mamífero"
    def __init__(mamifero):
        super().setMamifero()
        super().getMamifero()

        
    def setMamifero(mamifero):
        self.mamifero=mamifero;
    def getMamifero():
        return mamifero
    
class Perro(Mamifero):
    descripcion="Canino. 4 patas. Carnívoro"
    apodo="Max"
    def __init__(self,apodo,descripcion):
        super().setApodo()
        super().setDescripcion()
    def getDescripcion():
        return descripcion
    def setDescripcion (descripcion):
        self.descripcion=descripcion
    def getApodo():
        return apodo
    def setApodo(apodo):
        self.apodo=apodo

class Main:
    
    animal = Perro(apodo, descripcion)
    animal.setTipo()
    animal.setMamifero()
    animal.setDescripcion()
    animal.setApodo()

    print (animal.getTipo()+animal.getMamifero()+animal.getDescripcion+
               animal.getApodo())
    
    #def printAnimal(tipo,mamifero,descripcion,apodo):
     #   print (animal.getTipo()+animal.getMamifero()+animal.getDescripcion+
      #         animal.getApodo())
    
  #  animal.printAnimal()





    




        
