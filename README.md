# TP2 - Developpement de services avec Python Flask

Projet realise dans le cadre du TP2 de R2.10 - Introduction a la gestion des systemes d'information.

Equipe :

- Adam Murdakhaiev
- Adrien Crepieux
- Minh-Tam Nguyen
- Lokman Eddahchouri

## Objectif du projet

Ce projet contient plusieurs services web developpes avec Flask. Chaque service expose une API REST dediee a une fonctionnalite precise :

- calculs sur des matrices ;
- calculs statistiques sur des donnees envoyees en JSON ;
- calculs statistiques a partir de donnees stockees dans MySQL ;
- import de fichiers CSV dans une base MySQL.

Les services sont independants et peuvent etre lances separement sur des ports differents.

## Technologies utilisees

- Python
- Flask
- NumPy
- SciPy
- Pandas
- MySQL
- mysql-connector-python
- python-dotenv

## Structure du projet

```text
TP2/
|-- README.md
|-- requirements.txt
|-- data/
|   `-- donnees_exemples.csv
|-- sql/
|   `-- init_db.sql
|-- service1_matrices/
|   |-- app.py
|   |-- matrices.py
|   |-- tester.html
|   |-- tests1.http
|   |-- requirements.txt
|   `-- README.md
|-- service2_statistiques/
|   |-- app.py
|   |-- test_api.py
|   |-- test_api_2.py
|   `-- README.md
|-- service3_stats_mysql/
|   |-- app.py
|   |-- db.py
|   |-- tester.html
|   |-- test_app.py
|   |-- requirements.txt
|   `-- README.md
`-- service4_csv_mysql/
    |-- app.py
    |-- donnees_exemples.csv
    |-- requirements.txt
    `-- README.md
```

## Prerequis

Avant de lancer le projet, il faut disposer de :

- Python 3 ;
- pip ;
- MySQL ;
- un environnement virtuel Python, recommande mais optionnel.

## Installation

Depuis la racine du projet, creer et activer un environnement virtuel :

```bash
python -m venv .venv
```

Sous Windows PowerShell :

```bash
.\.venv\Scripts\Activate.ps1
```

Installer les dependances necessaires :

```bash
pip install flask numpy scipy pandas mysql-connector-python python-dotenv
```

Certains services possedent aussi leur propre fichier `requirements.txt`.

Exemple :

```bash
cd service3_stats_mysql
pip install -r requirements.txt
```

## Configuration MySQL

Les services 3 et 4 utilisent une base de donnees MySQL.

Creer un fichier `.env` a la racine du projet, ou dans le dossier du service lance, avec les variables suivantes :

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=votre_mot_de_passe
DB_NAME=tp2_flask
```

Remarque : le service 3 lit `DB_PASSWORD`. Dans le service 4, la connexion actuelle utilise `DB_HOST`, `DB_USER`, `DB_NAME` et `DB_PORT`.

## Initialisation de la base de donnees

Le dossier `sql/` contient le fichier `init_db.sql`, prevu pour initialiser la base de donnees.

La table attendue par les services MySQL est une table `donnees` contenant au minimum :

- `nom_serie` : nom de la serie statistique ;
- `valeur` : valeur numerique ;
- `categorie` : categorie optionnelle ;
- `date_mesure` : date optionnelle de la mesure.

Exemple de structure SQL possible :

```sql
CREATE DATABASE IF NOT EXISTS tp2_flask;
USE tp2_flask;

CREATE TABLE IF NOT EXISTS donnees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom_serie VARCHAR(100) NOT NULL,
    valeur FLOAT NOT NULL,
    categorie VARCHAR(100),
    date_mesure DATE
);
```

Pour executer le script SQL :

```bash
mysql -u root -p < sql/init_db.sql
```

## Lancement des services

Chaque service doit etre lance dans un terminal separe.

### Service 1 - Operations sur les matrices

Dossier :

```bash
cd service1_matrices
python app.py
```

Adresse :

```text
http://localhost:5001
```

Routes principales :

