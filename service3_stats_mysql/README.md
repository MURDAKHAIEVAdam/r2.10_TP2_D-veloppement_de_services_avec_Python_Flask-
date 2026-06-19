# Service 3 – Statistiques sur Base de Données
 
## Description
 
API REST Flask pour effectuer des calculs de statistiques descriptives et de corrélations sur des séries de données issues d'une base MySQL.
 
## Installation
 
```bash
cd service3_statistiques
python -m venv venv
source venv/Scripts/activate # Sur Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
 
## Architecture du code
 
- **app.py** : Contient le serveur Flask et la définition des routes API (Statistiques et Corrélations).
- **db.py** : Gère la connexion à la base de données MySQL locale et la récupération (fetch) des séries.
- **test_app.py** : Regroupe l'ensemble des tests unitaires automatisés avec pytest pour valider les routes et la gestion des erreurs.
## Routes disponibles
 
### GET /db/stats/describe
 
Calcule les statistiques descriptives d'une série spécifiée (moyenne, médiane, écart-type, minimum, maximum).
 
**Paramètres URL (Query Parameters) :**
 
- `serie` : Nom de la série de données à analyser (ex: `serie_A`).
**Exemple de requête :**
 
```
GET http://localhost:5003/db/stats/describe?serie=serie_A
```
 
**Réponse (200 OK) :**
 
```json
{
  "source": "mysql",
  "resultat": {
    "serie": "serie_A",
    "n": 5,
    "moyenne": 14.14,
    "mediane": 13.2,
    "ecart_type": 4.5159,
    "minimum": 8.7,
    "maximum": 21.0
  }
}
```
 
**Erreurs possibles :**
 
- `400 Bad Request` si le paramètre `serie` est manquant.
- `404 Not Found` si la série n'existe pas dans la base de données.
### GET /db/stats/correlation
 
Calcule le coefficient de corrélation de Pearson et la p-value entre deux séries distinctes.
 
**Paramètres URL (Query Parameters) :**
 
- `serie_x` : Nom de la première série (ex: `serie_A`).
- `serie_y` : Nom de la deuxième série (ex: `serie_B`).
**Exemple de requête :**
 
```
GET http://localhost:5003/db/stats/correlation?serie_x=serie_A&serie_y=serie_B
```
 
**Réponse (200 OK) :**
 
```json
{
  "source": "mysql",
  "series": {
    "x": "serie_A",
    "y": "serie_B",
    "n_points": 5
  },
  "resultat": {
    "r": 0.8742,
    "p_value": 0.0526,
    "significatif": false
  }
}
```
 
**Erreurs possibles :**
 
- `400 Bad Request` si l'un des deux paramètres (ou les deux) est manquant.
- `404 Not Found` si l'une des séries est introuvable en base.
## Exécution des Tests Unitaires
 
Pour lancer la suite de tests automatisés et vérifier la robustesse des routes :
 
```bash
pytest test_app.py
```