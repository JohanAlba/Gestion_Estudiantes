# 📚 Sistema de Gestión de Estudiantes

## 📋 Descripción del Proyecto

Sistema de gestión de estudiantes desarrollado en Python que permite administrar información de estudiantes, sus notas y generar reportes. Este proyecto está diseñado como práctica de programación orientada a objetos, manejo de archivos y estructuras de datos.

**Objetivo:** Crear una aplicación CLI (Command Line Interface) que posteriormente se convertirá en una aplicación de escritorio con interfaz gráfica.

---

## 🎯 Objetivos de Aprendizaje

- ✅ Programación Orientada a Objetos (POO)
- ✅ Manejo de archivos JSON
- ✅ Validaciones y manejo de excepciones
- ✅ Estructura de proyecto profesional
- ✅ CRUD completo (Create, Read, Update, Delete)
- ✅ Persistencia de datos

---

## 📁 Estructura del Proyecto

```
gestion_estudiantes/
│
├── main.py                 # Punto de entrada de la aplicación
├── estudiante.py           # Clase Estudiante
├── sistema.py              # Clase SistemaEstudiantes (lógica principal)
├── menu.py                 # Interfaz de menú CLI
├── datos/
│   └── estudiantes.json    # Archivo de persistencia de datos
├── README.md               # Este archivo
└── requirements.txt        # Dependencias (si las hay)
```

---

## 🏗️ Arquitectura del Sistema

### **1. Clase `Estudiante` (estudiante.py)**

**Responsabilidad:** Representar a un estudiante individual con sus datos y notas.

#### Atributos:
- `id` (str): Identificador único del estudiante
- `nombre` (str): Nombre completo
- `edad` (int): Edad del estudiante
- `notas` (dict): Diccionario con formato `{materia: calificacion}`

#### Métodos requeridos:

```python
__init__(self, id_estudiante, nombre, edad)
    # Constructor de la clase

agregar_nota(self, materia, calificacion)
    # Agrega o actualiza la nota de una materia
    # Validar que la calificación esté entre 0 y 10
    # Retornar True si se agregó, False si es inválida

promedio(self)
    # Calcula y retorna el promedio de todas las notas
    # Si no hay notas, retornar 0

aprobado(self, nota_minima=6.0)
    # Verifica si el estudiante aprobó
    # Retorna True si promedio >= nota_minima, False en caso contrario

to_dict(self)
    # Convierte el estudiante a un diccionario
    # Para poder guardarlo en JSON
    # Retorna: {'id': ..., 'nombre': ..., 'edad': ..., 'notas': {...}}

from_dict(data)
    # Método estático (@staticmethod)
    # Crea un objeto Estudiante desde un diccionario
    # Útil para cargar datos desde JSON

__str__(self)
    # Representación legible del estudiante
    # Ejemplo: "[001] Juan Pérez (20 años) - Promedio: 8.5 ✅ Aprobado"
```

---

### **2. Clase `SistemaEstudiantes` (sistema.py)**

**Responsabilidad:** Gestionar la colección de estudiantes y operaciones CRUD.

#### Atributos:
- `estudiantes` (dict): Diccionario `{id: objeto_Estudiante}`
- `archivo_datos` (str): Ruta al archivo JSON

#### Métodos requeridos:

```python
__init__(self, archivo_datos='datos/estudiantes.json')
    # Constructor
    # Cargar datos automáticamente si el archivo existe

agregar_estudiante(self, id_estudiante, nombre, edad)
    # Crea y agrega un nuevo estudiante
    # Validar que el ID no exista
    # Retornar True si se agregó, False si ya existe

eliminar_estudiante(self, id_estudiante)
    # Elimina un estudiante por ID
    # Retornar True si se eliminó, False si no existe

buscar_estudiante(self, id_estudiante)
    # Busca y retorna un estudiante por ID
    # Retornar objeto Estudiante o None

buscar_por_nombre(self, nombre)
    # Busca estudiantes cuyo nombre contenga el texto
    # Retornar lista de estudiantes encontrados

listar_estudiantes(self)
    # Retorna lista de todos los estudiantes

agregar_nota_estudiante(self, id_estudiante, materia, calificacion)
    # Agrega una nota a un estudiante específico
    # Retornar True si se agregó, False si el estudiante no existe

estudiantes_aprobados(self)
    # Retorna lista de estudiantes con promedio >= 6

estudiantes_reprobados(self)
    # Retorna lista de estudiantes con promedio < 6

guardar_datos(self)
    # Guarda todos los estudiantes en el archivo JSON
    # Usar to_dict() de cada estudiante

cargar_datos(self)
    # Carga los estudiantes desde el archivo JSON
    # Usar from_dict() para crear objetos

obtener_estadisticas(self)
    # Retorna un diccionario con estadísticas generales:
    # - Total de estudiantes
    # - Promedio general
    # - Cantidad de aprobados
    # - Cantidad de reprobados
```

