# Image source
FROM python

# Récupération des dépenances de mon projet
COPY Requirements.txt Requirements.txt

# Installer mes dépendances
RUN pip install -r Requirements.txt

# Ajout de mon application Flask
COPY app.py app.py

# Ouvrir le port 
EXPOSE 9001

# Démarrer mon application
CMD ["python", "app.py"]

# Création de l'image via le dockerFile -> docker build -t monappflask .

# Lancement du conteneur avec cette image -> docker run -dit --name testmonapp -p 9001:9001 monappflask