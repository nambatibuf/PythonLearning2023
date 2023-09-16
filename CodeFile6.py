import pandas as pd
import sqlite3
from sqlite3 import Error

conn_orders = sqlite3.connect("orders.db")
cur = conn_orders.cursor()

# sql_statement = "select * from customers;"
# df = pd.read_sql_query(sql_statement, conn_orders)
# display(df)

# sql_statement = "select * from orders;"
# df = pd.read_sql_query(sql_statement, conn_orders)
# display(df)

# sql_statement = "select * from vendors;"
# df = pd.read_sql_query(sql_statement, conn_orders)
# display(df)

# sql_statement = "select * from products;"
# df = pd.read_sql_query(sql_statement, conn_orders)
# display(df)

# sql_statement = "select * from orderitems;"
# df = pd.read_sql_query(sql_statement, conn_orders)
# display(df)

# sql_statement = "select * from productnotes;"
# df = pd.read_sql_query(sql_statement, conn_orders)
# display(df)


def ex1():
    # Write an SQL statement that SELECTs all rows from the `customers` table
    # output columns: cust_name, cust_email

    ### BEGIN SOLUTION
    sql_statement = "select cust_name, cust_email from customers"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex2():
    # Write an SQL statement that SELECTs all rows from the `products` table
    # output columns: vend_id

    ### BEGIN SOLUTION
    sql_statement = "select vend_id from products"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex3():
    # Write an SQL statement that SELECTs distinct rows for vend_id from the `products` table
    # output columns: vend_id

    ### BEGIN SOLUTION
    sql_statement = "select distinct(vend_id) from products"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex4():
    # Write an SQL statement that SELECTs the first five rows from the `products` table
    # output columns: prod_name

    ### BEGIN SOLUTION
    sql_statement = "select prod_name from products limit 5"
    ### END SOLUTION-*
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex5():
    # Write an SQL statement that SELECTs 4 rows starting from row 3 from `products` table
    # output columns: prod_name

    ### BEGIN SOLUTION
    sql_statement = "select prod_name from products limit 4 offset 3"
    
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex6():
    # Write an SQL statement that SELECTs all rows from `products` table and sorts by prod_name
    # output columns: prod_name

    ### BEGIN SOLUTION
    sql_statement = "select prod_name from products order by prod_name"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex7():
    # Write an SQL statement that SELECTs all rows from `products` table and sorts by prod_price and then prod_name 
    # output columns: prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "select prod_id, prod_price, prod_name from products order by prod_price,prod_name"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex8():
    # Write an SQL statement that SELECTs all rows from `products` table and sorts by prod_price (descending order)
    # and then prod_name 
    # output columns: prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "select prod_id,prod_price,prod_name from products order by prod_price desc,prod_name "
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex9():
    # Write an SQL statement that SELECTs all rows from `products` table where the price of product is 2.50
    # output columns: prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "select prod_id,prod_price,prod_name from products where prod_price=2.50"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex10():
    # Write an SQL statement that SELECTs all rows from `products` table where the name of product is Oil can
    # output columns: prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "select prod_id,prod_price,prod_name from products where prod_name='Oil can'"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex11():
    # Write an SQL statement that SELECTs all rows from `products` table where the price of product is 
    # less than or equal to 10
    # output columns: prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "select prod_id,prod_price,prod_name from products where prod_price<=10" 
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex12():
    # Write an SQL statement that SELECTs all rows from `products` table where the vendor id is not equal to 1003
    # output columns: vend_id, prod_name

    ### BEGIN SOLUTION
    sql_statement = "select vend_id, prod_name from products where vend_id!=1003"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex13():
    # Write an SQL statement that SELECTs all rows from `products` table where the product prices are between 5 and 10
    # output columns: prod_name, prod_price

    ### BEGIN SOLUTION
    sql_statement = "select prod_name,prod_price from products where prod_price between 5 and 10"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex14():
    # Write an SQL statement that SELECTs all rows from the `customers` table where the customer email is empty
    # output columns: cust_id, cust_name

    ### BEGIN SOLUTION
    sql_statement = "select cust_id, cust_name from customers where cust_email is NULL"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex15():
    # Write an SQL statement that SELECTs all rows from the `products` table where the vender id is 1003 and
    # the price is less than or equal to 10. 
    # output columns: vend_id, prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "select vend_id, prod_id, prod_price, prod_name from products where vend_id=1003 and prod_price<=10"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex16():
    # Write an SQL statement that SELECTs all rows from the `products` table where the vender id is 1002 or 1003 and
    # the price is greater than or equal to 5. 
    # output columns: vend_id, prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "select vend_id, prod_id, prod_price, prod_name from products where vend_id in ('1002','1003') and prod_price>=5"
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex17():
    # Write an SQL statement that SELECTs all rows from the `products` table where the vender id is 1002 or 1003 or 1005.
    # Use the IN operator for this!
    # output columns: vend_id, prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "select vend_id, prod_id, prod_price, prod_name from products where vend_id in (1002,1003,1005)"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex18():
    # Write an SQL statement that SELECTs all rows from the `products` table where the vender id is NOT 1002 or 1003.
    # Use the NOT IN operator for this!
    # output columns: vend_id, prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "select vend_id, prod_id, prod_price, prod_name from products where vend_id not in (1002,1003)"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex19():
    # Write an SQL statement that SELECTs all rows from the `products` table where the product name starts with 'jet'
    # output columns: prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "select prod_id, prod_price, prod_name from products where prod_name like 'jet%'"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex20():
    # Write an SQL statement that SELECTs all rows from the `products` table where the product name ends with 'anvil'
    # output columns: prod_id, prod_price, prod_name

    ### BEGIN SOLUTION
    sql_statement = "select prod_id, prod_price, prod_name from products where prod_name like '%anvil'"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex21():
    # Write an SQL statement that SELECTs all rows from the `vendors` table. Concatenate vendor name and vendor country
    # as vend_title. Order by vend_title. Leave space in between -- example `ACME (USA)`
    # output columns: vend_title

    ### BEGIN SOLUTION
    sql_statement = sql_statement = "SELECT vend_name ||' ('||vend_country||')' as vend_title from vendors order by vend_title"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex22():
    # Write an SQL statement that SELECTs all rows from the `orderitems` table where order number is 20005. 
    # Display an extra calculated column called `expanded_price` that is the result of quantity multiplied by item_price.
    # Round the value to two decimal places. 
    # output columns: prod_id, quantity, item_price, expanded_price

    ### BEGIN SOLUTION
    sql_statement = "select prod_id,quantity, item_price,round(item_price*quantity,2) as expanded_price from orderitems where order_num=20005 "
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex23():
    # Write an SQL statement that SELECTs all rows from the `orders` table where the order date is between 
    # 2005-09-13 and 2005-10-04
    # output columns: order_num, order_date
    # https://www.sqlitetutorial.net/sqlite-date-functions/sqlite-date-function/
    
    ### BEGIN SOLUTION
    sql_statement = "select order_num, order_date from orders where order_date between '2005-09-13' and '2005-10-04'"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex24():
    # Write an SQL statement that calculates the average price of all rows in the `products` table. 
    # Call the average column avg_price
    # output columns: avg_price

    ### BEGIN SOLUTION
    sql_statement = "select avg(prod_price) as avg_price from products"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


