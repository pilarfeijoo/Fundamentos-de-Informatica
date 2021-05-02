#cada cebada de mate consume del 30 ml de agua. Cosntruí una función que nos permita calcular cuántos
#termos de 1000 ml llenos consumiremos para un ronda dada 
#(es decir una cantidad de personas dada).


def cant_termos(personas):
    termo = personas * 30 / 100
    if termo < 1:
        return print("Necesitas " + str(1) + " termo")
    if termo - int(termo) < 0.50:
        return print("Necesitas " + str(round(termo) + 1) + " termos")
    if  termo - int(termo) >= 0.50:
        return print("Necesitas " + str(round(termo)) + " termos")


cant_termos(7)

