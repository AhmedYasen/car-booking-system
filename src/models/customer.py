from src.db import DbAdapter


class Customer:
    def __init__(self):
        self.db = DbAdapter()
        self.db.connect()

    def create_customer(self, email, name):
        query = "INSERT INTO customers (email, name) VALUES (%s, %s)"
        values = (email, name)
        success, data = self.db.execute(query, values)
        if success:
            data = self.db.last_rowid()

        return success, data

    def read_customer_by_email(self, email):
        query = "SELECT * FROM customers WHERE email = %s"
        self.db.execute(query, (email,))
        return self.db.fetchone()

    def read_customer_by_id(self, customer_id):
        query = "SELECT * FROM customers WHERE id = %s"
        self.db.execute(query, (customer_id,))
        return self.db.fetchone()

    def read_all(self):
        query = "SELECT * FROM customers"
        self.db.execute(query)
        return self.db.fetchall()

    def update_customer_by_id(self, customer_id, new_name):
        query = "UPDATE customers SET name = %s WHERE id = %s"
        values = (new_name, customer_id)
        return self.db.execute(query, values)

    def update_customer_by_email(self, email, new_name):
        query = "UPDATE customers SET name = %s WHERE email = %s"
        values = (new_name, email)
        return self.db.execute(query, values)

    def delete_customer_by_id(self, customer_id):
        query = "DELETE FROM customers WHERE id = %s"
        return self.db.execute(query, (customer_id,))