---

### **3. Menú CLI (menu.py)**

**Responsabilidad:** Interfaz de usuario por línea de comandos.

#### Funciones requeridas:

```python
mostrar_menu()
    # Muestra las opciones del menú principal

agregar_estudiante_menu(sistema)
    # Solicita datos y agrega un estudiante

ver_estudiantes_menu(sistema)
    # Muestra la lista de todos los estudiantes

buscar_estudiante_menu(sistema)
    # Solicita ID o nombre y busca estudiante(s)

agregar_nota_menu(sistema)
    # Solicita ID de estudiante, materia y calificación

ver_reportes_menu(sistema)
    # Muestra reportes (aprobados, reprobados, estadísticas)

eliminar_estudiante_menu(sistema)
    # Solicita ID y elimina estudiante

ejecutar_menu()
    # Loop principal del menú
    # Maneja la navegación entre opciones
```

---

### **4. Main (main.py)**

**Responsabilidad:** Punto de entrada de la aplicación.

```python
# Importar SistemaEstudiantes y ejecutar_menu
# Inicializar el sistema
# Ejecutar el menú
# Guardar datos al salir
```

---

## 🎨 Diseño del Menú CLI

```
╔════════════════════════════════════════╗
║   SISTEMA DE GESTIÓN DE ESTUDIANTES   ║
╚════════════════════════════════════════╝

1. ➕ Agregar estudiante
2. 📋 Ver todos los estudiantes
3. 🔍 Buscar estudiante
4. 📝 Agregar nota a estudiante
5. 📊 Ver reportes y estadísticas
6. ❌ Eliminar estudiante
7. 💾 Guardar y salir

Selecciona una opción (1-7): _
```

---

## 💾 Formato de Datos (JSON)

### Estructura del archivo `estudiantes.json`:

```json
{
  "001": {
    "id": "001",
    "nombre": "Juan Pérez",
    "edad": 20,
    "notas": {
      "Matemáticas": 8.5,
      "Python": 9.0,
      "Historia": 7.5
    }
  },
  "002": {
    "id": "002",
    "nombre": "María García",
    "edad": 22,
    "notas": {
      "Matemáticas": 9.5,
      "Python": 10.0,
      "Historia": 8.0
    }
  }
}
```

---

## 🔧 Funcionalidades Detalladas

### **1. Agregar Estudiante**
- Solicitar: ID, nombre, edad
- Validar que el ID sea único
- Crear objeto Estudiante
- Agregar al sistema
- Confirmar operación

### **2. Ver Estudiantes**
- Mostrar lista formateada
- Incluir: ID, nombre, edad, promedio, estado
- Si no hay estudiantes, mostrar mensaje

### **3. Buscar Estudiante**
- Opción A: Por ID (exacto)
- Opción B: Por nombre (contiene texto)
- Mostrar resultados o mensaje de no encontrado

### **4. Agregar Nota**
- Solicitar ID del estudiante
- Verificar que existe
- Solicitar materia y calificación
- Validar calificación (0-10)
- Agregar nota
- Mostrar promedio actualizado

### **5. Reportes**
Submenú con opciones:
- Ver estudiantes aprobados
- Ver estudiantes reprobados
- Ver estadísticas generales
- Ver promedio por materia (opcional)

