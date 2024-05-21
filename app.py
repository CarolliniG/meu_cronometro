from flask import Flask, render_template
import time

app = Flask(__name__)

class Cronometro:
    def __init__(self):
        self.tempo_inicial = 0
        self.tempo_final = 0
        self.tempo_total = 0
        self.rodando = False

    def iniciar(self):
        if not self.rodando:
            self.tempo_inicial = time.time()
            self.rodando = True
            print("Cronômetro iniciado.")

    def parar(self):
        if self.rodando:
            self.tempo_final = time.time()
            self.tempo_total += self.tempo_final - self.tempo_inicial
            self.rodando = False
            print(f"Cronômetro parado. Tempo total: {self.tempo_total:.2f} segundos.")

    def reiniciar(self):
        self.tempo_inicial = 0
        self.tempo_final = 0
        self.tempo_total = 0
        self.rodando = False
        print("Cronômetro reiniciado.")

    def tempo_decorrido(self):
        if self.rodando:
            tempo_atual = time.time()
            tempo_decorrido = self.tempo_total + (tempo_atual - self.tempo_inicial)
        else:
            tempo_decorrido = self.tempo_total
        print(f"Tempo decorrido: {tempo_decorrido:.2f} segundos.")
        return tempo_decorrido

cronometro = Cronometro()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start():
    cronometro.iniciar()
    return '', 204

@app.route('/stop')
def stop():
    cronometro.parar()
    return '', 204

@app.route('/reset')
def reset():
    cronometro.reiniciar()
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)

