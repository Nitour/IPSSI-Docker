# Image légère
FROM python:3.11-slim

# Définir le dossier de travail
WORKDIR /app

# Optimisation des couches : installation des dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && \
    rm requirements.txt

# Ajout d’un utilisateur non-root pour la sécurité
RUN adduser --disabled-password --gecos '' appuser
USER appuser

# Copier le code source
COPY app.py .

# Exposer le port utilisé par Flask
EXPOSE 5000

# Lancer l'application
CMD ["python", "app.py"]
