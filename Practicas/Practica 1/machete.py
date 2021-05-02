
lista_periodos = [1,1,1]
print(len(lista_periodos))

ahorros = 8000
for i in lista_periodos:
    ahorros = ahorros + ((ahorros * (1+(.1))**i)-ahorros)
print(ahorros)



for i in range(0, 4):
    ahorros = 8000
    ahorros = ahorros + (((ahorros * (1+(.1))**i)-ahorros))
        
print(ahorros)


