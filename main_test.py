#import de packages 
from flask import Flask
import subprocess

#affichage web
app = Flask(__name__)

@app.route ('/')
def hello():
    #envoi de la commande 
    ipmachine = subprocess.check_output("ip a",shell=True)
    web = '<html><body><h1>site test pour le test</h1><pre>{}</pre></body></html>'.format(ipmachine.decode("utf-8"))
    return web

if __name__ == '__main__':
    app.run() 