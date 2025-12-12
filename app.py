from flask import Flask, render_template, abort, url_for

app = Flask(__name__)

# Simple in-memory product catalog (replace with DB or JSON file later)
PRODUCTS = [
    {
        "id": "adirondack-patch-display",
        "title": "Adirondack Patch Display - Wall Mount",
        "price": 96,
        "excerpt": "Description: __in wide x __in high, holds all 46 Adirondack high peak patches",
        "description": "Features: Wall mount kit included, patch mount velcro kit included, customization available for stain and center image, patches NOT included",
        "leadtime": "2-3 weeks from time of purchase",
        "image": "adirondack_holder.JPG"
    },
    {
        "id": "shot-glass-display",
        "title": "Shot Glass Display - Wall Mount",
        "price": 174,
        "excerpt": "Description: __in wide x __in high, __ shotglass slots",
        "description": "Features: Slots for standard and double shot glasses, wall mount kit included, customization available for stain and center image",
        "leadtime": "2-4 weeks from time of purchase",
        "image": "shotglass_holder.JPG"
    },
    {
        "id": "shed-sauna",
        "title": "Shed Sauna",
        "price": 3990,
        "excerpt": "Description: Cedar interior, 5' wide x 4' deep x __' high",
        "description": "Features: Sealed for heat and moisture, ability to dissassemble and transport, customization available",
        "leadtime": "4-6 weeks from time of purchase",
        "image": "sauna.JPG"
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