def ex25():
    # Write an SQL statement that calculates the average price of all rows in the `products` table 
    # where the vendor id is 1003 . Call the average column avg_price
    # output columns: avg_price

    ### BEGIN SOLUTION
    sql_statement = "select avg(prod_price) as avg_price from products where vend_id in (1003)"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement



def ex26():
    # Write an SQL statement that counts the number of customers in the `customers` table 
    # Call the count column num_cust
    # output columns: num_cust

    ### BEGIN SOLUTION
    sql_statement = "select count(cust_id) as num_cust from  customers"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex27():
    # Write an SQL statement that calculates the max price in the `products` table 
    # Call the max column max_price. Round the value to two decimal places. 
    # output columns: max_price

    ### BEGIN SOLUTION
    sql_statement = "select max(prod_price ) as max_price   from products"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex28():
    # Write an SQL statement that calculates the min price in the `products` table 
    # Call the min column min_price. Round the value to two decimal places. 
    # output columns: min_price

    ### BEGIN SOLUTION
    sql_statement = "select round(min(prod_price),2) as min_price    from products"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement

def ex29():
    # Write an SQL statement that sums the quantity in the `orderitems` table where order number is 20005. 
    # Call the sum column items_ordered
    # output columns: items_ordered

    ### BEGIN SOLUTION
    sql_statement = "select sum(quantity) as items_ordered from orderitems where order_num=20005"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn_orders)
    # display(df)
    return sql_statement


