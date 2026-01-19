import pandas as pd
class Estudiante():
    'clase estudiante'

    def __init__(self,id_estudiante:str,nombre:str,edad:int):
        self.id_estudiante = id_estudiante
        self.nombre = nombre
        self.edad = edad #Constructor
        self.notas = {}

    def agregar_nota(self,materia, calificacion):    
    # Agrega o actualiza la nota de una materia
    # Validar que la calificación esté entre 0 y 10
    # Retornar True si se agregó, False si es inválida
        if calificacion >= 0 and calificacion <=10:
            self.notas [materia] = calificacion
            return True
        else:
            return False
      
    def promedio(self): #Calcular promedio de notas
        try:
            valores = self.notas.values()
            total = sum(valores)
            self.promedio = total / len(valores)
            return self.promedio
        except  ZeroDivisionError:
            return 0




    def aprobado(self,nota_minima=6): #Verificar si aprobó
        pass
    
    def to_dict(): #Convertir a diccionario (para guardar en JSO
        pass    