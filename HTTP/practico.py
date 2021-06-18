import requests
r = requests.get('https://macowins-server.herokuapp.com/prendas/1')
r.json()

#DESAFIO I
m = requests.get('https://macowins-server.herokuapp.com/prendas/20')
m.json()

# Desafío II
t = requests.get('https://macowins-server.herokuapp.com/prendas/400')
t.json()

a = requests.get('https://macowins-server.herokuapp.com/prendas/1')
a.json()

# status code: me da el codigo de estado, 400 significa que no fue encontrado y 200 signi]fica que fue encontrado

#Desafío IV
a = requests.get(' https://macowins-server.herokuapp.com/prindas/1')
a.json()

#me da error 404 not found

#¿es lo mismo consultar /prendas/ que /prendas/1? 
# ¿En qué se diferencian? ¿Qué ocurre si hacemos r.content? ¿Por qué?
#no es lo mismo ya que con /prendas me da todas las prendas y con /prendas 1 solo las de 1
#r.content me devuelve el contenido de todas las prendas

#Para pensar: ¿qué hará /ventas/2? ¿/ventas/?.
#/ventas/2 me devuelve solo la venta numero 2 y /ventas me devouelve todas.

#Desafío V

j = requests.get('https://macowins-server.herokuapp.com/ventas')
j.json()

n = requests.get('https://macowins-server.herokuapp.com/ventas/2')
n.json()

#Desafío VII
w = requests.get('https://macowins-server.herokuapp.com/prendas?tipo=remera&talle=XS')
w.json()

#Desafío VIII
#decí usando tus palabras qué significa la URI de este ejemplo cerebral
#cerebro://recuerdos:3403/recientes#hoy?tema=http
#se observan los recuerdos cerebrales de hoy en esta URI

#Para pensar: ¿Qué ocurrirá si hacemos un pedido a un dominio inexistente? ¿Qué código de estado HTTP obtendremos?
#esto nos dara un error ya que no existe

#Para pensar: ¿por qué Google tiene múltiples IPs?
#¿Que ventaja representa para esta empresa y para quienes lo usamos?
#Tiene varios IPs para que no se trabe ya que muchas personas estan conectadas a la misma vez. Esto es una ventaja para los que utilizan google y tambien para la empresa.

#Desafío IX;
#¿a través de qué IP accedés a google desde tu computadora?
# por la interfaz de mi red de internet

#Para pensar: ¿Cuál fue el Content-Type de las respuesta del ejemplo?


#content-type: 'application/json'

#Desafío X: ¿Qué devolverá la página principal (home) de nuestro sitio?
# Averiguá el Content-Type de /home
i = requests.get('https://macowins-server.herokuapp.com/home')
i.headers
#'Content-Type': 'text/html

#Desafío XII
data = {'id': 21}
r = requests.post('https://macowins-server.herokuapp.com/prendas/', data=data)
r.headers

#codigo de estado 201

#Para pensar: ¿por qué es importante respetar estas convenciones?
#para que no nos confundamos

#Desafío XV: ¿cuales de los siguientes sitios tiene (o parecen tener, al menos) rutas REST?
# Github --> pertence
# Youtube --> no pertenece
# Facebook --> si pertenece
# Infobae, Pagina12, La Nacion --> si pertenece
# UNQ, UCEMA --> si pertenece

#Desafío XVI: si no se organizan de forma REST, ¿cómo se organizan sus rutas?
#por el id 

