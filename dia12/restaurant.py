from tkinter import *
import random
import datetime
from tkinter import filedialog
from tkinter import messagebox

operador = ""
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_dessert = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)

def borrar():
    global operador 
    operador = ""
    visor_calculadora.delete(0, END)

def obtener_res():
    global operador
    res = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, res)
    operador = ""

def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get()==1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0, END)
                cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set("0")
        x+=1

    x = 0
    for c in cuadros_bebida:
        if variables_bebida[x].get()==1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0,END)
                cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set("0")
        x+=1

    x = 0
    for c in cuadros_dessert:
        if variables_dessert[x].get()==1:
            cuadros_dessert[x].config(state=NORMAL)
            if cuadros_dessert[x].get() == '0':
                cuadros_dessert[x].delete(0,END)
                cuadros_dessert[x].focus()
        else:
            cuadros_dessert[x].config(state=DISABLED)
            texto_dessert[x].set("0")
        x+=1

def total():
    sub_total_comida = 0
    p = 0
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[p])
        p+=1
    
    sub_total_bebida = 0
    p = 0
    for cantidad in texto_bebida:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[p])
        p+=1

    sub_total_dessert = 0
    p = 0
    for cantidad in texto_dessert:
        sub_total_dessert = sub_total_dessert + (float(cantidad.get()) * precios_dessert[p])
        p+=1

    sub_total = sub_total_bebida + sub_total_comida + sub_total_dessert
    impuestos = sub_total * 0.7
    total = impuestos + sub_total

    var_costo_comida.set(f"${round(sub_total_comida, 2)}")
    var_costo_bebida.set(f"${round(sub_total_bebida, 2)}")
    var_costo_dessert.set(f"${round(sub_total_dessert, 2)}")
    var_subtotal.set(f"${round(sub_total, 2)}")
    var_impuesto.set(f"${round(impuestos, 2)}")
    var_total.set(f"${round(total, 2)}")

def save():
    info_archivo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    archivo.write(info_archivo)
    archivo.close()
    messagebox.showinfo("Informacion", "Su recibo ha sido guardado")

def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f"N# - {random.randint(1000,1999)}"
    fecha = datetime.datetime.now()
    fecha_recibo = f"{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}"
    texto_recibo.insert(END, f"Datos:\t{num_recibo}\t\t{fecha_recibo}\n")
    texto_recibo.insert(END, f"*" * 63 + "\n")
    texto_recibo.insert(END, "Items\t\tCant.\tCosto Items\n")
    texto_recibo.insert(END, f"-" * 75 + "\n")
    
    total()

    x=0
    for comida in texto_comida:
        if comida.get() != "0":
            texto_recibo.insert(END, f"{lista_comidas[x]}\t\t{comida.get()}\t"
                                    f"$ {int(comida.get()) * precios_comida[x]}\n")
        x += 1

    x=0
    for bebida in texto_bebida:
        if bebida.get() != "0":
            texto_recibo.insert(END, f"{lista_bebidas[x]}\t\t{bebida.get()}\t"
                                    f"$ {int(bebida.get()) * precios_bebida[x]}\n")
        x += 1

    x=0
    for dessert in texto_dessert:
        if dessert.get() != "0":
            texto_recibo.insert(END, f"{lista_dessert[x]}\t\t{dessert.get()}\t"
                                    f"$ {int(dessert.get()) * precios_dessert[x]}\n")
        x += 1

    texto_recibo.insert(END, f"-" * 75 + "\n")
    texto_recibo.insert(END, f"Costo de la comida: \t\t\t{var_costo_comida.get()}\n")
    texto_recibo.insert(END, f"Costo de la bebida: \t\t\t{var_costo_bebida.get()}\n")
    texto_recibo.insert(END, f"Costo de postres: \t\t\t{var_costo_dessert.get()}\n")

    texto_recibo.insert(END, f"-" * 75 + "\n")
    texto_recibo.insert(END, f"Subtotal: \t\t\t{var_subtotal.get()}\n")
    texto_recibo.insert(END, f"Impuestos: \t\t\t{var_impuesto.get()}\n")
    texto_recibo.insert(END, f"Total: \t\t\t{var_total.get()}\n")
    
    texto_recibo.insert(END, f"*" * 63 + "\n")
    texto_recibo.insert(END, f"Lo esperamos pronto")

def reset():
    texto_recibo.delete(0.1, END)

    for texto in texto_comida:
        texto.set("0")
    for texto in texto_bebida:
        texto.set("0")
    for texto in texto_dessert:
        texto.set("0")

    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_dessert:
        cuadro.config(state=DISABLED)

    for v in variables_comida:
        v.set(0)
    for v in variables_bebida:
        v.set(0)
    for v in variables_dessert:
        v.set(0)

    var_costo_comida.set("")
    var_costo_bebida.set("")
    var_costo_dessert.set("")
    var_subtotal.set("")
    var_impuesto.set("")
    var_total.set("")


