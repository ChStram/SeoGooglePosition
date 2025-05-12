# Suivi de position Google via SerpAPI

Ce script permet d'automatiser la récupération des positions d'un site web sur Google pour une liste de mots-clés, en utilisant l'API SerpAPI

## Prérequis

- Python 3.x
- Un compte SerpAPI : [https://serpapi.com/](https://serpapi.com/) (gratuit)
- Une clé API SerpAPI valide

Installation des dépendances :

```bash
pip install requests
```

## Configuration

1. **Créer le fichier `config.json`** en partant de l'exemple config.json.example
2. **Modifier le fichier** :

   - `keywords` : Liste des mots-clés à analyser.
   - `domain` : Le nom de domaine à suivre (ex: `monsite.fr`).
   - `api_key` : Votre clé API SerpAPI.
   - `csv_filename` : Nom du fichier de sortie (ex: `resultats.csv`).

Exemple :

```json
{
  "keywords": [
    "mot clé 1",
    "mot clé 2",
    "mot clé 3"
  ],
  "domain": "monsite.fr",
  "api_key": "cle_api_serpapi",
  "csv_filename": "resultats.csv"
}
```

## Exécution

Lancer le script avec Python :

```bash
python script.py
```

Le fichier CSV avec les résultats sera généré à la fin à la racine du dossier.
