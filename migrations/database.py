import mysql.connector
import os

# Step 1: Connect to the MySQL Server
server_config = {
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASS"),
    'host': os.getenv("DB_HOST"),
}

server_conn = mysql.connector.connect(**server_config)
server_cursor = server_conn.cursor()

# Step 2: Create the Database
db_name = os.getenv("DB_NAME")
create_database_query = f"CREATE DATABASE IF NOT EXISTS `CarBookingDb`"
server_cursor.execute(create_database_query)
