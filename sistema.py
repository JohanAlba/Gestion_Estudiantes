from estudiante import Estudiante

class SistemaEstudiantes:
    #estudiantes` (dict): Diccionario `{id: objeto_Estudiante}`
    #archivo_datos` (str): Ruta al archivo JSON

    
    def __init__(self, archivo_datos='datos/estudiantes.json'):
        self.archivo_datos = archivo_datos
        self.estudiantes = {}
        self.cargar_datos()

    
    def agregar_estudiante(self, id_estudiante, nombre, edad):
        # Crea y agrega un nuevo estudiante
        # Validar que el ID no exista
        # Retornar True si se agregó, False si ya existe
        
        if id_estudiante in self.estudiantes:
            print('El estudiante ya existe')
            return False
    
        nuevo_estudiante =Estudiante (id_estudiante,nombre,edad)
        self.estudiantes['id_estudiante'] = nuevo_estudiante
        print('El estudiante se agrego')
        return True


        
