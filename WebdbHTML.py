

from flask import Flask,request,jsonify

import mysql.connector


#configuro la connessione
mydb = mysql.connector.connect(
    host="localhost",
    user='root',
    password ='Coletti_1',
    database ='pythonaprile'
)



app = Flask(__name__)


miaconnessione = mydb.cursor()



@app.route("/")
def Generale():
    #return "ciao"
    return "<h1>Sono il primo tag ricevuto dal server</h1>"

def leggiDati():
    stringaSQL ="select * from computer"

    miaconnessione.execute(stringaSQL)

    return miaconnessione.fetchall()
    

@app.route("/api/utenti", methods=['GET'])
def chiamatGET():

    return jsonify(leggiDati())


@app.route("/api/utenti", methods=['POST'])
def chiamataPOST():
    #print(request.get_json())
    nuovo=request.get_json()
    stringaSQL = f"insert into computer (ram,hd,processore) values ({nuovo['ram']},{nuovo['hd']},'{nuovo['processore']}')"
    miaconnessione.execute(stringaSQL)
    mydb.commit()

    return jsonify(leggiDati())

@app.route("/api/utenti", methods=['PUT'])
def chiamataPUT():
    nuovo=request.get_json()
    
    stringaSQL = f"update computer set ram={nuovo['ram']},processore='{nuovo['processore']}', hd={nuovo['hd']} where idcomputer ={nuovo['idaggiorna']}"
    miaconnessione.execute(stringaSQL)
    mydb.commit()
    return jsonify(leggiDati())


@app.route("/api/utenti", methods=['DELETE'])
def chiamataDELETE():
    cancella=request.get_json()["idcancella"]
    stringa =f"delete from computer where idcomputer ={cancella}"
    miaconnessione.execute(stringa)
    mydb.commit()
    return jsonify(leggiDati())


if __name__== '__main__':
    app.run()
