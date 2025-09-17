from flask import Flask
from controllers import produtos_controller

# criando rota principal
app = Flask(__name__, static_folder="views/static", template_folder="views/templates")

produtos_controller.configure_routes(app)

if __name__ == "__main__":
    app.run(debug=True)