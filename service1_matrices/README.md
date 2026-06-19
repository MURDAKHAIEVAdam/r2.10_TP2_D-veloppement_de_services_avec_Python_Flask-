# Service 1 - Operations sur les matrices

Ce service est une API Flask permettant d'effectuer plusieurs operations de calcul matriciel a partir de donnees envoyees au format JSON.

Le service utilise :

- Python
- Flask
- NumPy

## Fonctionnalites

Le service permet de realiser les operations suivantes :

- addition de deux matrices ;
- multiplication de deux matrices ;
- transposee d'une matrice ;
- calcul du determinant d'une matrice carree ;
- calcul de l'inverse d'une matrice carree inversible.

## Structure du dossier

```text
service1_matrices/
|-- app.py
|-- matrices.py
|-- requirements.txt
|-- tester.html
|-- tests1.http
`-- README.md
```

Le fichier principal du service est `app.py`.

## Installation

Depuis le dossier du service :

```bash
cd service1_matrices
pip install -r requirements.txt
```

Si le fichier `requirements.txt` est vide, installer les dependances necessaires avec :

```bash
pip install flask numpy
```

## Lancement du service

Depuis le dossier `service1_matrices`, executer :

```bash
python app.py
```

Le service demarre par defaut a l'adresse suivante :

```text
http://localhost:5001
```

La page d'accueil `/` renvoie le fichier `tester.html`, qui peut etre utilise pour tester le service depuis un navigateur.

## Format des matrices

Les matrices doivent etre envoyees sous forme de tableaux JSON a deux dimensions.

Exemple de matrice :

```json
{
  "A": [[1, 2], [3, 4]]
}
```

Pour les operations utilisant deux matrices, le corps de la requete doit contenir `A` et `B`.

```json
{
  "A": [[1, 2], [3, 4]],
  "B": [[5, 6], [7, 8]]
}
```

## Routes disponibles

### Addition de deux matrices

```http
POST /matrices/add
```

Additionne deux matrices de memes dimensions.

Exemple de requete :

```json
{
  "A": [[1, 2], [3, 4]],
  "B": [[5, 6], [7, 8]]
}
```

Exemple de reponse :

```json
{
  "operation": "addition",
  "resultat": [[6, 8], [10, 12]]
}
```

Erreur possible :

```json
{
  "erreur": "Dimensions incompatibles"
}
```

### Multiplication de deux matrices

```http
POST /matrices/multiply
```

Multiplie deux matrices lorsque le nombre de colonnes de `A` est egal au nombre de lignes de `B`.

Exemple de requete :

```json
{
  "A": [[1, 2], [3, 4]],
  "B": [[5, 6], [7, 8]]
}
```

Exemple de reponse :

```json
{
  "operation": "multiplication",
  "resultat": [[19, 22], [43, 50]]
}
```

### Transposee d'une matrice

```http
POST /matrices/transpose
```

Calcule la transposee de la matrice `A`.

Exemple de requete :

```json
{
  "A": [[1, 2, 3], [4, 5, 6]]
}
```

Exemple de reponse :

```json
{
  "operation": "transposee",
  "resultat": [[1, 4], [2, 5], [3, 6]]
}
```

### Determinant d'une matrice

```http
POST /matrices/determinant
```

Calcule le determinant d'une matrice carree.

Exemple de requete :

```json
{
  "A": [[1, 2], [3, 4]]
}
```

Exemple de reponse :

```json
{
  "operation": "determinant",
  "resultat": -2.0
}
```

Erreur possible :

```json
{
  "erreur": "La matrice doit etre carree"
}
```

### Inverse d'une matrice

```http
POST /matrices/inverse
```

Calcule l'inverse d'une matrice carree et inversible.

Exemple de requete :

```json
{
  "A": [[1, 2], [3, 4]]
}
```

Exemple de reponse :

```json
{
  "operation": "inverse",
  "resultat": [[-2.0, 1.0], [1.5, -0.5]]
}
```

Erreurs possibles :

```json
{
  "erreur": "La matrice doit etre carree"
}
```

```json
{
  "erreur": "Matrice singuliere, non inversible"
}
```

## Tester l'API

Le fichier `tests1.http` contient plusieurs requetes pretes a etre executees avec un client HTTP compatible, par exemple l'extension REST Client de Visual Studio Code.

Il est aussi possible de tester l'API avec `curl`.

Exemple :

```bash
curl -X POST http://localhost:5001/matrices/add \
  -H "Content-Type: application/json" \
  -d "{\"A\": [[1, 2], [3, 4]], \"B\": [[5, 6], [7, 8]]}"
```

## Gestion des erreurs

En cas de probleme, le service renvoie une reponse JSON contenant la cle `erreur` avec un code HTTP `400`.

Les erreurs gerees concernent notamment :

- les matrices absentes ou invalides ;
- les dimensions incompatibles ;
- les matrices non carrees pour le determinant ou l'inverse ;
- les matrices singulieres non inversibles.
