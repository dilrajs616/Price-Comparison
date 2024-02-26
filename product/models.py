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
            "api_key": "3461034bcd278c80c11bb39008c5690bad72a78b9fc1fc80c6b39a5c7870928f"
        }

        search = GoogleSearch(params)
        results = search.get_dict()

        return results, 200