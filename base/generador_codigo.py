import random as r


def generar_codigo():
    cadena = ""
    abc = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(10):
        a = r.choice(abc)
        cadena += a
    return cadena
