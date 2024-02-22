from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/product", methods=["GET", "POST"])
def product():
    if request.method == "GET":
        return redirect("/")
    else:
        product_data = request.form.get("name")
        return render_template("product.html", product_data = product_data)



if __name__ == "__main__":
    app.run(debug=True)