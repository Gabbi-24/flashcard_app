import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK (Only do this once)
### Create own firebase project and firestore database ###
### Get database credentials in json format and copy them into Firebase_key/flashcard_db_key.json file
cred = credentials.Certificate("Firebase_key/flashcard_db_key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


class GetData:
    def __init__(self, lang):
        self.lang = lang
        self.lang_collection = db.collection(lang)  # Reference to Firestore collection

    def fetch_data(self, category):
        doc_ref = self.lang_collection.document(category)
        doc = doc_ref.get()
        return doc.to_dict() if doc.exists else {"eng": {}, "non_eng": {}}

    def update_data(self, category, data):
        doc_ref = self.lang_collection.document(category)
        doc_ref.set(data, merge=True)

    def remove_word(self, category, word_number):
        word_number_str = str(word_number)
        if category != "complete":
            data = self.fetch_data(category)

            if word_number_str in data.get("eng", {}):
                del data["eng"][word_number_str]
                del data["non_eng"][word_number_str]
                self.update_data(category, data)
            else:
                print(f"Key {word_number_str} not found in {category}.")

    def add_word(self, category, word_number, non_eng_word,eng_word):
        word_number_str = str(word_number)
        data = self.fetch_data(category)
        data["eng"][word_number_str] = eng_word
        data["non_eng"][word_number_str] = non_eng_word
        self.update_data(category, data)
