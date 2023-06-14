#import de packages 
from flask import Flask, render_template
import subprocess

class Test: 
    def __init__(self,numero,object,status,validation):
        self.numero = numero
        self.object = object
        self.status = status
        self.validation = validation

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
                if 'OK' in line_split[1]:
                    dict['validation'] = "validé"
                elif 'CRITICAL' in line_split[1]:
                    dict['validation'] = "non validé"
                elif 'Error' in line_split[1]:
                    dict['validation'] = "non validé"
                else :
                    dict['validation'] = "non concluant"

            case 3 :
                dict['resultat attendue'] = line_split[0]
                dict['resultat '] = line_split[1]
                if 'OK' in line_split[1]:
                    dict['validation'] = "validé"
                elif 'CRITICAL' in line_split[1]:
                    dict['validation'] = "non validé"
                elif 'Error' in line_split[1]:
                    dict['validation'] = "non validé"
                else :
                    dict['validation'] = "non concluant"

                dict['detaille'] = line_split[2]
            case 4 :
                dict['resultat attendue'] = line_split[0]
                dict['resultat '] = line_split[1]
                
                if 'OK' in line_split[1]:
                    dict['validation'] = "validé"
                elif 'CRITICAL' in line_split[1]:
                    dict['validation'] = "non validé"
                elif 'Error' in line_split[1]:
                    dict['validation'] = "non validé"
                else :
                    dict['validation'] = "non concluant"
                
                dict['detaille'] = line_split[2] + line_split[3]
        
        tests.append(Test(dict['resultat attendue'],dict['resultat '],dict['detaille'],dict['validation']))
    
    return render_template('index.html',tests=tests)
file.close()
if __name__ == '__main__':
    app.run(debug=True) 