from flask import Flask, jsonify
import os
import platform
import psutil

app = Flask(__name__)

@app.route('/')
def raiz():
    html = """
    <html>
        <head><title>Informações do Servidor</title></head>
        <body style="font-family: Arial; background-color: #f0f0f0; padding: 20px;">
            <h1>Servidor Flask - Página inicial</h1>
            <p><a href='/info'>Ver informações do integrante</a></p>
            <p><a href='/metrics'>Ver métricas do sistema (JSON)</a></p>
            <p>¿Pode ser que o batman esconda uma receita de bolo de maça?</p>
            <img src="/static/girl_pic.jpeg" alt="info" width="500" height="600">
        </body>
    </html>
    """
    return html


def conteudo():
    # Obter PID do processo atual
    pid = os.getpid()

    # Obter informações do processo
    processo = psutil.Process(pid)
    memoria_mb = processo.memory_info().rss / (1024 * 1024)  # em MB
    cpu_percent = processo.cpu_percent(interval=0.1)  # uso de CPU %

    # Sistema operacional
    sistema_operacional = platform.system()

    dados = {
        "pid": pid,
        "memoria_mb": round(memoria_mb, 2),
        "cpu_percent": round(cpu_percent, 2),
        "sistema_operacional": sistema_operacional
    }

    return jsonify(dados)


@app.route("/info")
def info():
    dicionario = {"Nome": "Guilherme Arcanjo de Morais"}

    return jsonify(dicionario)


@app.route("/metrics")
def metrics():
    return conteudo()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
