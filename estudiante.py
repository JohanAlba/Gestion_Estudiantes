#import pandas as pd
class Estudiante():
    
    #clase estudiante
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
            return  total / len(valores)
 
        except  ZeroDivisionError:
            return 0

    def aprobado(self,nota_minima=6): 
        
        # Verifica si el estudiante aprobó
        # Retorna True si promedio >= nota_minima, False en caso contrario
        return self.promedio() >= nota_minima
    
    def to_dict(self): 
        
        # Convierte el estudiante a un diccionario
        # Para poder guardarlo en JSON
        # Retorna: {'id': ..., 'nombre': ..., 'edad': ..., 'notas': {...}
        
        return {
            'id':self.id_estudiante,
            'nombre':self.nombre,
            'edad':self.edad,
            'notas':self.notas
        }
    @staticmethod
    def from_dict(data):
        # Método estático (@staticmethod)
        # Crea un objeto Estudiante desde un diccionario
        # Útil para cargar datos desde JSON

        id = data['id']
        nombre = data['nombre']
        edad = data['edad']
        
        estudiante = Estudiante(id,nombre,edad)
        
        estudiante.notas = data.get('notas',{})

        return estudiante
    
    def __str__(self):
        
        # Representación legible del estudiante
        # Ejemplo: "[001] Juan Pérez (20 años) - Promedio: 8.5 ✅ Aprobado"
        promedio = self.promedio()
        if self.aprobado():
            estado = '✅ Aprobado'
        else:
            estado = '❌ Reprobado'
        return f'[{self.id_estudiante}] {self.nombre} ({self.edad} años) - Promedio: {promedio:.2f} {estado}'
        