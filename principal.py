from funciones import Funciones
import algoritmos
import time

# Carga de datos
data = Funciones.obtener_data()

# Variable para almacenar el usuario actual
usuario_actual = 0

# Función para el login
def login():
    print('LOGIN')
    nombre = input('Introduzca el Nombre de Usuario: ')
    contraseña = input('Introduzca su Contraseña: ')
    global usuario_actual

    # Validación de usuario administrador
    if (nombre == 'admin' and contraseña == 'admin'):
        usuario_actual = 1
        menu_principal()
        return 

    # Validación de usuarios estándar
    elif (nombre in data["usuarios"].keys()):
        if (data["usuarios"][nombre] == {'rol': 2, 'contrasena': contraseña}):
            usuario_actual = 2
            menu_principal()
            return
        elif (data["usuarios"][nombre] == {'rol': 1, 'contrasena': contraseña}):
            usuario_actual = 1
            menu_principal()
            return
    
    # Mensaje de acceso denegado
    else:
        print('Acceso denegado')
        time.sleep(1)
        login()
        return

# Función para el menú principal
def menu_principal():
    print('MENU PRINCIPAL')
    print('Introduzca una de las siguientes opciones: ')
    print('1. Crear Usuario')
    print('2. Gestión de Ficheros y Carpetas')
    print('3. Resetear Datos')
    print('4. Crear')
    print('5. Listar')
    print('6. Cargar Datos de Prueba')
    print('7. Salir')
    
    opcion = int(input())

    # Opciones del menú
    if opcion == 1:
        menu_crear_usuario()
    elif opcion == 2:
        menu_gestion_ficheros()
    elif opcion == 3:
        data = {"usuarios": {},"ficheros": {}, "unidades": {},"carpetas": {}}
        Funciones.guardar_data(data)
    elif opcion == 4:
        menu_crear()
    elif opcion == 5:
        menu_listar()
    elif opcion == 6:
        cargar_data()
    elif opcion == 7:
        exit()

    # Regresar al menú principal
    menu_principal()
  
# Función para crear un usuario
def menu_crear_usuario():

    # Validación de permisos de administrador
    if usuario_actual != 1:
        print('Acceso denegado. Necesita Usuario Administrador')
        time.sleep(1)
        menu_principal()
        return

    print('MENU CREAR USUARIO')
    print('Introduzca el Rol del Usuario: ')
    print('1. Administrador')
    print('2. Usuario Estandar')
    print('3. Regresar')

    opcion_rol = int(input())

    # Opciones de rol
    if opcion_rol == 3:
        menu_principal()
        return
  
    nombre_usuario = input('Introduzca el Nombre del Usuario: ')

    # Validación de nombre de usuario único
    if nombre_usuario in data["usuarios"]:
        print('El usuario ya existe')
        menu_crear_usuario()
        return

    contraseña_usuario = input('Introduzca la Contraseña del Usuario: ')

    # Agregar el nuevo usuario a la lista de usuarios
    data["usuarios"][nombre_usuario] = {'rol': opcion_rol, 'contrasena': contraseña_usuario}

    # Guardar los datos actualizados
    Funciones.guardar_data(data)

    # Mensaje de éxito

    print('Usuario Creado con exito')

def menu_gestion_ficheros():
    print('MENU GESTIÓN DE FICHEROS Y CARPETAS')
    print('Introduzca una de las siguientes opciones: ')
    print('1. Listar ficheros y carpetas ordenados por tamaño')
    print('2. Mostrar  ficheros  y  carpetas  en  orden  de  fecha  de  última  modificación')
    print('3. Buscar ficheros o carpetas por rango de tamaño y extensión')
    print('4. Listar todos los ficheros y carpetas que sean mayores o menores que un tamaño específico dado por el usuario')
    print('5. Ordenar por fecha de creación carpetas y ficheros según una ubicación de forma')
    print('6. Regresar')

    opcion = int(input())

    if opcion == 1:
        menu_gestion_uno()
    elif opcion == 2:
        menu_gestion_dos()
    elif opcion == 3:
        menu_gestion_tres()
    elif opcion == 4:
        menu_gestion_cuatro()
    elif opcion == 5:
        menu_gestion_cinco()    
    elif opcion == 6:
        menu_principal()

