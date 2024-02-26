from serpapi import GoogleSearch

class Product_Info():
    
    def google_product(self, product):
        
        params = {
            "engine": "google_shopping",
            "q": product,
            "api_key": "2c48521c2995601a65ae5562f47262ccc226a3a794e43d9ec325c75a3a401e4d"
        }

        search = GoogleSearch(params)
        results = search.get_dict()
        return results["shopping_results"]