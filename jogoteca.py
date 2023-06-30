from flask import Flask, render_template, request, redirect

app = Flask(__name__)


class Jogo:

  def __init__(self, nome, categoria, console):
    self.nome = nome
    self.categoria = categoria
    self.console = console


jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Hack n Slash', 'PS2')
lista = [jogo1, jogo2]


@app.route('/')
def hello():
  return render_template('lista.html', titulo='Jogos', jogos=lista)


@app.route('/hello')
def say_hello():
  return ('<h1 style=color:red;font-size:70px;margin-left:70px>Olá</h1>')


@app.route('/novo')
def novo():
  return render_template('novo.html', titulo="Novo Jogo")


@app.route('/criar', methods=[
  'POST',
])
def criar():
  nome = request.form['nome']
  categoria = request.form['categoria']
  console = request.form['console']
  jogo = Jogo(nome, categoria, console)

  lista.append(jogo)
  return redirect('/')


app.run(host='0.0.0.0', debug=True)
