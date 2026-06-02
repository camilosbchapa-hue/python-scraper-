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

# Guarda toda la tabla de pandas en un archivo excel #
df.to_excel("libros.xlsx", index=False)
print("¡Archivo Excel Creado Con Exito!")

# Convertir Precio de texto a numero: #
df["Precio"] = df["Precio"].str.encode("ascii", "ignore").str.decode("ascii").str.strip().astype(float)
# Creacion De grafica #

plt.figure(figsize=(12, 6))
plt.barh(df["Titulo"], df["Precio"], color="steelblue")
plt.xlabel("Precio en £")
plt.title("Precios de Libros - books.toscrape.com")
plt.tight_layout()
plt.show()













