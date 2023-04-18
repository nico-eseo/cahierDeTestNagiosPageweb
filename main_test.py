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
    #envoi de la commande 
    tests = [
        Test(1,"nagios http","pass"),
        Test(2,"nagios ssh","pass"),
        Test(3,"nagios cpu","pass"),
        Test(4,"nagios disk","failed")
    ]
    return render_template('index.html',tests=tests)

if __name__ == '__main__':
    app.run(debug=True) 