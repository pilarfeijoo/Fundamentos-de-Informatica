#Creá un programa que lea una cadena por teclado y compruebe si la primer letra es mayúscula o minúscula.

cadena = input ("Dame una palabra:")
def es_mayus(palabra):
    if palabra[0] >= "A" and palabra[0] <="Z":
        print("es minuscula")
    elif palabra[0] >= "A" and palabra[0] <= "Z":
        print("es mayuscula")

es_mayus(cadena)