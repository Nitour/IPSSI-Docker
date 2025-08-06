from flask import Flask, jsonify, render_template_string
import mysql.connector
import os

app = Flask(__name__)

# Template HTML simple
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Boutique E-commerce</title>
    <style>
        body { font-family: Arial; margin: 40px; }
        .product { border: 1px solid #ddd; padding: 10px; margin: 10px 0; }
    </style>
</head>
<body>
    <h1>Boutique E-commerce</h1>
    <p><a href="/health">Vérifier la santé</a> | <a href="/products">Voir les produits</a></p>
    <h2>Produits disponibles</h2>
    <div id="products">
        {% for product in products %}
        <div class="product">
            <h3>{{ product.nom }}</h3>
            <p>Prix: {{ product.prix }} euros</p>
            <p>{{ product.description }}</p>
        </div>
        {% endfor %}
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    try:
        conn = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM produits")
        products = cursor.fetchall()
        conn.close()
        return render_template_string(HTML_TEMPLATE, products=products)
    except Exception as e:
        return f"Erreur de connexion à la base : {e}"

@app.route('/health')
def health():
    try:
        conn = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM produits")
        count = cursor.fetchone()[0]
        conn.close()
        return jsonify({"status": "OK", "produits_count": count})
    except Exception as e:
        return jsonify({"status": "ERROR", "message": str(e)})

@app.route('/products')
def products_json():
    try:
        conn = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM produits")
        products = cursor.fetchall()
        conn.close()
        return jsonify(products)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
