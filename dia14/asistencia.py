import cv2
import face_recognition as fr
import os
import numpy
import pyttsx3
from datetime import datetime


# crear base de datos
ruta = "fotos/Empleados"
mis_imagenes = []
nombres_empleados = []
lista_empleados = os.listdir(ruta)

for nombre in lista_empleados:
    imagen_actual = cv2.imread(f"{ruta}/{nombre}")
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])


# codificar imagenes
def codificar(imagenes):
    # crear nueva lista
    lista_codificada = []

    # pasar todas las img a rgb
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

        # codificar
        codificado = fr.face_encodings(imagen)[0]

        #agregar a la lista
        lista_codificada.append(codificado)

    # devolver lista codificada
    return lista_codificada


def saludo_inicial(name):
    # crear variable con datos de hora
    hora = datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = "Good night" 
    elif 6 <= hora.hour < 13:
        momento = "Good morning"
    else:
        momento = "Good afternoon"

    # decir el saludo
    hablar(f"{momento} {name}.")


def hablar(mensaje):
    # encender el motor de pyttsx3
    engine = pyttsx3.init()
    # prununcia msje
    engine.say(mensaje)
    engine.runAndWait()


# registrar ingresos
def registrar_ingresos(persona):
    f = open("registro.csv", "r+")
    lista_datos = f.readlines()
    nombres_registro = []

    for linea in lista_datos:
        ingreso = linea.split(",")
        nombres_registro.append(ingreso[0])

    if persona not in nombres_registro:
        ahora = datetime.now()
        string_ahora = ahora.strftime("%H:%M:%S")
        f.writelines(f"\n{persona}, {string_ahora}")
    f.close()


lista_empleados_codificada = codificar(mis_imagenes)

# tomar imagen de camara web
captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)

#leer imagen de camara
exito, imagen = captura.read()
if not exito:
    hablar("Couldn't get the capture.")
else:
    # reconocer cara en captura
    cara_captura = fr.face_locations(imagen)
    if not cara_captura:
        hablar("No face detected.")

    # codificar cara capturada
    cara_capturada_codificada = fr.face_encodings(imagen, cara_captura)

    # buscar coincidencias
    for caracodif, caraubic in zip(cara_capturada_codificada, cara_captura):
        
        coincidencias = fr.compare_faces(lista_empleados_codificada, caracodif)
        distancias = fr.face_distance(lista_empleados_codificada, caracodif)
        
        indice_coincidencia = numpy.argmin(distancias)

        # mostrar coincidencias
        if distancias[indice_coincidencia] > 0.6:
            hablar("No coincidences in database.")
        else:
            # buscar el nombre del empleado enonctrado
            nombre = nombres_empleados[indice_coincidencia]
            
            y1, x2, y2, x1 = caraubic
            cv2.rectangle(imagen,
                          (x1, y1),
                          (x2, y2),
                          (0, 255, 0),
                          2)
            cv2.rectangle(imagen,
                          (x1, y2 - 35),
                          (x2, y2),
                          (0, 255, 0),
                          cv2.FILLED)
            cv2.putText(imagen, nombre, 
                        (x1 + 6, y2 - 6), 
                        cv2.FONT_HERSHEY_COMPLEX, 
                        1, 
                        (255, 255, 255), 
                        2)
            
            saludo_inicial(nombre)
            registrar_ingresos(nombre)

            # mostrar la imagen obtenida
            cv2.imshow("Captured image", imagen)

            # mantener la ventana abierta
            cv2.waitKey(0)