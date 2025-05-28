import mysql.connector             
from mysql.connector import Error  
from faker import Faker

# Initialize the faker object
Faker.seed(33422)
fake = Faker()

# Connect to the local MariaDB database
conn = mysql.connector.connect(
    host="127.0.0.1", 
    database="employees",
    user="root", 
    password="password", 
    auth_plugin="mysql_native_password", 
    ssl_disabled=True
)
cursor = conn.cursor()

# Insert fake records!
for i in range(1000):
    firstname = fake.first_name()
    lastname = fake.last_name()
    gender = fake.random_element(["M", "F"])
    date_of_birth = fake.date_of_birth()
    hire_date = fake.date()

    print(f"Inserting[{i}]: {firstname} {lastname}")
    cursor.execute('insert into employees (\
            emp_no, \
            first_name, \
            last_name, \
            gender, \
            birth_date, \
            hire_date\
        ) \
        values (%s, \'%s\', \'%s\', \'%s\', \'%s\', \'%s\')' \
                   %(i, \
                     firstname, \
                     lastname,
                     gender, \
                     date_of_birth, \
                     hire_date
                    )
        ) 

# Commit the operations, and close the connection
conn.commit()
conn.close()
