import os
from dotenv import load_dotenv

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'Ad584atpceVGiAqN1kuSza2YusWJbyTmOgC9HUzA')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
