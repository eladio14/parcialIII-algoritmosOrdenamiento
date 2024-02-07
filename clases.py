class Archivo:
    def __init__(self, id, nombre, tamaño, extension, fecha_creacion, fecha_modificacion, contenido):
        self.id = id
        self.nombre = nombre
        self.tamaño_total = tamaño
        self.extension = extension
        self.fecha_creacion = fecha_creacion
        self.fecha_modificacion = fecha_modificacion
        self.contenido = contenido

    def mostrar(self):
        print(f"ID: {self.id}, Nombre: {self.nombre}, Tamaño: {self.tamaño_total}, Extensión: {self.extension}, Fecha de creación: {self.fecha_creacion}, Fecha de modificación: {self.fecha_modificacion}")
        
class Carpeta:
    def __init__(self, id, nombre, lista_ficheros, fecha_creacion, lista_carpetas):
        self.id = id
        self.nombre = nombre
        self.lista_ficheros = lista_ficheros
        self.fecha_creacion = fecha_creacion
        self.lista_carpetas = lista_carpetas
        self.tamaño_total = 0

        for item in self.lista_ficheros:
            self.tamaño_total += item.tamaño
    
    
    def mostrar(self):
        print(f"ID: {self.id}, Nombre: {self.nombre}, Fecha de creación: {self.fecha_creacion}, Tamaño total: {self.tamaño_total}")

class UnidadDeAlmacenamiento:
    def __init__(self, id, nombre, capacidad_total, lista_carpetas, tipo_unidad):
        self.id = id
        self.nombre = nombre
        self.capacidad_total = capacidad_total
        self.espacio_disponible = capacidad_total
        self.lista_carpetas = lista_carpetas
        self.tipo_unidad = tipo_unidad
        
    def mostrar(self):
        print(f"ID: {self.id}, Nombre: {self.nombre}, Capacidad total: {self.capacidad_total}, Espacio disponible: {self.espacio_disponible}, Tipo de unidad: {self.tipo_unidad}")

class Comando:
    def __init__(self, id, nombre_comando, descripcion, rol_requerido):
        self.id = id
        self.nombre_comando = nombre_comando
        self.descripcion = descripcion
        self.rol_requerido = rol_requerido
