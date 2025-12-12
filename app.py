from flask import Flask, render_template, abort, url_for

app = Flask(__name__)

# Simple in-memory product catalog (replace with DB or JSON file later)
PRODUCTS = [
    {
        "id": "sauna-custom",
        "title": "Custom Sauna",
        "price": 3990,
        "excerpt": "Description: Cedar interior, 5' wide x 4' wide x __' high",
        "description": "Features: Sealed for heat and moisture, ability to dissassemble and transport, customization available",
        "image": "sauna.JPG"
    },
    {
        "id": "adirondack-patch",
        "title": "Adirondack Patch Wall Mount Holder",
        "price": 96,
        "excerpt": "Rustic patch-holder for jackets/keys — flat mount.",
        "description": "Holds jackets, keys, and small items. Built from reclaimed pine, hand-sanded, finished with tung oil.",
        "image": "adirondack_holder.JPG"
    },
    {
        "id": "shotglass-rack",
        "title": "Shot Glass Wall Mount Holder (6)",
        "price": 174,
        "excerpt": "Holds 6 shot glasses — perfect for bars and man caves.",
        "description": "Fits standard shot glasses; easy wall-mount with 2 screws. Stained to your preference (light/medium/dark).",
        "image": "shotglass_holder.JPG"
    }
]

def get_product(product_id):
    for p in PRODUCTS:
        if p["id"] == product_id:
            return p
    return None

@app.route("/")
def index():
    # featured (take first 3)
    featured = PRODUCTS[:3]
    return render_template("index.html", featured=featured)

@app.route("/products")
def products():
    return render_template("products.html", products=PRODUCTS)

@app.route("/product/<product_id>")
def product_detail(product_id):
    p = get_product(product_id)
    if not p:
        abort(404)
    return render_template("product_detail.html", product=p)

@app.route("/about")
def about():
    contact = {
        "email": "love.hartzke@gmail.com",
        "phone": "(613) 407-6995",
        "location": "Kanata, Ontario"
    }
    business_info = {
        "name": "Pepperville Products",
    }
    return render_template("about.html", contact=contact, business=business_info)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
