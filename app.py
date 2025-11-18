from flask import Flask, render_template, abort, url_for

app = Flask(__name__)

# Simple in-memory product catalog (replace with DB or JSON file later)
PRODUCTS = [
    {
        "id": "sauna-custom",
        "title": "Custom Mini Sauna Shelf",
        "price": 450,
        "excerpt": "Hand-built sauna bench shelf — cedar, stainless hardware.",
        "description": "Full description: handcrafted cedar sauna shelf, sealed for heat and moisture. Dimensions: 24 x 10 x 6 in. Custom sizes available.",
        "image": "sauna.jpg"
    },
    {
        "id": "adirondack-patch",
        "title": "Adirondack Patch Wall Mount Holder",
        "price": 65,
        "excerpt": "Rustic patch-holder for jackets/keys — flat mount.",
        "description": "Holds jackets, keys, and small items. Built from reclaimed pine, hand-sanded, finished with tung oil.",
        "image": "adirondack_holder.jpg"
    },
    {
        "id": "shotglass-rack",
        "title": "Shot Glass Wall Mount Holder (6)",
        "price": 48,
        "excerpt": "Holds 6 shot glasses — perfect for bars and man caves.",
        "description": "Fits standard shot glasses; easy wall-mount with 2 screws. Stained to your preference (light/medium/dark).",
        "image": "shotglass_holder.jpg"
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
        "email": "youremail@example.com",
        "phone": "(555) 555-5555",
        "location": "Your City, Province/State"
    }
    business_info = {
        "name": "Your Business Name",
        "hours": "By appointment / custom order"
    }
    return render_template("about.html", contact=contact, business=business_info)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
