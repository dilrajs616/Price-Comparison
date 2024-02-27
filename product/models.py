from serpapi import GoogleSearch

class Product_Info():
    
    def google_shopping(self, product):
        
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

        search = GoogleSearch(params)
        results = search.get_dict()

        return results, 200