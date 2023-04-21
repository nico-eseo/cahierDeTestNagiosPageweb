#import de packages 
from flask import Flask, render_template
import subprocess

class Test: 
    def __init__(self,numero,object,status):
        self.numero = numero
        self.object = object
        self.status = status

#affichage web
app = Flask(__name__)

@app.route ('/')
def index():
    #ouverture du fichier check.txt
    file = open('check.txt',mode = 'r', encoding='utf-8-sig')
    lines = file.readline()
    dict = {}
    tests = []
    #envoi de la commande 
    for line in lines:
        line = line.split('-')
            
        tests.append(Test(line,'test','test'))
    file.close()
    return render_template('index.html',tests=tests)

if __name__ == '__main__':
    app.run(debug=True) 