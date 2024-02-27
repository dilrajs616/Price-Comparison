from flask import session
from serpapi import GoogleSearch
from app import db

class Product_Info():
    
    def google_shopping(self, product):
        
        print(session)
        
        params = {
            "engine": "google_shopping",
            "q": product,
            "location": "India",
            "hl": "en",
            "gl": "in",
            "google_domain": "google.co.in",
            "num": "10",
            "start": "10",
            "safe": "active",
            "api_key": "e033335621656412e5aaae7d7e76dab36a1ec1819e0161a403e258031472117b"
        }

        id = session["user"]["_id"]
        
        db.users.update_one({"_id":id} ,{"$push": {"history": product}})

        search = GoogleSearch(params)
        results = search.get_dict()

        return results, 200