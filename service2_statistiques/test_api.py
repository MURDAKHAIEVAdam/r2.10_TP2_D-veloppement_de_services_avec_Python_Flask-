import requests

# L'URL locale de ton service statistique (vérifie bien le port, ici 5002)
URL = "http://127.0.0.1:5002/stats/describe"

# Les données (la liste de nombres) que tu envoies à ton API
payload = {
    "data": [12, 15, 14, 18, 11, 9, 16, 15, 13, 17]
}

try:
    # On envoie la requête POST avec le JSON
    response = requests.post(URL, json=payload)
    
    print("Status Code:", response.status_code)
    print("Réponse du serveur :", response.json())
except Exception as e:
    print("Erreur lors du test :", e)