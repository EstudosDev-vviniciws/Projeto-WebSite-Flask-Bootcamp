from flask import Flask, render_template, jsonify, request
from database import carrega_vagas_db, carrega_vaga_db, adiciona_incricao

app = Flask(__name__)

@app.route('/')
def home():
    vagas1 = carrega_vagas_db()
    return render_template("home.html", vagas=vagas1)

@app.route('/vagas')
def lista_vagas():
    vagas1 = carrega_vagas_db()
    return jsonify(vagas1)

@app.route('/vaga/<id>')
def mostra_vaga(id):
        vaga1 = carrega_vaga_db(id)
        if not vaga1:
            return "Not Found", 404
        return render_template("detalhevaga.html", vaga=vaga1)
    
@app.route('/vaga/<id>/inscricao', methods=["GET", "POST"])
def incricao_vaga(id):
    vaga1 = carrega_vaga_db(id)
    data = request.form
    adiciona_incricao(id, data)
    return render_template("inscricao_concluida.html", vaga=vaga1, inscricao=data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)