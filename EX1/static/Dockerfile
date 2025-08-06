 # 1. Image de départ avec Python déjà installé
 FROM python:3.11-slim
 # 2. Dossier de travail dans le conteneur
 WORKDIR /app
 # 3. Copier le fichier des dépendances
 COPY requirements.txt .
 # 4. Installer les dépendances Python
 RUN pip install -r requirements.txt
 # 5. Copier tout le code de l'application
 COPY . .
 # 6. Port que l'app utilise
 EXPOSE 5000
 # 7. Lancer l'application
 CMD ["python", "app.py"]