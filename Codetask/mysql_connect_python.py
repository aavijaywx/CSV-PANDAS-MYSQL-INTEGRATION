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

    df=pd.read_csv(r'Codetask/employees.csv',sep='\t')
    print(f"Column in Excel:",df.columns)

    my_cursor.execute(f'DROP TABLE IF EXISTS employees')



    columns=','.join([f'`{col}` VARCHAR(255)'for col in df.columns])
    create_table_query=f"CREATE TABLE employees({columns})"
    my_cursor.execute(create_table_query)
    print(f'Create Table Successfully!')

    placeholders = ', '.join(['%s'] * len(df.columns))
    insert_query = f"INSERT INTO employees({', '.join(df.columns)}) VALUES ({placeholders})"
    my_cursor.executemany(insert_query, df.values.tolist())
    connection.commit()

 
except Error as e:
    print(f"Error: {e} ")

finally:
    if connection.is_connected():
        my_cursor.close()
        connection.close()
        print(f"Connection Closed Successfully!")