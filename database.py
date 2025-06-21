from sqlalchemy import create_engine, text

string_conexao = "mysql+pymysql://root:Telefone225XX@localhost/python_talentos?charset=utf8mb4"
engine = create_engine(
    string_conexao,
    connect_args={
        "ssl":{
            "ssl_ca": "/etc/ssl/cert.pem"
        }
    }
)

with engine.connect() as conn:
    resultado = conn.execute(text("SELECT * FROM vagas"))
    
    resultado_dicionario = []
    for vaga in resultado.all():
        resultado_dicionario.append(vaga._asdict())
    
print(resultado_dicionario)