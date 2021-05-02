

pedido = { "Ana" : "no veggie", "Paul": "veganas", "Luz": "veganas"}
print(pedido["Ana"])

lista_comensales = pedido.keys()
print(str(lista_comensales) + "\n")



def empanadas_por_gusto(lista_pedidos):
   for i in lista_comensales:
     print(lista_pedidos[i])

empanadas_por_gusto(pedido)


def empanadas_por_gusto1(lista_pedidos):
  veggies = 0
  no_veggies = 0
  for i in lista_comensales:
    if lista_pedidos[i] == "veganas":
      veggies += 1
    else:
      no_veggies += 1
  return print("Veganas: "+ str(veggies) + "\nNo veganas: "+ str(no_veggies))


empanadas_por_gusto1(pedido)