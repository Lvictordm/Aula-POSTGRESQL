import psycopg2 as pg
from dotenv import load_dotenv
import os

#Carregar variaveis do .env
params={
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWoRD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_IMPORT"),
    
    
}
def conectar():
    try:
        conexao = pg.connect(**params)
        cursor = conexao.cursor()
        return conexao, cursor
    except Exception as erro:
            print(f"Erro de conexão {erro}")
            return None, None