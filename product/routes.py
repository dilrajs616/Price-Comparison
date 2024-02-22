from flask import render_template, request, redirect
from product.models import Product_Info

from app import app

@app.route("/product", methods=["GET", "POST"])
def product():
    if request.method == "GET":
        return redirect("/")
    else:
        product = request.form.get("name")
        product_data = Product_Info().amazon(product)
        
        if "products" in product_data["data"]:
            return render_template("product.html", product = product_data["data"]["products"][1])
        
        else:
            return "could not fetch data"
