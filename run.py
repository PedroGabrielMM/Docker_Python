from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Olá, estou na aplicação setada!'

# Para rodar a aplicação é necessário rodar o comando abaixo:
# flask --app run.py run
