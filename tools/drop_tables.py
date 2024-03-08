import os
import psycopg2
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get database details from environment variables
db_engine = os.getenv("DB_ENGINE")
db_host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_port = os.getenv("DB_PORT")

# Establish a connection to the database
conn = psycopg2.connect(
    database=db_name,
    user=db_user,
    password=db_password,
    host=db_host,
    port=db_port
)

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

def drop_all_tables():
    # Query to get all table names
    cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")
    table_names = cursor.fetchall()

    # Drop each table
    for table_name in table_names:
        cursor.execute(f"DROP TABLE IF EXISTS {table_name[0]} CASCADE;")

    # Commit the changes
    conn.commit()

# Call the function to drop all tables
drop_all_tables()

# Close the cursor and connection
cursor.close()
conn.close()

print("All tables dropped successfully.")
