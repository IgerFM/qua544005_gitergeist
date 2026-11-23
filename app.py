#SECTION - Bibliotecas
from flask import Flask, render_template, request
import pyautogui as auto
#NOTE - Para este programa usaremos o "pip install Flask pyautogui"
#!SECTION

app = Flask(__name__)

#SECTION - Rotas
@app.route("/")
def index():
    return render_template("index.html") #!SECTION

#SECTION - Runner
if __name__ == "__main__":
    app.run(debug=True) #!SECTION