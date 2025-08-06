# Image de base légère
FROM python:3.11-slim

RUN apt-get update && apt-get install -y gcc libmariadb-dev && rm -rf /var/lib/apt/lists/*

# Créer un répertoire de travail
WORKDIR /app


# Copier les fichiers de dépendances en premier (optimisation du cache)
COPY requirements.txt .
# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste de l'application
COPY . .

# Créer un utilisateur non-root
RUN adduser --disabled-password --gecos '' appuser
USER appuser

# Exposer le port 5000
EXPOSE 5000

# Lancer l’application
CMD ["python", "app.py"]