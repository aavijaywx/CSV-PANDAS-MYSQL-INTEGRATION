import mysql.connector 
from mysql.connector import Error
import pandas as pd

try: 
       connection=mysql.connector.connect(
        host='localhost',
        user='root',
        password='Root@123',
        database='codewithvijay'
    )

       if connection.is_connected():
        print(f"Connection Created Successfully!")
        my_cursor=connection.cursor()
        my_cursor.execute(f'Select Database();')
        db=my_cursor.fetchone()
        print(f"Connected Database : {db[0]}")

        query=f"SELECT * FROM employees"
        df=pd.read_sql(query,connection)
        print(df)


except Error as e:
    print(f"Errror: {e}")

finally:
    if connection.is_connected():
        my_cursor.close()
        connection.close()
        print(f"Connection Closed Successfully!")