#---------------------------------------------------------------------------------------------------------------------------------------------#

# You cannot use Pandas! I will deduct points after manual check if you use Pandas. You CANNOT use the 'csv' module to read the file

# Hint: Ensure to strip all strings so there is no space in them

# DO NOT use StudentID from the non_normalized table. Let the normalized table automatically handle StudentID. 


def create_connection(db_file, delete_db=False):
    import os
    if delete_db and os.path.exists(db_file):
        os.remove(db_file)

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        conn.execute("PRAGMA foreign_keys = 1")
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)
        
def execute_sql_statement(sql_statement, conn):
    cur = conn.cursor()
    cur.execute(sql_statement)

    rows = cur.fetchall()

    return rows

# conn_non_normalized = create_connection('non_normalized.db')
# sql_statement = "select * from Students;"
# df = pd.read_sql_query(sql_statement, conn_non_normalized)
# display(df)


def normalize_database(non_normalized_db_filename):
#     Normalize 'non_normalized.db'
#     Call the normalized database 'normalized.db'
#     Function Output: No outputs
#     Requirements:
#     Create four tables
#     Degrees table has one column:
#         [Degree] column is the primary key
    
#     Exams table has two columns:
#         [Exam] column is the primary key column
#         [Year] column stores the exam year
    
#     Students table has four columns:
#         [StudentID] primary key column 
#         [First_Name] stores first name
#         [Last_Name] stores last name
#         [Degree] foreign key to Degrees table
        
#     StudentExamScores table has four columns:
#         [PK] primary key column,
#         [StudentID] foreign key to Students table,
#         [Exam] foreign key to Exams table ,
#         [Score] exam score

    
    ### BEGIN SOLUTION
    conn=create_connection("normalized.db")
    Degrees = "CREATE TABLE IF NOT EXISTS Degrees(Degree text PRIMARY KEY)"
    Students = "CREATE TABLE IF NOT EXISTS Students(StudentID integer PRIMARY KEY,First_Name text,Last_Name text, Degree text,   FOREIGN KEY (Degree) REFERENCES Degrees(Degree) )"
    StudentExamScores = "CREATE TABLE IF NOT EXISTS StudentExamScores(PK integer PRIMARY KEY,StudentID integer,Exam text,Score real,FOREIGN KEY(StudentID)REFERENCES Students(StudentID),FOREIGN KEY(Exam)REFERENCES Exams(Exam) )"
    Exams = "CREATE TABLE IF NOT EXISTS Exams(Exam text PRIMARY KEY,Year integer )"
    create_table(conn,Degrees)
    create_table(conn,Exams)
    create_table(conn,Students)
    create_table(conn,StudentExamScores)
    conn2=create_connection("non_normalized.db")
    data=execute_sql_statement("select *from students", conn2)
    degrees=[]
    for row in data:
        degrees.append(row[2])
    unique_degree=list(set(degrees))
    for data2 in unique_degree:
        degree_tb=f'INSERT OR IGNORE INTO DEGREES(Degree) VALUES("{data2}")'
        execute_sql_statement(degree_tb, conn)
    exam=dict()
    exam_year=[]
    for i in data:
        tt=i[3].split(",")
        for j in tt:
            ff=j.split("(")
            rr=(ff[0].strip(" "))
            nn=ff[1].strip(")")
            exam.update({rr:int(nn)})
    for exam,year in exam.items():
        Exams_tb=f'INSERT OR IGNORE INTO Exams(Exam,Year) VALUES("{exam}",{year})'
        execute_sql_statement(Exams_tb, conn)
    degrees=[]
    exam=[]
    scores=[]
    student_id=[]
    for row in data:
        degree=row[2] 
    for row in data:
        #below statement is to put student id into Studnets and Student Exam scores
        StudemtID=int(row[0])
        last_name,first_name=row[1].split(",")
        last_name=last_name.strip()
        first_name=first_name.strip()
        degree=row[2]
        student_tb=f'INSERT OR IGNORE INTO STUDENTS(StudentID,First_Name,Last_Name,Degree) VALUES({StudemtID},"{first_name}","{last_name}","{degree}")'
        execute_sql_statement(student_tb, conn)
        #Exam Scores
        tt=row[3].split(",")
        for j in tt:
            ff=j.split("(")
            rr=(ff[0].strip(" "))
            nn=ff[1].strip(")")
            exam.append(rr)
            student_id.append(row[0])
        tr=row[4].split(",")
        for p in tr:
            scores.append(p.strip())
    for i in range(1,len(student_id)+1):
        examscores_tb=f'INSERT OR IGNORE INTO StudentExamScores(PK,StudentID,Exam,Score) VALUES({i},{student_id[i-1]},"{exam[i-1]}",{scores[i-1]})'
        execute_sql_statement(examscores_tb, conn)
    conn.commit()
    pass
    ### END SOLUTION
        
    
