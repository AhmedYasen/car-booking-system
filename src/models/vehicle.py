from src.db import DbAdapter
from enum import Enum


class Category(Enum):
    SMALL = 0,
    FAMILY = 1,
    VAN = 2


class Vehicle:
    def __init__(self):
        self.db = DbAdapter()
        self.db.connect()

    def create(self, category_id: int, avail: bool):
        query = "INSERT INTO vehicle (category_id, availability) VALUES (%s, %s)"
        values = (category_id, avail)
        success, data = self.db.execute(query, values)
        if success:
            data = self.db.last_rowid()
        return success, data

    def read(self, vehicle_id):
        query = "SELECT * FROM vehicle WHERE id = %s"
        self.db.execute(query, (vehicle_id,))
        return self.db.fetchone()

    def update_by_id(self, vehicle_id, avail):
        query = "UPDATE vehicle SET availability = %s WHERE id = %s"
        values = (avail, vehicle_id)
        return self.db.execute(query, values)

    def delete(self, vehicle_id):
        query = "DELETE FROM vehicle WHERE id = %s"
        return self.db.execute(query, (vehicle_id,))
