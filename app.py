#SECTION - Bibliotecas
from flask import Flask, render_template, request
import pyautogui as auto
import webview

from datetime import date
import os
import sys
#NOTE - Para este programa usaremos o "pip install Flask pyautogui"
#NOTE - Tambem usamos o "pip install pywebview pyinstaller"
#!SECTION

#SECTION - Indexador
if getattr (sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)

else:
    app = Flask(__name__) #!SECTION

#SECTION - Abridor de terminal
def abrir_terminal(repositorio):
    auto.hotkey('win','r')
    auto.write('cmd')
    auto.press('enter')
    auto.write(f'cd {repositorio}')
    auto.press('enter') #!SECTION

#SECTION - Commitador
def commitar(hoje):
    auto.write(f'git add . && git commit -m "{hoje} | Auto-Commit (PC Senai)"')
    auto.press('enter')
    auto.write(f'git push origin main')
    auto.press('enter')
    auto.sleep(5)
    auto.write('exit')
    auto.press('enter') #!SECTION

#SECTION - Rotas
@app.route("/", methods = ['GET','POST'])
def index():
    hoje = date.today().strftime("%y/%m/%d")
    repositorio = None
    if request.method == 'POST':
        repositorio = request.form.get('repositorio','')
        auto.PAUSE = 1
        abrir_terminal(repositorio)
        commitar(hoje)
    return render_template("index.html") #!SECTION

#SECTION - Runner
if __name__ == "__main__": 
    window = webview.create_window(
        title="Gitergeist v2.0",
        url=app,
        width=1080,
        height=920,
    ) 

    webview.start()
    #!SECTION