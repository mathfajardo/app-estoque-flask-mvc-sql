from flask import render_template, redirect, request, url_for
from models.produtos import Produto

def configure_routes(app):
    @app.route("/")
    def index():
        produtos = Produto.get_produtos()
        return render_template("index.html", produtos=produtos)

    @app.route("/contact")
    def contact():
        return render_template("contact.html")

    @app.route("/produtos/new", methods=["POST", "GET"])
    def criar_produto():
        nome = request.form["nome"]
        quantidade = request.form["quantidade"]
        categoria = request.form["categoria"]

        Produto.adicionar_produto(nome, quantidade, categoria)
        return redirect(url_for('index'))
    
    @app.route("/remover/<int:id>", methods=["POST", "GET"])
    def remover_produto(id):
        Produto.remover_produto(id)
        return redirect(url_for('index'))
        