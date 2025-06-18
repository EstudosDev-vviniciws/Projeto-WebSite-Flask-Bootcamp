from flask import Flask, render_template, jsonify

app = Flask(__name__)

VAGAS = [
    {
        'id': 1,
        'titulo': 'Analista de Dados',
        'localidade': 'MG, Brasil',
        'salario': 'R$ 4.700'    
    },
    
    {
        'id': 2,
        'titulo': 'Engenheiro de Software',
        'localidade': 'SP, Brasil',
        'salario': 'R$ 3.700'
    },
    
    {
        'id': 3,
        'titulo': 'Desenvolvedor Front-End',
        'localidade': 'MG, Brasil',
        'salario': 'R$ 3.000'
    },
    
    {
        'id': 4,
        'titulo': 'Desenvolvedor Back-End',
        'localidade': 'MG, Brasil',
        'salario': 'R$ 4.200'
    },
    
    {
        'id': 5,
        'titulo': 'Desenvolvedor Full-Stack',
        'localidade': 'RJ, Brasil',
        'salario': 'R$ 5.200'
    }
]

@app.route('/')
def hello():
    return render_template("home.html", vagas=VAGAS)

@app.route('/vagas')
def lista_vagas():
    return jsonify(VAGAS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)