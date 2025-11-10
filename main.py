from flask import Flask
import os
import platform
import psutil

app = Flask(__name__)

@app.route('/')
def info():
    # nome fixo
    nome = "Guilherme"

    #obter PID do processo atual
    pid = os.getpid()

    # Obter informações do processo
    processo = psutil.Process(pid)
    memoria_mb = processo.memory_info().rss / (1024 * 1024)  # em MB
    cpu_percent = processo.cpu_percent(interval=0.1)  # uso de CPU %

    # sistema operacional
    sistema_operacional = platform.system()

    html = f"""
    <html>
        <head><title>Informações do Servidor</title></head>
        <body style="font-family: Arial; background-color: #f0f0f0; padding: 20px;">
            <h1>Servidor Flask - Informações</h1>
            <p><b>Nome:</b> {nome}</p>
            <p><b>PID do processo:</b> {pid}</p>
            <p><b>Memória utilizada:</b> {memoria_mb:.2f} MB</p>
            <p><b>Uso de CPU:</b> {cpu_percent:.2f}%</p>
            <p><b>Sistema operacional:</b> {sistema_operacional}</p>
        </body>
    </html>
    """
    return html

if __name__ == '__main__':
    # e xecuta o servidor
    app.run(host='0.0.0.0', port=5000, debug=True)
