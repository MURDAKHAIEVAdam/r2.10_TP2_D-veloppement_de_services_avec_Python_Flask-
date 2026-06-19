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
 
**Commande de test (cURL Windows/PowerShell) :**
 
```bash
curl.exe -X GET "http://localhost:5003/db/stats/describe?serie=serie_A"
```
 
**Réponse (200 OK) :**
 
```json
{
    "resultat": {
        "ecart_type": 4.5159,
        "maximum": 21.0,
        "mediane": 13.2,
        "minimum": 8.7,
        "moyenne": 14.14,
        "n": 5,
        "serie": "serie_A"
    },
    "source": "mysql"
}
```
 
**Codes de statut :**
 
- `200 OK` : Succès.
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
 
**Commande de test (cURL Windows/PowerShell) :**
 
```bash
curl.exe -X GET "http://localhost:5003/db/stats/correlation?serie_x=serie_A&serie_y=serie_B"
```
 
**Réponse (200 OK) :**
 
```json
{
    "resultat": {
        "p_value": 0.221189,
        "r": 0.7788,
        "significatif": false
    },
    "series": {
        "n_points": 4,
        "x": "serie_A",
        "y": "serie_B"
    },
    "source": "mysql"
}
```
 
**Codes de statut :**
 
- `200 OK` : Succès.
- `400 Bad Request` si l'un des deux paramètres (ou les deux) est manquant.
- `404 Not Found` si l'une des séries est introuvable en base.
## Page de test (HTML/CSS)
 
Une page de test statique (HTML/CSS/JS) est disponible pour interroger les routes sans passer par cURL ou Postman. Une fois le serveur Flask lancé (`python app.py`), ouvrez le fichier de test dans votre navigateur, puis renseignez l'URL du service (par défaut `http://localhost:5003`) dans le champ prévu.
 
Cette page permet de :
 
- Tester chaque route individuellement (`describe` et `correlation`) via des boutons dédiés.
- Modifier les paramètres (`serie`, `serie_x`, `serie_y`) directement dans les champs de saisie.
- Lancer tous les exemples en une seule fois avec le bouton **Tester toutes les routes**.
- Copier l'URL générée pour chaque requête.
- Visualiser le code de statut HTTP et la réponse JSON brute pour chaque test.
## Exécution des Tests Unitaires
 
Pour lancer la suite de tests automatisés et vérifier la robustesse des routes :
 
```bash
pytest test_app.py
```