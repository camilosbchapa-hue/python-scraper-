# Intalamos Librerias Ter pip install requests beautifulsoup4 pandas openpyxl matplotlib #

# Importamos Librerias #
import requests 
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

# Conectar Con la web y verificar si la conexion fue exitosa #
url = "https://books.toscrape.com/"

# Entramos a la pagina y traemos todo el contenido: #
response = requests.get(url)

""" response.status_code → es el código de respuesta del servidor:
200 → conexión exitosa ✅
404 → página no encontrada ❌
403 → acceso denegado ❌ """
print(response.status_code)

# Convertimos Pagina Web En Simbolos Python #
soup = BeautifulSoup(response.text, "html.parser")
print(soup.title)

# Buscar todos los libros en la pagina y contar cuantos encontro#
libros = soup.find_all("article", class_="product_pod")
print(len(libros))

# Recorremos Cada Libro, extraer su titulo y precio los guarda en una lista y los convierte en una tabla organizada # 
datos = []
for libro in libros:
    titulo = libro.find("h3").find("a")["title"]
    precio = libro.find("p", class_="price_color").text
    datos.append({"Titulo": titulo, "Precio": precio})
df = pd.DataFrame(datos)
print(df)



# Convertir Precio de texto a numero: #
df["Precio"] = df["Precio"].str.encode("ascii", "ignore").str.decode("ascii").str.strip().astype(float)

# Guarda toda la tabla de pandas en un archivo excel #
df.to_excel("PrimerEjemplo.xlsx", index=False)
print("¡Archivo Excel Creado Con Exito!")

# Creacion De grafica #

plt.figure(figsize=(12, 6))
plt.barh(df["Titulo"], df["Precio"], color="steelblue")
plt.xlabel("Precio en £")
plt.title("Precios de Libros - books.toscrape.com")
plt.tight_layout()
plt.show()




import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

datos = []

for pagina in range(1, 51):
    url = f"https://books.toscrape.com/catalogue/page-{pagina}.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    libros = soup.find_all("article", class_="product_pod")
    
    for libro in libros:
        titulo = libro.find("h3").find("a")["title"]
        precio = libro.find("p", class_="price_color").text
        datos.append({"Titulo": titulo, "Precio": precio})

df = pd.DataFrame(datos)
df["Precio"] = df["Precio"].str.encode("ascii", "ignore").str.decode("ascii").str.strip().astype(float)
df.to_excel("libros.xlsx", index=False)
print(f"Total de libros: {len(df)}")
plt.figure(figsize=(12, 6))
plt.hist(df["Precio"], bins=20, color="steelblue")
plt.xlabel("Precio en £")
plt.ylabel("Cantidad de libros")
plt.title("Distribución de Precios - 1000 Libros")
plt.tight_layout()
plt.show()



#Logica


#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("¿Quieres saber si eres mayor de edad?")
age=int(input("Ingresa tu edad porfavor: "))
if age >= 18 : 
    print("Eres mayor de edad")
else:
    print("No eres mayor de edad")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("Bienvenido al sistema de ingreso login de maxima seguridad")
enter_the_pasword=input("Ingresa la contraseña: ")
enter= enter_the_pasword.lower()
password="Contraseña"
pasword= password.lower()
if enter ==  pasword:
    print(" Acceso Correcto, Bienvenido ")
else:
    print("Acceso denegado, Intenta de nuevo ")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("Bienvenido al Programa dividiendo con Cami ;) ")
n1=int(input("Para Comenzar Ingresa Primer digito: "))
n2=int(input("Ahora ingresa tu digito 2 a dividir: "))
if n2 == 0 :
    print(" Error en la division ")
else:
    n4= n1/n2
    print(f"Tu division es: {n4}")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("Vamos a revisar si tu numero es par o impar list@?")
number=int(input("Para Comenzar ingresa tu numero yo hare la revision por ti ;)"))
if number % 2 == 0:
    print("par")
else:
    print("impar")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("Es usted un declarante itrubutario ? Vamos a averiguarlo")
age=int(input("Para Comenzar ingrese su edad: "))
income=float(input("Ahora ingrese sus ingresos mensuales Totales: "))
if age >16 and income >=1000:
    print ("Es usted declarante Tributario")
