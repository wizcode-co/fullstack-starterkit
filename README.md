# WizCode Fullstack StarterKit

When this application is ran, you'll see a button "Get Data" on the frontend client. This button will perform an HTTP action on the backend server and if it resolves you'll see a success message

- **Frontend** - NextJS
- **Styling** - TailwindCSS
- **Backend** - Firebase Cloud Functions with Python Flask
- **Database** - Firebase Firestore NoSQL DB
- **Auth** - Firebase Authentication - Sign in with Google

# Setup Guide

Before starting, have 2 terminals open at frontend and backend subdirs

## BACKEND
1. in the backend directory create a file - ```.env```
   1. add this to line 1: ```FLASK_APP=app```
2. In a terminal, start the flask server with ```flask run```

## FRONTEND
1. Enter ```npm install```
4. Now enter, ```next dev```
   1. If this fails, try ```npm run dev```  

