from src.db import DbAdapter


class Booking:
    def __init__(self):
        self.db = DbAdapter()
        self.db.connect()

    def create(self, customer_id, vehicle_id, hire_date, return_date):
        query = "INSERT INTO booking (customer_id, vehicle_id, hire_date, return_date) VALUES (%s, %s, %s, %s)"
        values = (customer_id, vehicle_id, hire_date, return_date)
        success, data = self.db.execute(query, values)
        if success:
            data = self.db.last_rowid()

        return success, data

    def read_by_hire_date(self, hire_date):
        query = "SELECT * FROM booking (customer_id, vehicle_id, return_date) WHERE hire_date = %s"
        values = (hire_date, )
        return self.db.execute(query, values)