# normalize_database('non_normalized.db')
# conn_normalized = create_connection('normalized.db')

def ex30(conn):
    # Write an SQL statement that SELECTs all rows from the `Exams` table and sort the exams by Year
    # output columns: exam, year
    
    ### BEGIN SOLUTION
    sql_statement = "select exam,year from Exams order by year,exam"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn)
    # display(df)
    return sql_statement


def ex31(conn):
    # Write an SQL statement that SELECTs all rows from the `Degrees` table and sort the degrees by name
    # output columns: degree
    
    ### BEGIN SOLUTION
    sql_statement = "select degree from degrees order by degree"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn)
    # display(df)
    return sql_statement


def ex32(conn):
    # Write an SQL statement that counts the numbers of gradate and undergraduate students
    # output columns: degree, count_degree
    
    ### BEGIN SOLUTION
    sql_statement = "SELECT Degree, COUNT(*) AS count_degree FROM Students GROUP BY Degree;"
    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn)
    # display(df)
    return sql_statement


def ex33(conn):
    # Write an SQL statement that calculates the exam averages for exams; sort by average in descending order.
    # output columns: exam, year, average
    # round to two decimal places
    
    
    ### BEGIN SOLUTION
    sql_statement = "select e.exam, year,round(avg(score),2) as average from exams e inner join studentexamscores ses on e.exam=ses.exam group by year,e.exam order by average desc;"

    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn)
    # display(df)
    return sql_statement


def ex34(conn):
    # Write an SQL statement that calculates the exam averages for degrees; sort by average in descending order.
    # output columns: degree, average 
    # round to two decimal places
    
    ### BEGIN SOLUTION
    sql_statement = "SELECT s.degree,ROUND(AVG(ses.score), 2) AS average FROM students s INNER JOIN studentexamscores ses ON s.studentid = ses.studentid GROUP BY s.degree;"

    ### END SOLUTION
    # df = pd.read_sql_query(sql_statement, conn)
    # display(df)
    return sql_statement

def ex35(conn):
    # Write an SQL statement that calculates the exam averages for students; sort by average in descending order. Show only top 10 students
    # output columns: first_name, last_name, degree, average
    # round to two decimal places
    # Order by average in descending order
    # Warning two of the students have the same average!!!
    
    ### BEGIN SOLUTION
    sql_statement = "select s.first_name,s.last_name,s.degree,round(avg(ses.score), 2) as average from students s inner join studentexamscores ses on s.studentid=ses.studentid group by s.last_name,s.first_name,s.degree order by average desc limit 10;"
    ### END SOLUTION 
    # df = pd.read_sql_query(sql_statement, conn)
    # display(df)
    return sql_statement
