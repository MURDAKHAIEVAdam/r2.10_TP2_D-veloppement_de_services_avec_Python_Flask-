import requests

# L'URL locale de ton service statistique (vérifie bien le port, ici 5002)
BASE_URL = "http://127.0.0.1:5002"

# --- Test 1 : Description statistique ---
print("=== Test 1 : /stats/describe ===")
url = f"{BASE_URL}/stats/describe"
payload = {
    "data": [12, 15, 14, 18, 11, 9, 16, 15, 13, 17]
}
try:
    response = requests.post(url, json=payload)
    print("Status Code:", response.status_code)
    print("Réponse du serveur :", response.json())
except Exception as e:
    print("Erreur lors du test :", e)

print()

# --- Test 2 : Corrélation de Pearson ---
print("=== Test 2 : /stats/correlation ===")
url = f"{BASE_URL}/stats/correlation"
payload = {
    "x": [1, 2, 3, 4, 5],
    "y": [2, 4, 5, 4, 5]
}
try:
    response = requests.post(url, json=payload)
    print("Status Code:", response.status_code)
    print("Réponse du serveur :", response.json())
except Exception as e:
    print("Erreur lors du test :", e)

print()

# --- Test 3 : Test de normalité (Shapiro-Wilk) ---
print("=== Test 3 : /stats/test_normalite ===")
url = f"{BASE_URL}/stats/test_normalite"
payload = {
    "data": [12, 15, 14, 18, 11, 9, 16, 15, 13, 17]
}
try:
    response = requests.post(url, json=payload)
    print("Status Code:", response.status_code)
    print("Réponse du serveur :", response.json())
except Exception as e:
    print("Erreur lors du test :", e)

print()

# --- Test 4 : Test t de Student ---
print("=== Test 4 : /stats/test_student ===")
url = f"{BASE_URL}/stats/test_student"
payload = {
    "groupe1": [12, 15, 14, 18, 11],
    "groupe2": [20, 22, 19, 25, 21]
}
try:
    response = requests.post(url, json=payload)
    print("Status Code:", response.status_code)
    print("Réponse du serveur :", response.json())
except Exception as e:
    print("Erreur lors du test :", e)
