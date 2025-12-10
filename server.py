from flask import Flask, jsonify, request
from http import HTTPStatus


app = Flask(__name__) # instance of Flask

@app.route("/", methods=["GEt"])
def index():
    return "Welcome To Flask Framework"

@app.route("/cohort-62", methods=["GET"])
def cohort62():
    students_list = ["Michael", "Tyler", "Carlos", "Jonathan", "Rober", "Ashton", "Kirt"]
    return students_list

@app.route("/cohort-100", methods=["GET"])
def cohort100():
    students_list = ["Pam", "Dwight", "Michael", "Oscar"]
    return students_list

@app.route("/contact", methods=["GET"])
def contact():
    information = {"email": "johnasrochon@yahoo.com", "phone": "832-348-9268"}
    return information

@app.route("/course-information", methods=["GET"])
def course_information():
    course_information = {"title": "Intro to Web API with Flask", "duration": "4 months", "level": "beginner"}
    return course_information

@app.route("/user-endpoint", methods=["GET"])
def user_endpoint():
    user_endpoint = {"name": "john", "role": "student", "is_active": True , "favorite_technologies": ["API", "Cloud", "networking"]}
    return user_endpoint, HTTPStatus.OK

# Path parameter
# Is a dynamic part of the URL used to identify a specific item or resource within an API
@app.route("/greet/<string:name>")
def greet(name):
    return {"message": f"Hello {name}"}

products = [
    {
          "_id": 1,
    "title": "Nintendo Switch",
    "price": 299.99,
    "category": "Entertainment",
    "image": "https://picsum.photos/seed/1/300/300"
  },
  {
    "_id": 2,
    "title": "Smart Refrigerator",
    "price": 999.99,
    "category": "Kitchen",
    "image": "https://picsum.photos/seed/2/300/300"
  },
  {
    "_id": 3,
    "title": "Bluetooth Speaker",
    "price": 79.99,
    "category": "Electronics",
    "image": "https://picsum.photos/seed/3/300/300"
    }
]

# GET /api/products endpoint that return a list of products
@app.route("/api/products", methods=["GET"])
def get_products():
    return jsonify({
        "success": True,
        "message": "Products retrieved successfully",
        "data": products
    }), HTTPStatus.OK

# Get /api/products/2
@app.route("/api/products/<int:product_id>", methods=["GET"])
def get_product_by_id(product_id):
    for product in products:
        print (product)
        if product ["_id"] == product_id:
            return jsonify ({
                "success": True,
                "message": "Product retrieved successfully",
                "data": product
            }), HTTPStatus.OK
    
    return "Not found"

# POST /api/products
@app.route("/api/prodcuts", methods=["POST"])
def create_product():
    print (request.get_json())
    new_product= request.get_json()
    products.append(new_product)
    return jsonify({
        "success": True,
        "message": "Product successfully created",
        "date": new_product
    }), HTTPStatus.CREATED

# ---------Coupons---------
coupons = [
  {"_id": 1, "code": "WELCOME10", "discount": 10},
  {"_id": 2, "code": "SPOOKY25", "discount": 25},
  {"_id": 3, "code": "VIP50", "discount": 50}
]

@app.route("/api/coupons", methods=["GET"])
def get_coupons():
    return coupons

@app.route("/api/coupons/count", methods=["GET"])
def get_coupons_count():
    return len(coupons)


if __name__ == "__main__":
    app.run(debug=True)
# When this file is run directly: __name__ -- "__main__"
# When this file is imported as a modulel: __name__ == "server.py"
 