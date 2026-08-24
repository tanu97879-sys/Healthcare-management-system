import mysql.connector

# Connect to MySQL Database
def connect_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",
            database="healthcare_db"
        )
        if conn.is_connected():
            print("Successfully connected to Healthcare Management Database!")
            return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

if __name__ == "__main__":
    connect_database()
