from src import app
from flask import request, jsonify
from src.models.vehicle import Vehicle


@app.route('/vehicle', methods=['POST'])
def create_vehicle():
    category_id = request.json['category_id']
    avail = request.json['availability']
    data = Vehicle().create(category_id, avail)
    return data


# Get a single customer by ID
@app.route('/vehicle/<int:vehicle_id>', methods=['GET'])
def get_vehicle(vehicle_id):
    success, data = Vehicle().read(vehicle_id)
    if success and data:
        return data
    elif not success:
        return {"msg": data}
    return {"msg": f"Customer with id ({vehicle_id}) is not found"}


# Update a customer by ID
@app.route('/vehicle/<int:vehicle_id>', methods=['PUT'])
def update_vehicle(vehicle_id):
    avail = request.json['availability']
    success, msg = Vehicle().update_by_id(vehicle_id, avail)
    return jsonify(msg)


# Delete a customer by ID
@app.route('/vehicle/<int:vehicle_id>', methods=['DELETE'])
def delete_vehicle(vehicle_id):
    success, msg = Vehicle().delete(vehicle_id)
    return jsonify(msg)
