from src import app
from flask import request, jsonify
from src.models.customer import Customer


@app.route('/customer', methods=['POST'])
def create_customer():
    name = request.json['name']
    email = request.json['email']
    data = Customer().create_customer(name=name, email=email)
    return data


# Get all customers
@app.route('/customers', methods=['GET'])
def get_customers():
    customers = Customer().read_all()
    return customers


# Get a single customer by ID
@app.route('/customer/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    success, data = Customer().read_customer_by_id(customer_id)
    if success and data:
        return data
    elif not success:
        return {"msg": data}
    return {"msg": f"Customer with id ({customer_id}) is not found"}


# Update a customer by ID
@app.route('/customer/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    name = request.json['name']
    if customer_id:
        success, msg = Customer().update_customer_by_id(customer_id, name)
    else:
        email = request.json['email']
        success, msg = Customer().update_customer_by_email(email, name)
    return jsonify(msg)


# Delete a customer by ID
@app.route('/customer/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    success, msg = Customer().delete_customer_by_id(customer_id)
    return jsonify(msg)
