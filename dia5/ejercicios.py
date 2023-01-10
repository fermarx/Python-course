def describir_persona(nombre, **kwargs):
    
    string = ""
    
    for key,val in kwargs.items():
        string += f"{key}: {val}\n"
    
    return f"Características de {nombre}:\n" + string


print(describir_persona("tomás", color_ojos="azules", color_pelo="rubio"))