# init tkinter
app = Tk()
# window size
app.geometry("950x600+0+0")
# no maximize
app.resizable(0, 0)

# window title 
app.title("Restaurant")
# bg color
app.config(bg="burlywood")

# superior frame
panel_superior = Frame(app, bd=1, relief=RAISED)
panel_superior.pack(side=TOP)
# title
etiqueta_titulo = Label(panel_superior, text="Facturacion", fg="azure4", 
                    font=("dosis,58"), bg="burlywood", width=27)
etiqueta_titulo.grid(row=0, column=0)

# panel izquierdo
panel_izquierdo = Frame(app, bd=1, relief=FLAT)
panel_izquierdo.pack(side=LEFT)
# panel costos
panel_cosotos = Frame(panel_izquierdo, bd=1, relief=FLAT, bg="azure4")
panel_cosotos.pack(side=BOTTOM)
# panel comidas
panel_comidas = LabelFrame(panel_izquierdo, text="Food", font=("Dosis", 19, "bold"),
                            bd=1, relief=FLAT, fg="azure4")
panel_comidas.pack(side=LEFT)
# panel bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text="Drinks", font=("Dosis", 19, "bold"),
                            bd=1, relief=FLAT, fg="azure4")
panel_bebidas.pack(side=LEFT)
# panel postres
panel_postres = LabelFrame(panel_izquierdo, text="Desserts", font=("Dosis", 19, "bold"),
                            bd=1, relief=FLAT, fg="azure4")
panel_postres.pack(side=LEFT)

# panel derecha
panel_derecha = Frame(app, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)
# panel calculadora
panel_calculadora = Frame(panel_derecha, bd=1, relief=FLAT, bg="burlywood")
panel_calculadora.pack()
# panel recibo
panel_recibo = Frame(panel_derecha, bd=1, relief=FLAT, bg="burlywood")
panel_recibo.pack()
# panel buttons
panel_button = Frame(panel_derecha, bd=1, relief=FLAT, bg="burlywood")
panel_button.pack()


# lista productos
lista_comidas = ["chicken", "lamb", "salmon", "hake", "kebab", "pizza1", "pizza2", "pizza3"]
lista_bebidas = ["water", "juice", "coke", "pepsi", "wine", "wine2", "beer", "beer2"]
lista_dessert = ["icecream", "cake", "cake2", "cheesecake", "fruit", "brownie", "mousse", "flan"]

cont = 0
variables_comida = []
cuadros_comida = []
texto_comida = []
for comida in lista_comidas:
    
    # checkbutton
    variables_comida.append("")
    variables_comida[cont] = IntVar()
    comida = Checkbutton(panel_comidas,text=comida.title(), font=("Dosis", 12, "bold"), 
                            onvalue=1, offvalue=0, variable=variables_comida[cont],
                            command=revisar_check)
    comida.grid(row=cont, column=0, sticky=W)

    # cuadro entrada
    cuadros_comida.append("")
    texto_comida.append("")
    texto_comida[cont] = StringVar()
    texto_comida[cont].set("0")
    cuadros_comida[cont] = Entry(panel_comidas, font=("Dosis", 18, "bold"), 
                                    bd=1, width=6, state=DISABLED, textvariable=texto_comida[cont])
    cuadros_comida[cont].grid(row=cont, column=1)
    
    cont+=1


cont = 0
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
for bebida in lista_bebidas:
    
    # checkbutton
    variables_bebida.append("")
    variables_bebida[cont] = IntVar()
    bebida = Checkbutton(panel_bebidas, text=bebida.title(), font=("Dosis", 12, "bold"), 
                            onvalue=1, offvalue=0, variable=variables_bebida[cont],
                            command=revisar_check)
    bebida.grid(row=cont, column=0, sticky=W)
    
    # cuadro entrada
    cuadros_bebida.append("")
    texto_bebida.append("")
    texto_bebida[cont] = StringVar()
    texto_bebida[cont].set("0")
    cuadros_bebida[cont] = Entry(panel_bebidas, font=("Dosis", 18, "bold"), 
                                    bd=1, width=6, state=DISABLED, textvariable=texto_bebida[cont])
    cuadros_bebida[cont].grid(row=cont, column=1)
    
    cont+=1

cont = 0
variables_dessert = []
cuadros_dessert = []
texto_dessert = []
for dessert in lista_dessert:
    
    # checkbutton
    variables_dessert.append("")
    variables_dessert[cont] = IntVar()
    dessert = Checkbutton(panel_postres, text=dessert.title(), font=("Dosis", 12, "bold"), 
                            onvalue=1, offvalue=0, variable=variables_dessert[cont],
                            command=revisar_check)
    dessert.grid(row=cont, column=0, sticky=W)
    
    # cuadro entrada
    cuadros_dessert.append("")
    texto_dessert.append("")
    texto_dessert[cont] = StringVar()
    texto_dessert[cont].set("0")
    cuadros_dessert[cont] = Entry(panel_postres, font=("Dosis", 18, "bold"), 
                                    bd=1, width=6, state=DISABLED, textvariable=texto_dessert[cont])
    cuadros_dessert[cont].grid(row=cont, column=1)
    
    cont+=1

# variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_dessert = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

# etiquetas costo y campos de entrada
etiqueta_costo_comida = Label(panel_cosotos, text="Food price", font=("Dosis", 12, "bold"),
                                bg="azure4", fg="white")
etiqueta_costo_comida.grid(row=0,column=0)

texto_costo_comida = Entry(panel_cosotos, font=("Dosis", 12, "bold"), bd=1,
                                width=10, state="readonly", textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1)


etiqueta_costo_bebida = Label(panel_cosotos, text="Drink price", font=("Dosis", 12, "bold"),
                                bg="azure4", fg="white")
etiqueta_costo_bebida.grid(row=1,column=0)

texto_costo_bebida = Entry(panel_cosotos, font=("Dosis", 12, "bold"), bd=1,
                                width=10, state="readonly", textvariable=var_costo_bebida)
texto_costo_bebida.grid(row=1, column=1)


etiqueta_costo_dessert = Label(panel_cosotos, text="Dessert price", font=("Dosis", 12, "bold"),
                                bg="azure4", fg="white")
etiqueta_costo_dessert.grid(row=2,column=0)

texto_costo_dessert = Entry(panel_cosotos, font=("Dosis", 12, "bold"), bd=1,
                                width=10, state="readonly", textvariable=var_costo_dessert)
texto_costo_dessert.grid(row=2, column=1)


etiqueta_subtotal = Label(panel_cosotos, text="Subtotal", font=("Dosis", 12, "bold"),
                                bg="azure4", fg="white")
etiqueta_subtotal.grid(row=0,column=2)

texto_subtotal = Entry(panel_cosotos, font=("Dosis", 12, "bold"), bd=1,
                                width=10, state="readonly", textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3)


etiqueta_impuesto = Label(panel_cosotos, text="Taxes", font=("Dosis", 12, "bold"),
                                bg="azure4", fg="white")
etiqueta_impuesto.grid(row=1,column=2)

texto_impuesto = Entry(panel_cosotos, font=("Dosis", 12, "bold"), bd=1,
                                width=10, state="readonly", textvariable=var_impuesto)
texto_impuesto.grid(row=1, column=3)


etiqueta_total = Label(panel_cosotos, text="Total", font=("Dosis", 12, "bold"),
                                bg="azure4", fg="white")
etiqueta_total.grid(row=2,column=2)

texto_total = Entry(panel_cosotos, font=("Dosis", 12, "bold"), bd=1,
                                width=10, state="readonly", textvariable=var_total)
texto_total.grid(row=2, column=3)


# botones
botones = ["total", "bill", "save", "reset"]
botones_creados = []
colum = 0

for boton in botones:
    boton = Button(panel_button, text=boton.title(), font=("Dosis", 12, "bold"),
                    fg="white", bg="azure4", bd=1, width=9)
    botones_creados.append(boton)
    boton.grid(row=0, column=colum)
    colum+=1
botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=save)
botones_creados[3].config(command=reset)

# area recibo
texto_recibo = Text(panel_recibo, font=("Dosis", 12, "bold"),bd=1,width=42, height=10)
texto_recibo.grid(row=0, column=0)

# calculadora
visor_calculadora = Entry(panel_calculadora, font=("Dosis", 12, "bold"), width=32, bd=1)
visor_calculadora.grid(row=0,column=0,columnspan=4)

buttons = ["7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "*", "CE", "Delete", "0", "/"]
botones_guardados = []
colum = 0
fila = 1
for button in buttons:
    button = Button(panel_calculadora, text=button.title(), font=("Dosis", 12, "bold"),
                    fg="white", bg="azure4", bd=1, width=8)
    button.grid(row=fila, column=colum)
    
    if colum == 3:
        fila+=1
    colum+=1
    if colum == 4:
        colum = 0

    botones_guardados.append(button)

botones_guardados[0].config(command=lambda: click_boton("7"))
botones_guardados[1].config(command=lambda: click_boton("8"))
botones_guardados[2].config(command=lambda: click_boton("9"))
botones_guardados[3].config(command=lambda: click_boton("+"))
botones_guardados[4].config(command=lambda: click_boton("4"))
botones_guardados[5].config(command=lambda: click_boton("5"))
botones_guardados[6].config(command=lambda: click_boton("6"))
botones_guardados[7].config(command=lambda: click_boton("-"))
botones_guardados[8].config(command=lambda: click_boton("1"))
botones_guardados[9].config(command=lambda: click_boton("2"))
botones_guardados[10].config(command=lambda: click_boton("3"))
botones_guardados[11].config(command=lambda: click_boton("*"))
botones_guardados[14].config(command=lambda: click_boton("0"))
botones_guardados[15].config(command=lambda: click_boton("/"))

botones_guardados[13].config(command=obtener_res)
botones_guardados[13].config(command=borrar)


# keep window open 
app.mainloop()
