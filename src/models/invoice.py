from src.db import DbAdapter


class Invoice:
    def __init__(self):
        self.db = DbAdapter()
        self.db.connect()

    def create_invoice(self, booking_id: int, total: int, paid: bool):
        query = "INSERT INTO invoice (booking_id, total, paid) VALUES (%s, %s, %s)"
        values = (booking_id, total, paid)
        success, data = self.db.execute(query, values)
        if success:
            data = self.db.last_rowid()
        return success, data

    def read_invoice(self, invoice_id: int):
        query = "SELECT * FROM invoice WHERE id = %s"
        self.db.execute(query, (invoice_id,))
        return self.db.fetchone()

    def delete_invoice(self, invoice_id):
        query = "DELETE FROM invoice WHERE id = %s"
        return self.db.execute(query, (invoice_id,))
