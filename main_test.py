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
file = open('check.txt',mode = 'r', encoding='utf-8-sig')
lines = file.readlines()

@app.route ('/')
def index():
    #ouverture du fichier check.txt
    
    dict = {}
    tests = []
    line_split = []
    #envoi de la commande 
    for line in lines:
        
        line_split = line.split('-')
        line_split = [j.strip() for j in line_split]
        length = len(line_split)
        match length:
            case 1 :
                dict['resultat attendue'] = line_split[0]
            case 2 :
                dict['resultat attendue'] = line_split[0]
                dict['resultat '] = line_split[1]
            case 3 :
                dict['resultat attendue'] = line_split[0]
                dict['resultat '] = line_split[1]
                dict['detaille'] = line_split[2]
            case 4 :
                dict['resultat attendue'] = line_split[0]
                dict['resultat '] = line_split[1]
                dict['detaille'] = line_split[2]
        
        tests.append(Test(dict['resultat attendue'],dict['resultat '],dict['detaille']))
    
    return render_template('index.html',tests=tests)
file.close()
if __name__ == '__main__':
    app.run(debug=True) 