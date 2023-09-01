from src import app
from flask import request, jsonify
from src.models.booking import Booking
from src.models.vehicle import Vehicle
from src.models.customer import Customer
from src.models.invoice import Invoice
from datetime import datetime
import logging


@app.route('/booking', methods=['POST'])
def book_vehicle():
    customer_id = request.json['customer_id']
    vehicle_id = request.json['vehicle_id']
    hire_date = request.json['hire_date']
    return_date = request.json['return_date']

    success, data = Vehicle.read(vehicle_id)
    if not success:
        return data
    elif success and data is None:
        return {"msg": f"There is no vehicle with this id ({vehicle_id})"}

    vehicle_avail = data[2]
    if not vehicle_avail:
        return {"msg": "Please select available vehicle!"}

    success, data = Customer.read_customer_by_id(customer_id)
    if not success:
        return data
    elif success and data is None:
        return {"msg": f"Customer with id ({customer_id} is not registered!"}

    date_format = '%Y-%m-%d'
    try:
        hire_date_obj = datetime.strptime(hire_date, date_format)
        return_date_obj = datetime.strptime(return_date, date_format)

    except ValueError as e:
        return {"msg": str(e)}

    today = datetime.today()

    hire_duration = return_date_obj - hire_date_obj
    pre_hire_duration = hire_date_obj - today

    if hire_date_obj > return_date_obj:
        return {"msg": "hire date must be before the return date"}
    elif today > hire_date_obj:
        return {"msg": "You are selecting an old hire date"}
    elif hire_duration > 7:
        return {"msg": "unfortunately, you can't hire vehicle more than 7 days!"}
    elif pre_hire_duration > 7:
        return {"msg": "unfortunately, only you can book a vehicle max. 7 days in advance!"}
    elif pre_hire_duration > 1:
        logging.info(f"Dear Customer, \n\twe are confirming on vehicle {vehicle_id} hire. Thank you.")

    booking_id = Booking().create()

    invoice = Invoice().create_invoice()
    return "OK"
