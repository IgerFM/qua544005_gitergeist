#SECTION - Bibliotecas
from flask import Flask, render_template, request
import pyautogui as auto
from datetime import date
#NOTE - Para este programa usaremos o "pip install Flask pyautogui"
#!SECTION

app = Flask(__name__)

def abrir_terminal(repositorio):
    auto.hotkey('win','r')
    auto.write('cmd')
    auto.press('enter')
    auto.write(f'cd {repositorio}')
    auto.press('enter')

def commitar(hoje):
    auto.write(f'git add . && git commit -m "{hoje} | Auto-Commit (PC Senai)" && git push origin main')
    auto.press('enter')
    auto.sleep(8)
    auto.write('exit')
    auto.press('enter')

#SECTION - Rotas
@app.route("/", methods = ['GET','POST'])
def index():
    hoje = date.today().strftime("%y%m%d")
    repositorio = None
    if request.method == 'POST':
        repositorio = request.form.get('repositorio','')
        auto.PAUSE = 1
        abrir_terminal(repositorio)
        commitar(hoje)
    return render_template("index.html") #!SECTION

#SECTION - Runner
if __name__ == "__main__":
    app.run(debug=True) #!SECTION