else:
    print("No es usted declarante") 
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("Empezaremos a definir a que seccion del salon perteneces")
sex=input("Ingresa porfavor que sexo eres M para masculino o F para femenino: ").upper()
name=input("Cuales es tu nombre?: ").upper()
if sex == "F"  and name[0] < "M":
    print("Eres Del grupo A")
elif sex == "M" and name[0] >"N":
    print("perteneces al grupo A")
else: 
    print(" Eres del grupo B") 
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("Programa diseñado para la declaracion de renta, sabes usted que porcentaje le corresponde y si debe de pagar algo ?")
print(" Vamos a ello. ")
income=float(input("Para Comenzar ingrese su monto de dinero recibido por año."))
if  income <= 9999:
    print("Es una persona que deba de clarar, su impuesto por el dinero resivido al año es del 5%") 
elif 10000 <= income < 19999:
    print("Es una persona que deba de clarar, su impuesto por el dinero resivido al año es del 15%")
elif 20000 <= income <34999:
    print("Es una persona que deba de clarar, su impuesto por el dinero resivido al año es del 20%")
elif 35000 <= income <= 60000:
    print("Es una persona que deba de clarar, su impuesto por el dinero resivido al año es del 30%")
else:
    print("Es una persona que deba de clarar, su impuesto por el dinero resivido al año es del 45%")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("Sistema de calificacion para sus empleados Por Dinero ")
employee=input("Para empezar ingrese el nombre de su empleado: ")
level=float(input("Ahora ingresa la puntuacion de su epmleado: "))
money= level * 2400
if level == 0.0:
    print(f" Su Dinero bajo la calificacion a recibir es de: {money}{employee} ")
elif level == 0.4:
    print(f" Su Dinero bajo la calificacion a recibir es de: {money}{employee} ")
elif level >= 0.6:
    print(f" Su Dinero bajo la calificacion a recibir es de: {money}{employee} ")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print(" ¡Hola! Bienvenido a Go Cars Interactive Models Cars")
age=int(input("El precio de la entrada varia por edad, para empezar ingresa tu edad porfavor: "))
if age < 4:
    print(" Su Hijo no pagara entrada ")
elif age <= 17: 
    print(" Su entrada tiene un costo de 5$ cancele su entrada en los modulos en la sa 304. ")
elif age >= 18:
    print("Usted es mayor de edad por lo tanto su entrada tiene un costo de 10$ cancele en los modulos de la sala 304. ")
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("Pizzeria Vegeans, Estamos a sus ordenes con pizzas calientes y deliciosas.")
vegetarian=input("¿Deseas ver las pizzas vegetarianas?").upper()
if vegetarian == ("S"):
    print("Ingredientes: Pimiento Y Tofu.")
    ingredient=input("Elige Uno de los dos Como Adicional: ")
else:
    print("Entonces seleccionaste el menu carnivoro.")
    print("Ingredientes: Peperoni, Jamon y Salmon.")
    ingredient=input("Eliege Uno de los 3 Ingredientes Como Adicional: ")
print(f"Su Pizza Esta en proceso de preparacion tu pizza lleva: Mozzarella y tomate, tu ingrediente adicional es: {ingredient}")

nombre = "Kevin Camilo Chaparro Ramirez"
edad = 26
print(f"Hola, mi nombre es {nombre} y tengo {edad}")

#2
number = int(input("Introduce un numero porfavor: "))
if number > 0:
    print("Positivo")
elif number < 0:
    print("Negativo")
else:
    print("Cero")
#3
for i in range (1, 11):
    print(f"{i}")
    if i % 2 == 0:
        print("par")
    else:
        print("impar")
#4
productos = ["Mouse", "Teclado", "Monitor", "Audifonos"]
for i in productos:
    if i == "Mouse":
        print(f"Su Producto es {i}")
#5
ventas = [2000, 1500, 3000, 1000]
a = int(ventas[0])
b = int(ventas[1])
c = int(ventas[2])
d = int(ventas[3])
suma = a + b + c + d

print(f"{suma}")



