#import de packages 
from flask import Flask, render_template
import subprocess

class test: 
    def __init__(self,numero,object,status):
        self.numero = numero
        self.object = object
        self.status = status

#affichage web
app = Flask(__name__)

@app.route ('/')
def hello():
    #envoi de la commande 
    ipmachine = subprocess.check_output([''],shell=True)
    web = '<html><body><h1>site test pour le test</h1><pre>{}</pre></body></html>'.format(ipmachine.decode("utf-8"))
    return web

if __name__ == '__main__':
    app.run() 