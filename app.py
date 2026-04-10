from flask import Flask, render_template, request, redirect, url_for
from inventory_service import (
    get_all_products,
    add_product,
    get_product_by_id,
    update_product,
    delete_product
)
import os

app = Flask(__name__)

@app.route("/")
def index():
    products = get_all_products()
    return render_template("index.html", products=products)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form["name"]
        category = request.form["category"]
        price = float(request.form["price"])
        quantity = int(request.form["quantity"])
        supplier = request.form["supplier"]

        add_product(name, category, price, quantity, supplier)
        return redirect(url_for("index"))

    return render_template("add_product.html")

@app.route("/edit/<int:product_id>", methods=["GET", "POST"])
def edit(product_id):
    product = get_product_by_id(product_id)
    if not product:
        return "Product not found", 404

    if request.method == "POST":
        name = request.form["name"]
        category = request.form["category"]
        price = float(request.form["price"])
        quantity = int(request.form["quantity"])
        supplier = request.form["supplier"]

        update_product(product_id, name, category, price, quantity, supplier)
        return redirect(url_for("index"))

    return render_template("edit_product.html", product=product)

@app.route("/delete/<int:product_id>")
def delete(product_id):
    delete_product(product_id)
    return redirect(url_for("index"))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)