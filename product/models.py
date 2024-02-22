import requests

class Product_Info():
    
    def amazon(self, product):
        
        url = "https://real-time-amazon-data.p.rapidapi.com/search"

        querystring = {"query":product,"page":"1","country":"IN","category_id":"aps"}

        headers = {
            "X-RapidAPI-Key": "caa3f795c4mshd4912cdde11ccd9p1b28d6jsnf00ee6983a6e",
            "X-RapidAPI-Host": "real-time-amazon-data.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        return response.json()