def menu_crear_fichero():

    if usuario_actual != 1:
        print('Acceso denegado. Necesita Usuario Administrador')
        time.sleep(1)
        menu_principal()
        return

    if len(data["carpetas"]) == 0:
        print('No hay Carpetas creadas')
        time.sleep(1)
        menu_crear()
        return
    
    id = input('Introduzca el ID del Fichero: ')

    if id in data["ficheros"].keys():
        print('El Fichero ya existe')
        time.sleep(1)
        menu_crear()
        return

    id_carpeta = input('Introduzca el ID de la Carpeta: ')

    if id_carpeta not in data["carpetas"]:
        print('La Carpeta no existe')
        time.sleep(1)
        menu_crear()
        return

    nombre = input('Introduzca el Nombre del Fichero: ')
    extension = input('Introduzca la Extensión del Fichero: ')
    tamaño = input('Introduzca el Tamaño del Fichero: ')
    fecha_creacion = input('Introduzca la Fecha de Creación del Fichero: ')
    fecha_modificacion = input('Introduzca la Fecha de Modificación del Fichero: ')
    contenido = input('Introduzca el Contenido del Fichero: ')

    data["ficheros"][id] = {'nombre': nombre, 'extension': extension, 'tamaño': tamaño, 'fecha_creacion': fecha_creacion, 'fecha_modificacion': fecha_modificacion, 'contenido': contenido}

    data["carpetas"][id_carpeta]["lista_ficheros"].append(id)

    Funciones.guardar_data(data)

def menu_crear_carpeta():

    if usuario_actual != 1:
        print('Acceso denegado. Necesita Usuario Administrador')
        time.sleep(1)
        menu_principal()
        return

    if len(data["unidades"]) == 0:
        print('No hay Unidades de Almacenamiento creadas')
        time.sleep(1)
        menu_crear()
        return

    id = input('Introduzca el ID de la Carpeta: ')

    if id in data["carpetas"].keys():
        print('La Carpeta ya existe')
        time.sleep(1)
        menu_crear()
        return
    
    id_unidad = input('Introduzca el ID de la Unidad de Almacenamiento: ')

    if id_unidad not in data["unidades"].keys():
        print('La Unidad de Almacenamiento no existe')
        time.sleep(1)
        menu_crear()
        return

    nombre = input('Introduzca el Nombre de la Carpeta: ')
    fecha_creacion = input('Introduzca la Fecha de Creación de la Carpeta: ')
    tamano_total = input('Introduzca el Tamaño Total de la Carpeta: ')

    data["carpetas"][id] = {'nombre': nombre, 'fecha_creacion': fecha_creacion, 'tamano_total': tamano_total, 'lista_ficheros': [], 'lista_carpetas': []}

    data["unidades"][id_unidad]["lista_carpetas"].append(id)

    Funciones.guardar_data(data)

def menu_crear_unidad():
    
    if usuario_actual != 1:
        print('Acceso denegado. Necesita Usuario Administrador')
        time.sleep(1)
        menu_principal()
        return

    id = input('Introduzca el ID de la Unidad de Almacenamiento: ')

    if id in data["unidades"].keys():
        print('La Unidad de Almacenamiento ya existe')
        time.sleep(1)
        menu_crear()
        return

    nombre = input('Introduzca el Nombre de la Unidad de Almacenamiento: ')
    capacidad_total = input('Introduzca la Capacidad Total de la Unidad de Almacenamiento: ')
    tipo_unidad = input('Introduzca el Tipo de Unidad de Almacenamiento: ')

    data["unidades"][id] = {'nombre': nombre, 'capacidad_total': capacidad_total, 'espacio_disponible': capacidad_total, 'lista_carpetas': [], 'tipo_unidad': tipo_unidad}

    Funciones.guardar_data(data)

