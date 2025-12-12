from flask import Flask, jsonify, request
from http import HTTPStatus

app = Flask(__name__)  # instance of Flask

@app.route("/", methods=["GET"])
def index():
    return "Welcome To Flask Framework"

@app.route("/cohort-62", methods=["GET"])
def cohort62():
    students_list = ["Michael", "Tyler", "Carlos", "Jonathan", "Rober", "Ashton", "Kirt"]
    return jsonify(students_list)

@app.route("/cohort-100", methods=["GET"])
def cohort100():
    students_list = ["Pam", "Dwight", "Michael", "Oscar"]
    return jsonify(students_list)

@app.route("/contact", methods=["GET"])
def contact():
    information = {"email": "johnasrochon@yahoo.com", "phone": "832-348-9268"}
    return jsonify(information)

@app.route("/course-information", methods=["GET"])
def course_information():
    info = {"title": "Intro to Web API with Flask", "duration": "4 months", "level": "beginner"}
    return jsonify(info)

@app.route("/user-endpoint", methods=["GET"])
def user_endpoint():
    user = {"name": "john", "role": "student", "is_active": True, 
            "favorite_technologies": ["API", "Cloud", "networking"]}
    return jsonify(user), HTTPStatus.OK

@app.route("/greet/<string:name>")
def greet(name):
    return jsonify({"message": f"Hello {name}"})


# ----------------- PRODUCTS -----------------

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

@app.route("/api/products", methods=["GET"])
def get_products():
    return jsonify({
        "success": True,
        "message": "Products retrieved successfully",
        "data": products
    }), HTTPStatus.OK


@app.route("/api/products/<int:product_id>", methods=["GET"])
def get_product_by_id(product_id):
    for product in products:
        if product["_id"] == product_id:
            return jsonify({
                "success": True,
                "message": "Product retrieved successfully",
                "data": product
            }), HTTPStatus.OK

    return jsonify({
        "success": False,
        "message": "Product not found"
    }), HTTPStatus.NOT_FOUND


@app.route("/api/products", methods=["POST"])  # fixed typo
def create_product():
    new_product = request.get_json()

    if "_id" not in new_product:
        return jsonify({"success": False, "message": "Product must include _id"}), HTTPStatus.BAD_REQUEST

    products.append(new_product)
    return jsonify({
        "success": True,
        "message": "Product successfully created",
        "data": new_product
    }), HTTPStatus.CREATED



# -------------------- COUPONS API --------------------

coupons = [
    {"_id": 1, "code": "WELCOME10", "discount": 10},
    {"_id": 2, "code": "SPOOKY25", "discount": 25},
    {"_id": 3, "code": "VIP50", "discount": 50}
]

# GET all coupons
@app.route("/api/coupons", methods=["GET"])
def get_coupons():
    return jsonify({
        "success": True,
        "data": coupons
    }), HTTPStatus.OK


# GET coupons count
@app.route("/api/coupons/count", methods=["GET"])
def get_coupons_count():
    return jsonify({
        "success": True,
        "count": len(coupons)
    }), HTTPStatus.OK


# GET coupon by ID
@app.route("/api/coupons/<int:id>", methods=["GET"])
def get_coupon_by_id(id):
    for coupon in coupons:
        if coupon["_id"] == id:
            return jsonify({
                "success": True,
                "data": coupon
            }), HTTPStatus.OK

    return jsonify({
        "success": False,
        "message": "Coupon not found"
    }), HTTPStatus.NOT_FOUND


# POST create coupon
@app.route("/api/coupons", methods=["POST"])
def create_coupon():
    new_coupon = request.get_json()

    # Validate input
    if "_id" not in new_coupon or "code" not in new_coupon or "discount" not in new_coupon:
        return jsonify({
            "success": False,
            "message": "Coupon must include _id, code, discount"
        }), HTTPStatus.BAD_REQUEST

    coupons.append(new_coupon)

    return jsonify({
        "success": True,
        "message": "Coupon created successfully",
        "data": new_coupon
    }), HTTPStatus.CREATED


# PUT update coupon by ID
@app.route("/api/coupons/<int:id>", methods=["PUT"])
def update_coupon(id):
    updated_data = request.get_json()

    for coupon in coupons:
        if coupon["_id"] == id:
            coupon.update(updated_data)
            return jsonify({
                "success": True,
                "message": "Coupon updated successfully",
                "data": coupon
            }), HTTPStatus.OK

    return jsonify({
        "success": False,
        "message": "Coupon not found"
    }), HTTPStatus.NOT_FOUND


# DELETE coupon by ID
@app.route("/api/coupons/<int:id>", methods=["DELETE"])
def delete_coupon(id):
    for coupon in coupons:
        if coupon["_id"] == id:
            coupons.remove(coupon)
            return jsonify({
                "success": True,
                "message": "Coupon deleted successfully"
            }), HTTPStatus.OK

    return jsonify({
        "success": False,
        "message": "Coupon not found"
    }), HTTPStatus.NOT_FOUND


# SEARCH: coupons with discount < 30
@app.route("/api/coupons/search", methods=["GET"])
def search_coupons():
    filtered = [c for c in coupons if c["discount"] < 30]

    return jsonify({
        "success": True,
        "results": filtered
    }), HTTPStatus.OK



# -------------------- MAIN --------------------

if __name__ == "__main__":
    app.run(debug=True)
