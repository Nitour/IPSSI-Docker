from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Boutique Sécurisée</h1>
    <p><a href="/health">Vérifier la santé</a></p>
    <p><a href="/products">Voir les produits</a></p>
    """

@app.route('/health')
def health():
    try:
        conn = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user='root',
            password=os.getenv('DB_PASSWORD'),
            database='boutique'
        )
        conn.close()
        return jsonify({"status": "OK", "database": "connected"})
    except Exception as e:
        return jsonify({"status": "ERROR", "message": str(e)})

@app.route('/products')
def products():
    return jsonify([
        {"id": 1, "nom": "Laptop", "prix": 999.99},
        {"id": 2, "nom": "Souris", "prix": 25.50}
    ])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
