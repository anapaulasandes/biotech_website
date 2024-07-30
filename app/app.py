from flask import Flask, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Conectar ao MongoDB
client = MongoClient('mongodb://mongo:27017/')
db = client['mydatabase']
collection = db['names']

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Receber o nome do formulário
        name = request.form.get('name')
        if name:
            # Salvar o nome no MongoDB
            collection.insert_one({'name': name})
            return 'Nome salvo com sucesso!'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
