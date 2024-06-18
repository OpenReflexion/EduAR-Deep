# EduAR-Deep
EduAR-Deep est une application éducative révolutionnaire qui combine les technologies de réalité augmentée (AR) et de deep learning pour offrir une expérience d'apprentissage immersive et interactive. Conçu pour stimuler l'engagement et faciliter la compréhension, EduAR-Deep permet aux utilisateurs de visualiser des concepts complexes de manière intuitive et captivante.

## Caractéristiques

- **Réalité Augmentée** : Utilisez la réalité augmentée pour superposer des informations visuelles et interactives sur le monde réel, rendant l'apprentissage plus dynamique et intéressant.
- **Deep Learning** : Intégrez des modèles de deep learning pour personnaliser l'expérience d'apprentissage en fonction des besoins et des progrès de chaque utilisateur.
- **Interface Intuitive** : Une interface utilisateur simple et élégante qui rend l'application accessible à tous, des enfants aux adultes.
- **Large Gamme de Sujets** : Explorez une vaste bibliothèque de sujets éducatifs, allant des sciences naturelles aux mathématiques, en passant par l'histoire et la géographie.

## Structure du Projet
```
EduAR-Deep/
│
├── app/
│   ├── __init__.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── config.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── main_controller.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── image_model.py
│   ├── schema/
│   │   ├── __init__.py
│   │   └── create_db.py
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css
│   │   └── js/
│   │       └── main.js
│   ├── templates/
│   │   └── index.html
│   └── database.db
├── .env
├── run.py
├── requirements.txt
```

## Installation

### Prérequis

- Python 3.x
- Flask

### Instructions

1. Clonez le dépôt :
   ```sh
   git clone https://github.com/YourUsername/EduAR-Deep.git
   cd EduAR-Deep
   ```

2. Installez les paquets requis :
    ```sh
    pip install -r requirements.txt
    ```

3. Création du `.env` :
    ```sh
    cp .env.example .env
    ```

4. Lancez l'application :
    ```sh
    python run.py
    ```
5. Ouvrez votre navigateur et naviguez vers http://localhost:5000

# Contribution
Les contributions sont les bienvenues ! Veuillez soumettre une pull request ou ouvrir une issue pour toute modification ou amélioration.

# Licence
Ce projet est sous licence MIT.