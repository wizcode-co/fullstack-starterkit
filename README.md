# Fullstack StarterKit

When you run this application you'll see a "Get Data" button on the frontend client. If you hit that button and the backend server is up successfully, you will see a success message show on screen. Otherwise you either messed something up or you're screwed

- Backend is built with Python Flask
- Frontend is built with NextJS

# Setup Guide

Before starting, have 2 terminals open at frontend and backend subdirs

## BACKEND
1. in the backend directory create a file - ```.env```
   1. add this to line 1: ```FLASK_APP=app```
2. In a terminal, start the flask server with ```flask run```

## FRONTEND
1. In terminal, enter ```npm install```
2. Now enter, ```next dev```
   1. If this fails, try ```npm run dev```  

