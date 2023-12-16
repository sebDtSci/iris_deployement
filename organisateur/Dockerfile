# Utiliser une image de base Python
FROM python:3.9

# Créer et utiliser un répertoire de travail
WORKDIR /app

# Installer les dépendances (si nécessaire)
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copier le script init.py
COPY init.py ./

# Définir la commande par défaut à exécuter
CMD ["python", "./init.py"]
