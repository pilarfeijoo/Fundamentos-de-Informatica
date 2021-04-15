#2 Ejercicio 2 Realizar un programa donde se imprima la 5ta y 6ta letra de un string pasado por teclado en mayúscula (Asegurarse de que el string tenga la cantidad de caracteres suficientes).
string = input("Ingrese una palabra de minimo 6 letras:")
if len(string) >= 6:
    string_mayus = string.upper()
    print(string_mayus[4]) #5ta posicion
    print(string_mayus[5]) #6ta posicion
else:
    string2 = input("Ingrese una palabra con por lo menos 6 letras:")
    string2_mayus = string2.upper()
    print(string2_mayus[4]) #5ta posicion
    print(string2_mayus[5]) #6ta posicion