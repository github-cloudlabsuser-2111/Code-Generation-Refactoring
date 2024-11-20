import requests

def obtener_datos_climaticos(ciudad, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"
    respuesta = requests.get(url)
    
    if respuesta.status_code == 200:
        datos = respuesta.json()
        temperatura = datos['main']['temp']
        humedad = datos['main']['humidity']
        condiciones = datos['weather'][0]['description']
        return temperatura, humedad, condiciones
    else:
        return None, None, None

def main():
    ciudad = input("Ingresa el nombre de la ciudad: ")
    api_key = "1cc13a675aba124a4ffee3506f124af5"  # Reemplaza con tu API key de OpenWeatherMap

    temperatura, humedad, condiciones = obtener_datos_climaticos(ciudad, api_key)

    if temperatura is not None:
        print(f"Temperatura: {temperatura}°C")
        print(f"Humedad: {humedad}%")
        print(f"Condiciones del clima: {condiciones}")
    else:
        print("No se pudieron obtener los datos climáticos. Verifica el nombre de la ciudad y tu API key.")

if __name__ == "__main__":
    main()