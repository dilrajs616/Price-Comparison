from flask import render_template, request, redirect
from product.models import Product_Info

from app import app

@app.route("/google/product", methods=["GET", "POST"])
def product():
    if request.method == "GET":
        return redirect("/")
    else:
        product = request.form.get("name")
        product_data = Product_Info().google_shopping(product)
        
        return render_template ("product.html", product=product_data )