from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # URL del archivo
    url = "https://gist.githubusercontent.com/reroes/502d11c95f1f8a17d300ece914464c57/raw/872172ebb60e22e95baf8f50e2472551f49311ff/gistfile1.txt"
    response = requests.get(url)
    contenido = response.text

    # Construimos el HTML
    tabla_html = "<h1>Personas con ID iniciando en 3, 4, 5 o 7</h1>"
    tabla_html += "<table border='1' cellpadding='5' cellspacing='0'>"
    tabla_html += "<tr><th>ID</th><th>Nombre</th><th>Apellido</th></tr>"

    lineas = contenido.strip().split('\n')
    for linea in lineas:
        partes = linea.strip().split('|')
        if len(partes) >= 3:
            id_persona = partes[0]
            if id_persona.startswith(('3', '4', '5', '7')):
                id_val = partes[0]
                nombre = partes[1]
                apellido = partes[2]
                tabla_html += f"<tr><td>{id_val}</td><td>{nombre}</td><td>{apellido}</td></tr>"

    tabla_html += "</table>"
    return tabla_html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
