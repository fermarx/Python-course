import pyttsx3
import pywhatkit
import speech_recognition as sr
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


# escuchar micro y devolver audio como texto
def transormar_audio_en_texto():
    # almacenar recognizer
    r = sr.Recognizer()

    # configurar micro
    with sr.Microphone() as origen:
        # informar que comenzo la grabacion
        print("Now you can talk")

        # guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # buscar en google 
            pedido = r.recognize_google(audio, language="en-gb")

            # prueba de que pudo ingresar
            print("You said: " + pedido)

            #devolver pedido
            return pedido

        # en caso de que no comprenda
        except sr.UnknownValueError:
            # prueba de que no comprendio
            print("Oops! I didn't undestand")

            # devolver error
            return "I'm still waiting"

        # no resolver pedido
        except sr.RequestError:
            # prueba de que no comprendio
            print("Oops! There's no service")

            # devolver error
            return "I'm still waiting"

        # Error inesperado
        except:
            # prueba de que no comprendio
            print("Oops! Something went wrong")

            # devolver error
            return "I'm still waiting"


# funcion para que el asistente pueda ser escuchado
def hablar(mensaje):
    # encender el motor de pyttsx3
    engine = pyttsx3.init()
    #engine.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0")

    # prununcia msje
    engine.say(mensaje)
    engine.runAndWait()


# informar dia de la semana
def pedir_dia():
    # crear variable con datos de hoy
    dia = datetime.date.today()

    # crear variable para el dia de la semana
    dia_semana = dia.weekday()
    # diccionario con nombres de dias
    calendario = {0: "Monday",
                  1: "Tuesday",
                  2: "Wednesday",
                  3: "Thursday",
                  4: "Friday",
                  5: "Saturday",
                  6: "Sunday"}
    # decir el dia de la semana
    hablar(f"Today is {calendario[dia_semana]}")


# informar de la hora
def pedir_hora():
    # crear variable con datos hora
    hora = datetime.datetime.now()

    hora = f"At this moment, it is {hora.hour} hours, {hora.minute} minutes and {hora.second} seconds."

    # decir hora
    hablar(hora)


# saludo inicial
def saludo_inicial():

    # crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = "Good night" 
    elif 6 <= hora.hour < 13:
        momento = "Good morning"
    else:
        momento = "Good afternoon"

    # decir el saludo
    hablar(f"{momento}, I am Stephana, your personal assistant. Tell me how can I help you.")


# funcion central del asisitente
def pedir_cosas():
    # activar saludo inicial
    saludo_inicial()

    # variable de corte
    comenzar = True
    while comenzar:
        # activar micro y guardar en un string
        pedido = transormar_audio_en_texto().lower()

        if "open youtube" in pedido:
            hablar("Opening youtube")
            webbrowser.open("http://www.youtube.com")
            continue

        elif "open google" in pedido:
            hablar("Opening Google")
            webbrowser.open("http://www.google.com")
            continue

        elif "what is the date" in pedido:
            pedir_dia()
            continue

        elif "what time is it" in pedido:
            pedir_hora()
            continue

        elif "search on wikipedia" in pedido:
            pedido = pedido.replace("search on wikipedia", "")
            print(pedido)
            hablar(f"Okay, searching on wikipedia {pedido}")
            try:
                res = wikipedia.summary(pedido, sentences = 1)
                hablar(f"Wikipedia says: {res}")
                print(res)
            except:
                hablar("Sorry, that didn't work")
            continue

        elif "search in internet" in pedido: 
            hablar("Searching in internet")
            pedido = pedido.replace("search in internet", "")
            pywhatkit.search(pedido)
            hablar("This is what I found")
            continue

        elif "play" in pedido:
            hablar("Good idea")
            pywhatkit.playonyt(pedido)
            continue
    
        elif "joke" in pedido:
            hablar(pyjokes.get_joke("en"))
            continue
            
        elif "price of actions" in pedido:
            accion = pedido.split("of")[-1].strip()
            cartera = {"apple": "APPL",
                        "amazon": "AMZN",
                        "google": "GOOGL"}

            try: 
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info["regularMarketPrice"]
                hablar(f"I found that the price of {accion} is {precio_actual}")
                continue
            except:
                hablar("Sorry, I didn't find anything")

        elif "goodbye" in pedido:
            hablar("Goodbye, see you later.")
            break

pedir_cosas()