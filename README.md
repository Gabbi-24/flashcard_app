# flashcard_app
A simple vocabulary flashcard app.

# NOTE
Due to security reasons, I could not include the actual credentials for the Firebase database. I chose not to hard-code my values because I want to show my understanding and use of server databases (I used Firebase). Rather, I have all the code setup. The only thing you need to do is paste in your own Firebase credentials (json format) into the flashcard_db_key.json file inside the Firebase_key folder.

# Here are the steps to follow to be able to run my code successfully
Step 1: Create a Firebase Project
Go to the Firebase Console.
Click Add project to create a new Firebase project.
Follow the on-screen instructions (you can choose to enable or disable Google Analytics for your project).
Once the project is created, you’ll be taken to the Firebase project dashboard.

Step 2: Set Up Firestore Database
In the Firebase console, navigate to Firestore Database on the left sidebar.
Click Create database and select the appropriate settings (start in production mode or test mode).
Set up the rules and location based on your needs (you can use default settings for now).

Step 3: Get Your Firebase Database Credentials
In the Firebase console, click on the Settings gear icon next to Project Overview and select Project settings.
Go to the Service accounts tab.
Click Generate new private key. This will download a .json file containing your Firebase credentials.
Move the downloaded JSON file to the Firebase_key folder in your project and rename it to flashcard_db_key.json.

Step 4: Edit and Use the Firebase Credentials
Open the flashcard_db_key.json file in the Firebase_key folder.
Ensure that the file is properly populated with the credentials you downloaded from Firebase.
Run the code as normal, and it will now connect to your Firebase Firestore database using your credentials.
