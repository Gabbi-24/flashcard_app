import json
import os
import firebase_admin
import pandas as pd
from firebase_admin import credentials, firestore


# --------------------------------- CREATE JSON FILES FROM CSV DATA -------------------------------------------------- #
def get_lang_json(csv, json_file_name):
    raw_data = pd.read_csv(csv)
    data_dict = raw_data.to_dict()

    with open(json_file_name, "w") as data_file:
        json.dump(data_dict, data_file, indent=4)


# Convert CSVs to JSON
get_lang_json("Dutch.csv", "dutch.json")
get_lang_json("German.csv", "german.json")
get_lang_json("French.csv", "french.json")
get_lang_json("Portuguese.csv", "portuguese.json")
get_lang_json("Spanish.csv", "spanish.json")

# --------------------------------- FIREBASE SETUP ------------------------------------------------------ #
### Create own firebase project and firestore database ###
### Get database credentials in json format and copy them into Firebase_key/flashcard_db_key.json file

cred = credentials.Certificate("Firebase_key/flashcard_db_key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Directory where JSON files are stored
json_folder = "C:\\Users\\gabri\\OneDrive\\Documents\\Work\\Udemy\\100 Days of Python\\OOP\\Day 31.5 - Flashcard with Firebase"

languages = ["Dutch", "German", "French", "Portuguese", "Spanish"]


# --------------------------------- FUNCTION TO INITIALIZE FIRESTORE STRUCTURE ---------------------------------------- #
def initialize_firestore():
    for lang in languages:
        lang_collection = db.collection(lang)

        # Create empty documents for Firestore structure
        for category in ["complete", "remaining", "right", "wrong"]:
            lang_collection.document(category).set({
                "eng": {},
                "non_eng": {}
            })
        print(f"Initialized Firestore collection for {lang}")


initialize_firestore()

# --------------------------------- UPLOAD JSON DATA TO FIRESTORE ---------------------------------------------------- #
for filename in os.listdir(json_folder):
    if filename.endswith(".json"):
        language_name = filename.split(".json")[0].capitalize()  # Extract language name (e.g., "dutch" -> "Dutch")

        with open(os.path.join(json_folder, filename), "r", encoding="utf-8") as file:
            data = json.load(file)

        # Update "complete" and "remaining" maps within the language collection
        db.collection(language_name).document("complete").update({
            "eng": data.get("ENG", {}),
            "non_eng": data.get("NON_ENG", {})
        })

        db.collection(language_name).document("remaining").update({
            "eng": data.get("ENG", {}),
            "non_eng": data.get("NON_ENG", {})
        })

        print(f"Uploaded data for {language_name} successfully!")

print("All JSON files uploaded!")
