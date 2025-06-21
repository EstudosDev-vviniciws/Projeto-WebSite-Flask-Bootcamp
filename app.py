from flask import Flask, render_template, jsonify
from database import carrega_vagas_db

app = Flask(__name__)

@app.route('/')
def hello():
    vagas1 = carrega_vagas_db()
    return render_template("home.html", vagas=vagas1)

@app.route('/vagas')
def lista_vagas():
    vagas1 = carrega_vagas_db()
    return jsonify(vagas1)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)