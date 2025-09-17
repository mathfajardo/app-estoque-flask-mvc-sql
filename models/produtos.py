import mysql.connector
from config import db_config

# função para realizar configuração
def inicia_db():
    conn = mysql.connector.connect(**db_config)
    return conn

class Produto:
    @staticmethod
    def get_produtos():
        produtos = []
        conn = inicia_db()
        if conn:
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT * FROM estoque_braga.produtos")
            produtos = cursor.fetchall()
            cursor.close()
            conn.close()
        return produtos
    
    @staticmethod
    def adicionar_produto(nome, quantidade, categoria):
        conn = inicia_db()
        if conn:
            cursor = conn.cursor()
            query = "INSERT INTO estoque_braga.produtos (nome, quantidade, categoria) VALUES (%s, %s, %s)"
            cursor.execute(query, (nome, quantidade, categoria))
            conn.commit()
            cursor.close()
            conn.close()

    @staticmethod
    def remover_produto(id):
        conn = inicia_db()
        if conn:
            cursor = conn.cursor()
            query = "DELETE FROM estoque_braga.produtos WHERE id = %s"
            cursor.execute(query, (id,))
            conn.commit()
            cursor.close()
            conn.close()