# Jeu de Dés - Simulation

## Description
Ce projet est une simulation interactive d'un jeu de dés. Le joueur peut lancer des dés, consulter ses scores, et configurer les paramètres du jeu. Le système est conçu en utilisant plusieurs **design patterns** (MVC, Singleton, Composite, etc.) et s'appuie sur des technologies modernes comme **Python**, **Streamlit**, et des bases de données (SQL, NoSQL, CSV)

## Fonctionnalités
- **Lancer des dés** : Le joueur peut lancer les dés et obtenir des points en fonction des règles
- **Consultation des meilleurs scores** : Les scores sont sauvegardés et peuvent être consultés depuis plusieurs bases de données
- **Configuration des paramètres** : Personnalisez le jeu, notamment le nombre de dés ou les stratégies de score
- **Affichage des règles** : Les règles du jeu sont disponibles dans une interface conviviale

## Technologies utilisées
- **Python** : Langage principal pour la logique et l'architecture du jeu
- **Streamlit** : Pour l'interface utilisateur interactive
- **MongoDB** : Base de données NoSQL pour stocker les scores
- **SQLite** : Base de données relationnelle pour la persistance des données
- **CSV** : Format de stockage simple et portable

## Installation
1. Clonez le dépôt :
   ```bash
   git clone https://github.com/votre-repo/jeu-de-des.git
   cd jeu-de-des

2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt

3. Lancez l'application Streamlit :
   ```bash
   streamlit run main.py

## Structure des fichiers
- **DiceSystem/** : Contient la logique principale du jeu (lancers, scores, etc.)
- **DicePersist/** : Gère la persistance des données (SQL, NoSQL, CSV)
- **DiceVisualisation/** : Interface utilisateur
- **RandomStyle/** : Sous-système pour la génération des résultats aléatoires

## Auters
Oleksandra KUKSA
Olha ALIEINIK
