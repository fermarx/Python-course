import re

def verificar_email(email):
    ver = r"\w+@\w+.com"
    
    print(re.search(ver, email))

    if re.search(ver, email) : print("Ok")
    
    else: print("La dirección de email es incorrecta")

verificar_email("@host.com")