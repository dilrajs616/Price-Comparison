from flask import request, session, jsonify
from passlib.hash import pbkdf2_sha256
import uuid
from app import db

class User:

    def start_session(self, user):
        
        del user["password"]
        session["logged_in"] = True
        session["user"] = user
        return session, 200
    
    def signup(self):
        
        name = request.form.get("name")
        username = request.form.get("username")
        password = request.form.get("password")
        
        if db.users.count_documents({"username":username}):
            return jsonify({"error": "username already in use"}), 203
                
        else:    
            user = {
                "_id": uuid.uuid4().hex,
                "name": name,
                "username": username,
                "password": password,
                "wishlist": [],
                "history": []
            }
            
            user["password"] = pbkdf2_sha256.encrypt(user["password"])

            if db.users.insert_one(user):
                return self.start_session(user)
            
            else:
                return jsonify({"error": "could not signup"}), 201
    
    def login(self):
        username = request.form.get("username")
        password = request.form.get("password")
        
        user = db.users.find_one({"username":username})
        
        if user and pbkdf2_sha256.verify(password, user["password"]):
            return self.start_session(user)
        
        else:
            return jsonify({"error":"credentials not found"}), 202
    
    def logout(self):
        session.clear()
        return True
    
    