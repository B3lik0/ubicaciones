import requests
import json 

# puedes usar el estado que requieras, 
with open("yuc.json", "r") as f:
  # Leer el contenido del archivo y convertirlo en un diccionario de Python
  estados = json.load(f)

# Crear una lista vacía para guardar las ubicaciones GPS
ubicaciones = []
api_key=''
ubicaciones_json = {}
# Recorrer cada estado y cada municipio en el Json
for estado, municipios in estados.items():
  for municipio in municipios:
    # Construir la URL de la API de Google Maps con el nombre del municipio y el estado
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={municipio},{estado}&key={api_key}"
    respuesta = requests.get(url).json()
    latitud = respuesta["results"][0]["geometry"]["location"]["lat"]
    longitud = respuesta["results"][0]["geometry"]["location"]["lng"]
    ubicaciones_json[municipio] = (latitud, longitud)

with open("ubicaciones.json", "w") as f:
  json.dump(ubicaciones_json, f)

