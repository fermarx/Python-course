import math
import shutil
from pathlib import Path
from os import walk
import re
from datetime import date
import time

base = Path.home()
path = Path(base, "OneDrive", "Documentos", "curso_python", "dia9", "project", "Mi_Gran_Directorio")

"""
shutil.unpack_archive("Proyecto+Dia+9.zip", path, "zip")
"""

match = "[N][A-z]{3}[-]\d{5}"
fecha = date.today()
n_encontrados = 0

print(f"""----------------------------------------------------
Fecha de búsqueda: [{fecha.day}/{fecha.month}/{fecha.year}]

ARCHIVO\t\tNRO. SERIE
-------\t\t----------""")

ini = time.time()
for directory, subdirectories, files in walk(path):
    partial_path = Path(path, directory) 

    for file in files:
        final_path = Path(partial_path, file)         
        pf = open(final_path)
        read = pf.read()
        if re.search(match, read):
            for matches in re.findall(match, read):
                print(f"{file}\t{matches}")
                n_encontrados += 1

        pf.close()
end = time.time()

print(f"""
Números encontrados: {n_encontrados}
Duración de la búsqueda: {math.ceil(end-ini)} segundos
----------------------------------------------------
""")