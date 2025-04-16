from flask import Flask
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # Leer archivo desde URL con requests
    url = "https://gist.githubusercontent.com/reroes/502d11c95f1f8a17d300ece914464c57/raw/872172ebb60e22e95baf8f50e2472551f49311ff/gistfile1.txt"
    response = requests.get(url)
    contenido = response.text.splitlines()  # Lista de líneas del archivo

    # Filtrar las personas cuyo ID empieza con 3, 4, 5 o 7
    ids_validos = ('3', '4', '5', '7')
    personas = [linea.split(';') for linea in contenido if linea.startswith(ids_validos)]

    # Construir tabla HTML
    tabla_html = """
    <h2>Personas filtradas (ID empieza con 3, 4, 5 o 7)</h2>
    <table border="1" cellpadding="5" cellspacing="0">
        <tr><th>ID</th><th>Nombre</th><th>Apellido</th><th>Correo</th></tr>
    """

    for persona in personas:
        tabla_html += f"<tr><td>{persona[0]}</td><td>{persona[1]}</td><td>{persona[2]}</td><td>{persona[3]}</td></tr>"

    tabla_html += "</table>"

    return tabla_html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