### **6. Eliminar Estudiante**
- Solicitar ID
- Confirmar eliminación
- Eliminar del sistema

### **7. Guardar y Salir**
- Guardar automáticamente en JSON
- Mensaje de confirmación
- Salir del programa

---

## ✅ Validaciones Requeridas

### Estudiante:
- ✅ ID no puede estar vacío
- ✅ ID debe ser único
- ✅ Nombre no puede estar vacío
- ✅ Edad debe ser > 0
- ✅ Calificaciones entre 0 y 10

### Sistema:
- ✅ Manejar archivo JSON inexistente
- ✅ Manejar JSON corrupto
- ✅ Validar operaciones sobre estudiantes inexistentes

---

## 🎯 Manejo de Errores

```python
try:
    # Operaciones con archivos
except FileNotFoundError:
    # Crear archivo nuevo
except json.JSONDecodeError:
    # JSON corrupto, iniciar vacío
except ValueError:
    # Datos inválidos
except Exception as e:
    # Error general
```

---

## 📊 Ejemplo de Uso

```
>>> Sistema iniciado
>>> Estudiantes cargados: 0

[MENÚ]
Opción: 1

Ingrese ID: 001
Ingrese nombre: Juan Pérez
Ingrese edad: 20

✅ Estudiante agregado exitosamente

[MENÚ]
Opción: 4

Ingrese ID del estudiante: 001
Ingrese materia: Matemáticas
Ingrese calificación: 8.5

✅ Nota agregada
📊 Promedio actual: 8.50

[MENÚ]
Opción: 2

=== LISTA DE ESTUDIANTES ===
[001] Juan Pérez (20 años) - Promedio: 8.50 ✅ Aprobado

Total: 1 estudiante(s)
```

---

## 🚀 Roadmap del Proyecto

### **Fase 1: CLI (Actual)** ⬅️ ESTÁS AQUÍ
- [ ] Clase Estudiante
- [ ] Clase SistemaEstudiantes
- [ ] Menú CLI
- [ ] Persistencia JSON
- [ ] Validaciones

### **Fase 2: GUI (Próxima semana)**
- [ ] Interfaz con Tkinter
- [ ] Ventanas de formularios
- [ ] Tablas para mostrar datos
- [ ] Botones y eventos

### **Fase 3: Mejoras (Futuro)**
- [ ] Base de datos SQLite
- [ ] Gráficos con matplotlib
- [ ] Exportar reportes PDF
- [ ] Búsqueda avanzada

---

## 📝 Entregables

1. ✅ Código fuente completo y comentado
2. ✅ README con instrucciones de uso
3. ✅ Archivo JSON de ejemplo con datos
4. ✅ Manejo de errores robusto
5. ✅ Código subido a GitHub

---

## 🎓 Conceptos Practicados

- Programación Orientada a Objetos
- Encapsulamiento
- Métodos estáticos
- Manejo de archivos
- Serialización/Deserialización (JSON)
- Validación de datos
- Manejo de excepciones
- Estructuras de datos (diccionarios, listas)
- Interfaz CLI
- Organización de código en módulos

---

## 💡 Tips de Desarrollo

1. **Desarrolla incrementalmente:** Primero la clase Estudiante, luego Sistema, luego Menú
2. **Prueba cada función:** Crea tests manuales mientras desarrollas
3. **Guarda frecuentemente:** Git commits regulares
4. **Comenta tu código:** Explica la lógica compleja
5. **Maneja errores:** Usa try-except en operaciones críticas

---

## 🏆 Criterios de Éxito

- ✅ Todas las funcionalidades CRUD funcionan
- ✅ Los datos se guardan y cargan correctamente
- ✅ No hay errores sin manejar
- ✅ El código es legible y está organizado
- ✅ La interfaz CLI es clara y fácil de usar

---

## 📞 Notas

Este proyecto es la **Fase 1** de un sistema completo que evolucionará hacia una aplicación de escritorio con interfaz gráfica. Enfócate en hacer la lógica sólida y bien estructurada, ya que luego solo cambiaremos la interfaz, no la lógica del negocio.

---

**¡Buena suerte con el desarrollo! 🚀**