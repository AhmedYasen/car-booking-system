import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

# Create a connection to the target database
target_config = {
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASS"),
    'host': os.getenv("DB_HOST"),
    'database': os.getenv("DB_NAME")
}

target_conn = mysql.connector.connect(**target_config)
target_cursor = target_conn.cursor()

# Read and execute SQL statements from the .sql file
with open('migration.sql', 'r') as sql_file:
    sql_statements = sql_file.read()

    # Split SQL statements into individual statements
    statements = sql_statements.split(';')

    for statement in statements:
        if statement.strip():
            target_cursor.execute(statement)
            target_conn.commit()

# Close the cursor and connection
target_cursor.close()
target_conn.close()
