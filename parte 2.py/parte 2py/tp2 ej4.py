#Una compañía de transporte internacional tiene servicio en algunos países de América del Sur, América Central, América del Norte, Europa y Asia. El costo por el servicio de transporte se basa en el peso del paquete y la zona a la que va dirigido, tal como se muestra en la tabla:


gramos = int(input("ingrese el paso en gramos:")
zona = input("ingrese la zona:")
if gramos < 5000:
    if zona == "America del Sur":
       print(10 * gramos)
    elif zona == "America Central":
        print(10 * gramos)
    elif zona == "America del Norte":
        print(18 * gramos)
    elif zona == "Europa":
        print(18 * gramos)
    elif zona == "Asia":
        print(30 * gramos)
