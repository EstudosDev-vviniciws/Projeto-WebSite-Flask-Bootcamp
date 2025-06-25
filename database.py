from sqlalchemy import create_engine, text
import os
from dotenv import load_dotenv

load_dotenv()
string_conexao = os.getenv("DATABASE_URL")
engine = create_engine(
    string_conexao,
    connect_args={
        "ssl":{
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
)

def carrega_vagas_db():
    with engine.connect() as conn:
        resultado = conn.execute(text("SELECT * FROM vagas"))
        vagas = []
    for vaga in resultado.all():
        vagas.append(vaga._asdict())
    return vagas

def carrega_vaga_db(id):
    with engine.connect() as conn:
        resultado = conn.execute(text(f"SELECT * FROM vagas WHERE id = :value"), {"value": id})
        registro = resultado.mappings().all()
        if len(registro) == 0:
            return None
        else: 
            return dict(registro[0])
        
def adiciona_incricao(id_vaga, dados):
    with engine.begin() as conn:
        query = text(f"INSERT INTO incricoes(vaga_id, nome, email, linkedin, experiencia) VALUES (:vaga_id, :nome, :email, :linkedin, :experiencia)")
        conn.execute(query, {'vaga_id': id_vaga, 'nome': dados['nome'], 'email': dados['email'], 'linkedin': dados['linkedin'], 'experiencia': dados['experiencia']})
        