| Methode | Route | Description |
| --- | --- | --- |
| GET | `/` | Page de test HTML |
| POST | `/matrices/add` | Addition de deux matrices |
| POST | `/matrices/multiply` | Multiplication de deux matrices |
| POST | `/matrices/transpose` | Transposee d'une matrice |
| POST | `/matrices/determinant` | Determinant d'une matrice carree |
| POST | `/matrices/inverse` | Inverse d'une matrice carree inversible |

Exemple de requete :

```json
{
  "A": [[1, 2], [3, 4]],
  "B": [[5, 6], [7, 8]]
}
```

### Service 2 - Statistiques sur donnees JSON

Dossier :

```bash
cd service2_statistiques
python app.py
```

Adresse :

```text
http://localhost:5002
```

Routes principales :

| Methode | Route | Description |
| --- | --- | --- |
| POST | `/stats/describe` | Statistiques descriptives |
| POST | `/stats/correlation` | Correlation de Pearson |
| POST | `/stats/test_normalite` | Test de normalite de Shapiro-Wilk |
| POST | `/stats/test_student` | Test t de Student |

Exemple pour les statistiques descriptives :

```json
{
  "data": [12, 15, 18, 20, 22]
}
```

Exemple pour la correlation :

```json
{
  "x": [1, 2, 3, 4, 5],
  "y": [2, 4, 6, 8, 10]
}
```

### Service 3 - Statistiques depuis MySQL

Dossier :

```bash
cd service3_stats_mysql
python app.py
```

Adresse :

```text
http://localhost:5003
```

Routes principales :

| Methode | Route | Description |
| --- | --- | --- |
| GET | `/` | Page de test HTML |
| GET | `/db/stats/describe?serie=serie_A` | Statistiques descriptives d'une serie MySQL |
| GET | `/db/stats/correlation?serie_x=serie_A&serie_y=serie_B` | Correlation entre deux series MySQL |

Le service recupere les valeurs dans la table `donnees`, filtrees par le champ `nom_serie`.

### Service 4 - Import CSV vers MySQL

Dossier :

```bash
cd service4_csv_mysql
python app.py
```

Adresse :

```text
http://localhost:5004
```

Route principale :

| Methode | Route | Description |
| --- | --- | --- |
| POST | `/upload/csv` | Importe un fichier CSV dans MySQL |

Le fichier CSV doit contenir au minimum les colonnes suivantes :

```text
nom_serie,valeur
```

Colonnes optionnelles :

```text
categorie,date_mesure
```

Exemple de fichier CSV :

```csv
nom_serie,valeur,categorie,date_mesure
serie_A,10,groupe1,2026-01-01
serie_A,12,groupe1,2026-01-02
serie_B,20,groupe2,2026-01-01
```

Exemple avec `curl` :

```bash
curl -X POST http://localhost:5004/upload/csv -F "file=@donnees_exemples.csv"
```

## Exemples de tests API

Le service 1 contient un fichier `tests1.http` avec plusieurs requetes pretes a etre executees depuis Visual Studio Code avec l'extension REST Client.

Les services peuvent aussi etre testes avec :

- un navigateur pour les routes `GET` ;
- Postman ;
- Insomnia ;
- curl ;
- REST Client dans Visual Studio Code.

## Codes de reponse

Les API renvoient des reponses JSON.

Codes courants :

| Code | Signification |
| --- | --- |
| 200 | Requete traitee avec succes |
| 201 | Ressource creee ou import reussi |
| 400 | Requete invalide |
| 404 | Donnee introuvable |
| 413 | Fichier trop volumineux |
| 500 | Erreur serveur ou erreur base de donnees |

En cas d'erreur, la reponse contient generalement une cle `erreur`.

Exemple :

```json
{
  "erreur": "Dimensions incompatibles"
}
```

## Ports utilises

| Service | Port |
| --- | --- |
| Service 1 - Matrices | 5001 |
| Service 2 - Statistiques JSON | 5002 |
| Service 3 - Statistiques MySQL | 5003 |
| Service 4 - Import CSV MySQL | 5004 |

## Remarques

- Chaque service est lance separement avec `python app.py`.
- Les services 3 et 4 necessitent une base MySQL configuree avant le lancement.
- Le fichier CSV importe par le service 4 est limite a 5 Mo.
- Les donnees envoyees aux API doivent etre numeriques lorsque des calculs statistiques ou matriciels sont effectues.