def menu_listar_ficheros():
    for llave, valor in data["ficheros"].items():
        print(llave, ":", str(valor).replace("'", "").replace("{", "").replace("}", ""))

def menu_listar_carpetas():
    for llave, valor in data["carpetas"].items():
        print(llave, ":", str(valor).replace("'", "").replace("{", "").replace("}", ""))

def menu_listar_unidades():
    for llave, valor in data["unidades"].items():
        print(llave, ":", str(valor).replace("'", "").replace("{", "").replace("}", ""))

def menu_crear():
    print('1. Crear Fichero')
    print('2. Crear Carpeta')
    print('3. Crear Unidad de Almacenamiento')
    print('4. Regresar')

    opcion = int(input('Introduzca una de las opciones: '))

    if opcion == 1:
        menu_crear_fichero()
    elif opcion == 2:
        menu_crear_carpeta()
    elif opcion == 3:
        menu_crear_unidad()
    elif opcion == 4:
        menu_principal()

def menu_listar():
    print('1. Listar Ficheros')
    print('2. Listar Carpetas')
    print('3. Listar Unidades de Almacenamiento')

    opcion = int(input('Introduzca una de las opciones: '))

    if opcion == 1:
        menu_listar_ficheros()
    elif opcion == 2:
        menu_listar_carpetas()
    elif opcion == 3:
        menu_listar_unidades()
    elif opcion == 4:
        menu_principal()

def menu_gestion_uno():
    print('MENU GESTIÓN EJERCICIO 1')
    print('1. Ordenar de Forma Ascendente')
    print('2. Ordenar de Forma Descendente')
    print('3. Regresar')
    
    opcion = int(input('Introduzca una de las opciones: '))

    #Listar ficheros y carpetas ordenados por tamaño
    tamaños = []
    for llave, valor in data["ficheros"].items():
        tamaños.append(int(valor["tamaño"]))
    for llave, valor in data["carpetas"].items():
        tamaños.append(int(valor["tamano_total"]))

    n = len(tamaños)
    if opcion == 1:
        algoritmos.quick_sort(tamaños, 0, n-1)
    elif opcion == 2:
        algoritmos.quick_sort(tamaños, 0, n-1)
        tamaños.reverse()
    elif opcion == 3:
        menu_principal()
        return
    else:
        menu_principal()
        return


    for tamano in tamaños:
        for llave, valor in data["ficheros"].items():
            if int(valor["tamaño"]) == tamano:
                print(llave, ":", str(valor).replace("'", "").replace("{", "").replace("}", ""))
        for llave, valor in data["carpetas"].items():
            if int(valor["tamano_total"]) == tamano:
                print(llave, ":", str(valor).replace("'", "").replace("{", "").replace("}", ""))


def menu_gestion_dos():
    print('MENU GESTIÓN EJERCICIO 2')
    print('1. Ordenar de Forma Ascendente')
    print('2. Ordenar de Forma Descendente')
    print('3. Regresar')
    
    opcion = int(input('Introduzca una de las opciones: '))

    if opcion == 3:
        menu_principal()
        return
    
    menu_listar_carpetas()
    menu_listar_ficheros()

def menu_gestion_tres():
    print("MENU GESTION EJERCICIO 4")

    limite_inferior_rango = int(input("Ingresar el Límite Inferior del Rango: "))
    limite_superior_rango = int(input("Ingresar el Límite Superior del Rango: "))
    extension = input("Ingresa la extensión: ")

    for llave, valor in data["ficheros"].items():
        if int(valor["tamaño"]) > limite_inferior_rango and int(valor["tamaño"]) < limite_superior_rango:
            if extension != "":
                if extension == valor["extension"]:
                    print(llave, ":", str(valor).replace("'", "").replace("{", "").replace("}", ""))
            else:
                print(llave, ":", str(valor).replace("'", "").replace("{", "").replace("}", ""))

 
def menu_gestion_cuatro():
    pass

def menu_gestion_cinco():
    pass

def cargar_data():
    Funciones.cargar_data_prueba()

if __name__ == '__main__':
    login() 