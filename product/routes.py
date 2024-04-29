from flask import render_template, request, redirect
from product.models import Product_Info
from product.scrape import Scraper

from app import app

@app.route("/google/product", methods=["GET", "POST"])
def product():
    if request.method == "GET":
        return redirect("/")
    else:
        product = request.form.get("name")
        product_data, res = Product_Info().google_shopping(product)
        
        return render_template ("product.html", product=product_data )
    
@app.route('/product/compare')
def compare():
    site = request.args.get("compare_link")
    table = Scraper().get_table(site)
    return render_template("comparison.html", table=table)