from flask import Flask, request, jsonify
import pandas as pd
import mysql.connector
from dotenv import load_dotenv
import os
import io

load_dotenv()
app = Flask(__name__)

# Configuration des constantes [cite: 223]
COLONNES_REQUISES = {'nom_serie', 'valeur'}
TAILLE_MAX_OCTETS = 5 * 1024 * 1024  # 5 Mo [cite: 223]

def get_connection():
    return mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        database=os.getenv('DB_NAME'),
        port=os.getenv('DB_PORT'),
    )

@app.route('/upload/csv', methods=['POST'])
def upload_csv():
    print("Requête reçue !")
    print(f"Fichiers envoyés : {request.files}")
    if 'file' not in request.files:
        print("Erreur : clé 'file' manquante")
        return jsonify({'erreur': 'Aucun fichier envoyé'}), 400

    if 'file' not in request.files:
        return jsonify({'erreur': 'Aucun fichier envoyé'}), 400
    file = request.files['file']
    
    # 2. Validation de l'extension et de la taille 
    if not file.filename.endswith('.csv'):
        return jsonify({'erreur': 'Seuls les fichiers .csv sont acceptés'}), 400
    
    content = file.read()
    if len(content) > TAILLE_MAX_OCTETS:
        return jsonify({'erreur': 'Fichier trop volumineux'}), 413
    
    # 3. Lecture et validation via pandas 
    df = pd.read_csv(io.BytesIO(content))
    colonnes_manquantes = COLONNES_REQUISES - set(df.columns)
    if colonnes_manquantes:
        return jsonify({'erreur': 'Colonnes obligatoires manquantes', 'manquantes': list(colonnes_manquantes)}), 400
    
    # 4. Nettoyage des données 
    df['valeur'] = pd.to_numeric(df['valeur'], errors='coerce')
    df.dropna(subset=['valeur'], inplace=True)
    
    # 5. Insertion en base de données 
    conn = get_connection()
    cursor = conn.cursor()
    for _, row in df.iterrows():
        cursor.execute(
            'INSERT INTO donnees (nom_serie, valeur, categorie, date_mesure) VALUES (%s, %s, %s, %s)',
            (row['nom_serie'], float(row['valeur']), row.get('categorie'), row.get('date_mesure'))
        )
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'statut': 'success', 'message': 'Chargement réussi'}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5004)