from tkinter import image_names
import bs4
import requests

# url sin numero
url_base = "http://books.toscrape.com/catalogue/page-{}.html"

# lista de libros 4 o 5 estrellas
titulo_libro = []

for n in range(1, 51):

    # crear sopa en cada pagina
    resultado = requests.get(url_base.format(n))
    sopa = bs4.BeautifulSoup(resultado.text, "lxml")

    # seleccion datos de libros
    libros = sopa.select(".product_pod")
    
    # iterar libros
    for libro in libros:
        # chequear estrellas
        if libro.select(".star-rating.Four")  or libro.select(".star-rating.Five"):
            # guardar titulo en variable
            titulo_libro.append(libro.select("a")[1]["title"])

print(titulo_libro)