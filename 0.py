import mysql.connector 
from mysql.connector import Error 

try:

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password=""
    )

    cursor = db.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS user_database")
    print("Database 'user_database' created or already exists.")

    cursor.execute("USE user_database")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL UNIQUE,
            email VARCHAR(100) NOT NULL UNIQUE,
            password VARCHAR(100) NOT NULL
        )
    """)

    db.commit()
    print("Table 'users' with username, email, and password created successfully!")

except Error as e:
    print(f"Error: {e}")

finally:
  
    if db.is_connected():
        cursor.close()
        db.close()
        print("MySQL connection closed.")
