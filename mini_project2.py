### Utility Functions
import pandas as pd
import sqlite3
from sqlite3 import Error

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


def create_table(conn, create_table_sql, drop_table_name=None):
    
    if drop_table_name: # You can optionally pass drop_table_name to drop the table. 
        try:
            c = conn.cursor()
            c.execute("""DROP TABLE IF EXISTS %s""" % (drop_table_name))
        except Error as e:
            print(e)
    
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

def step1_create_region_table(data_filename, normalized_database_filename):
    # Inputs: Name of the data and normalized database filename
    # Output: Nones
    
    ### BEGIN SOLUTION
    with open(data_filename, 'r') as file:
    # skip header row if it exists
        lines=file.readlines()
        global name,address,city,region,county_region,country,a,b,c,d,e,f,prod_name9,prod_price9,prod_catg9
        county_region=dict()
        name=[]
        address=[]
        city=[]
        country=[]
        region=[]
        prod_name9=[]
        prod_price9=[]
        prod_catg9=[]
        for i in lines:
            name.append(i.split('\t')[0])
            address.append(i.split('\t')[1])
            city.append(i.split('\t')[2])
            county_region[i.split('\t')[3]]=i.split('\t')[4]
            country.append(i.split('\t')[3])
            region.append(i.split('\t')[4])
            a=((i.split('\t')[5]).split(';'))
            b=((i.split('\t')[6]).split(';'))
            c=((i.split('\t')[7]).split(';'))
            d=((i.split('\t')[8]).split(';'))
            e=((i.split('\t')[9]).split(';'))
            f=((i.split('\t')[10]).split(';'))
            prod_name9.append(i.split('\t')[5].split(';'))
            prod_price9.append(i.split('\t')[8].split(';'))
            prod_catg9.append(i.split('\t')[6].split(';'))
        region=region[1:]
        region=list(set(region))
        region.sort()
        global region_diction
        region_diction = dict()
        for i in range(len(region)):
            temp=region[i]
            region_diction[temp]=i+1
        conn=create_connection(normalized_database_filename)
        Region = '''CREATE TABLE IF NOT EXISTS Region(
            RegionID integer primary key,
            Region text not null)''' 
        create_table(conn, Region, drop_table_name=None)
        for key,value in region_diction.items():
            execute_sql_statement(f'INSERT OR IGNORE INTO Region(RegionID,Region) Values({value},"{key}")',conn)
        conn.commit()


    ### END SOLUTION

def step2_create_region_to_regionid_dictionary(normalized_database_filename):
    
    
    ### BEGIN SOLUTION
    return region_diction;
    pass

    ### END SOLUTION


def step3_create_country_table(data_filename, normalized_database_filename):
    # Inputs: Name of the data and normalized database filename
    # Output: None
    
    ### BEGIN SOLUTION
    conn=create_connection(normalized_database_filename)
    Country = '''CREATE TABLE IF NOT EXISTS Country(
            CountryID integer primary key,
            Country text not null,
            RegionID integer not null,
            FOREIGN KEY (RegionID) REFERENCES Region (RegionID))'''
    create_table(conn, Country, drop_table_name=None)
    del county_region['Country']
    country_region=dict()
    for key,value in county_region.items():
        country_region[key]=region_diction[value]
    country_region_sort=dict()
    sorted_keys = sorted(country_region.keys())
    for key in sorted_keys:
        country_region_sort[key]=country_region[key]
    counter=1
    for key,value in country_region_sort.items():
        execute_sql_statement(f'INSERT OR IGNORE INTO Country(CountryID,Country,RegionID) Values({counter},"{key}",{value})',conn)
        counter=counter+1
    conn.commit()
    pass
    ### END SOLUTION


def step4_create_country_to_countryid_dictionary(normalized_database_filename):
    
    
    ### BEGIN SOLUTION
    pass
    conn = create_connection(normalized_database_filename)
    countryID = execute_sql_statement("select CountryID from Country", conn)
    countries = execute_sql_statement("select Country from Country", conn)
    global step4_country_dict
    step4_country_dict = {}
    for i in range(len(countries)):
        step4_country_dict[countries[i][0]] = countryID[i][0]
    return step4_country_dict
    ### END SOLUTION
        
        
def step5_create_customer_table(data_filename, normalized_database_filename):

    ### BEGIN SOLUTION
    conn=create_connection(normalized_database_filename)
    Customer = '''CREATE TABLE IF NOT EXISTS Customer(
            CustomerID integer primary key,
            FirstName text not null,
            LastName text not null,
            Address text not null,
            City text not null,
            CountryID integer not null,
            FOREIGN KEY (CountryID) REFERENCES Country(CountryID))'''
    create_table(conn, Customer, drop_table_name=None)
    name2=name[1:]
    first_name=[]
    last_name=[]
    for i in name2:
        temp=i.split(" ")
        if len(temp)>2:
            middle_name=temp[1:]
            lastname=" ".join(middle_name)
            first_name.append(temp[0])
            last_name.append(lastname)
        else:
            first_name.append(temp[0])
            last_name.append(temp[1])
    country2=country[1:]
    address2=address[1:]
    city2=city[1:]
    country_id_1=[]
    for i in country2:
        country_id_1.append(step4_country_dict[i])
    counter=1
    cust_list=list(zip(first_name,last_name,address2,city2,country_id_1))
    cust_list.sort()
    for i in cust_list:
        execute_sql_statement(f'INSERT OR IGNORE INTO CUSTOMER(CustomerID,Firstname,lastname,address,city,countryID) values ({counter},"{i[0]}","{i[1]}","{i[2]}","{i[3]}","{i[4]}")',conn)
        counter=counter+1
    conn.commit()
    pass

    ### END SOLUTION


def step6_create_customer_to_customerid_dictionary(normalized_database_filename):
    
    
    ### BEGIN SOLUTION
    conn = create_connection(normalized_database_filename)
    first_name=execute_sql_statement("select FirstName from Customer", conn)
    last_name = execute_sql_statement("select LastName from Customer", conn)
    custId_list = execute_sql_statement("select CustomerID from Customer", conn)
    full_name=[]
    global step6_create_cust
    step6_create_cust=dict()
    full_name = [f"{first_name[i][0]} {last_name[i][0]}" for i in range(len(last_name))]
    step6_create_cust = {full_name[i]: custId_list[i][0] for i in range(len(full_name))}
    return step6_create_cust

    ### END SOLUTION
        
def step7_create_productcategory_table(data_filename, normalized_database_filename):
    # Inputs: Name of the data and normalized database filename
    # Output: None

    
    ### BEGIN SOLUTION
    conn=create_connection(normalized_database_filename)
    ProductCategory = '''CREATE TABLE IF NOT EXISTS ProductCategory (
            ProductCategoryID integer primary key,
            ProductCategory text,
            ProductCategoryDescription text)'''
    
    create_table(conn, ProductCategory,drop_table_name=None)
    temp2323=list(zip(a,b,c,d,e,f))
    product_name=[]
    product_cat=[]
    product_desc=[]
    product_price=[]
    product_qty=[]
    product_date=[]
    for i in range(len(temp2323)):
        product_name.append(temp2323[i][0])
        product_cat.append(temp2323[i][1])
        product_desc.append(temp2323[i][2])
        product_price.append(temp2323[i][3])
        product_qty.append(temp2323[i][4])
        product_date.append(temp2323[i][5])
    temp2=list(zip(product_cat,product_desc))
    temp2.sort()
    unique_data = set()
    for item in temp2:
        if item not in unique_data:
            unique_data.add(item)

    unique_data=list(unique_data)
    unique_data.sort()
    for i in range(len(unique_data)):
        execute_sql_statement(f'INSERT OR IGNORE INTO productcategory(ProductCategoryID,ProductCategory,ProductCategoryDescription) values ({i+1},"{unique_data[i][0]}","{unique_data[i][1]}")',conn)
    conn.commit()
   
    ### END SOLUTION

def step8_create_productcategory_to_productcategoryid_dictionary(normalized_database_filename):
    
    
    ### BEGIN SOLUTION
    pass
    conn=create_connection(normalized_database_filename)
    ProductCategoryIDs=execute_sql_statement("select ProductCategoryID from ProductCategory", conn)
    ProductCategory=execute_sql_statement("select ProductCategory from ProductCategory", conn)
    step8_create_prodcatg=dict()
    for i in range(len(ProductCategoryIDs)):
        step8_create_prodcatg[ProductCategory[i][0]]=ProductCategoryIDs[i][0]
    return step8_create_prodcatg
    ### END SOLUTION
        

def step9_create_product_table(data_filename, normalized_database_filename):
    # Inputs: Name of the data and normalized database filename
    # Output: None

    
    ### BEGIN SOLUTION
    
    step8_create_prodcatg=step8_create_productcategory_to_productcategoryid_dictionary(normalized_database_filename)
    conn=create_connection(normalized_database_filename)
    Product = '''CREATE TABLE IF NOT EXISTS Product(
            ProductID integer primary key,
            ProductName text,
            ProductUnitPrice real,
            ProductCategoryID integer,
            FOREIGN KEY (ProductCategoryID) REFERENCES ProductCategory (ProductCategoryID))'''
    create_table(conn, Product,drop_table_name=None)
    temp112=list(zip(prod_name9,prod_price9,prod_catg9))
    temp113=temp112.pop()
    prod_catg_=[]
    prod_name_=[]
    prod_price_=[]
    for i in range(len(temp113[0])):
        if temp113[0][i] not in prod_name_:
            prod_name_.append(temp113[0][i])
            prod_catg_.append(temp113[1][i])
            prod_price_.append(temp113[2][i])
        else:
            continue
    sorted_lists = sorted(zip(prod_name_, prod_catg_, prod_price_), key=lambda x: x[0])

    prod_name_, prod_catg_, prod_price_ = zip(*sorted_lists)
    counter=1
    for i in range(len(prod_name_)):
        execute_sql_statement(f'INSERT OR IGNORE INTO Product(ProductID,ProductName,ProductUnitPrice,ProductCategoryID) VALUES({counter},"{prod_name_[i]}",{float(prod_catg_[i])},{step8_create_prodcatg[prod_price_[i]]})',conn)
        counter+=1
    conn.commit()
   
    ### END SOLUTION


def step10_create_product_to_productid_dictionary(normalized_database_filename):
    
    ### BEGIN SOLUTION
    conn = create_connection(normalized_database_filename)
    prodid_list = execute_sql_statement("select productid from product", conn)
    prodname_list = execute_sql_statement("select productname from product", conn)
    global step10_create_prod_dict
    step10_create_prod_dict=dict()
    for i in range(len(prodname_list)):
        step10_create_prod_dict[prodname_list[i][0]] = prodid_list[i][0]
    return step10_create_prod_dict


    ### END SOLUTION
        

def step11_create_orderdetail_table(data_filename, normalized_database_filename):
    # Inputs: Name of the data and normalized database filename
    # Output: None

    import datetime 
    ### BEGIN SOLUTION
    pass
    conn=create_connection(normalized_database_filename)
    OrderDetail = '''CREATE TABLE IF NOT EXISTS OrderDetail (
            OrderID integer primary key,
            CustomerID integer,
            ProductID integer,
            OrderDate TEXT,
            QuantityOrdered integer,
            FOREIGN KEY (CustomerID) REFERENCES Customer (CustomerID),
            FOREIGN KEY (ProductID) REFERENCES Product (ProductID))'''
    create_table(conn, OrderDetail,drop_table_name=None)
    order=[]
    with open(data_filename, 'r') as file:
        lines=file.readlines()
        for i in lines:
            temp=[]
            temp.append((i.split('\t')[0]))
            temp.append(i.split('\t')[5].split(';'))
            temp.append(i.split('\t')[10].split(';'))
            temp.append(i.split('\t')[9].split(';'))
            order.append(temp)
    new_order=order[1:]
    name__=[]
    prodid__=[]
    date__=[]
    quant__=[]
    for i in (range(91)):
        for l in range(len(new_order[i][1])):
            name__.append(step6_create_cust[new_order[i][0]])
        for j in new_order[i][1]:
            prodid__.append(step10_create_prod_dict[j])
        for k in new_order[i][2]:
            temp=k.strip()
            con_date=datetime.datetime.strptime(temp,'%Y%m%d').strftime('%Y-%m-%d')
            date__.append(con_date)
        for k in new_order[i][3]:
            quant__.append(k)
    for i in range(len(prodid__)):
        execute_sql_statement(f'INSERT OR IGNORE INTO ORDERDETAIL(ORDERID,CustomerID,ProductID,OrderDate,QuantityOrdered) VALUES({i+1},{name__[i]},{prodid__[i]},"{date__[i]}",{quant__[i]})',conn)
    conn.commit()
    ### END SOLUTION


def ex1(conn, CustomerName):
    
    # Simply, you are fetching all the rows for a given CustomerName. 
    # Write an SQL statement that selects from the OrderDetail table and joins with the Customer and Product table.
    # Pull out the following columns. 
    # Name -- concatenation of FirstName and LastName
    # ProductName
    # OrderDate
    # ProductUnitPrice
    # QuantityOrdered
    # Total -- which is calculated from multiplying ProductUnitPrice with QuantityOrdered -- round to two decimal places
    # HINT: USE customer_to_customerid_dict to map customer name to customer id and then use where clause with CustomerID
    
    ### BEGIN SOLUTION

    custiddict = step6_create_customer_to_customerid_dictionary("normalized.db")
    customer_id = custiddict[CustomerName]

    sql_statement = f'select FirstName|| " " || LastName AS Name,ProductName,OrderDate,ProductUnitPrice,QuantityOrdered,round(productunitprice*quantityordered,2) as Total FROM orderdetail o inner join customer c on o.CustomerID = c.CustomerID inner join product p ON o.productid = p.productid WHERE o.CustomerID = {customer_id}'

    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement

def ex2(conn, CustomerName):
    
    # Simply, you are summing the total for a given CustomerName. 
    # Write an SQL statement that selects from the OrderDetail table and joins with the Customer and Product table.
    # Pull out the following columns. 
    # Name -- concatenation of FirstName and LastName
    # Total -- which is calculated from multiplying ProductUnitPrice with QuantityOrdered -- sum first and then round to two decimal places
    # HINT: USE customer_to_customerid_dict to map customer name to customer id and then use where clause with CustomerID
    
    ### BEGIN SOLUTION
    custiddict = step6_create_customer_to_customerid_dictionary("normalized.db")
    customer_id = custiddict[CustomerName]

    sql_statement = f'select FirstName|| " " || LastName AS Name,round(sum(productunitprice * quantityordereD), 2) as Total FROM orderdetail o join customer c on o.customerID = c.customerID inner join product p ON o.productid = p.productid WHERE o.customerID = {customer_id}'

    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement

def ex3(conn):
    
    # Simply, find the total for all the customers
    # Write an SQL statement that selects from the OrderDetail table and joins with the Customer and Product table.
    # Pull out the following columns. 
    # Name -- concatenation of FirstName and LastName
    # Total -- which is calculated from multiplying ProductUnitPrice with QuantityOrdered -- sum first and then round to two decimal places
    # ORDER BY Total Descending 
    ### BEGIN SOLUTION

    sql_statement = f'select FirstName|| " " || LastName AS Name,round(sum(productunitprice*quantityordereD), 2) as Total FROM orderdetail o join customer c on o.customerID = c.customerID join product p ON o.productid = p.productid group by o.CustomerID order by Total desc'

    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement

def ex4(conn):
    
    # Simply, find the total for all the region
    # Write an SQL statement that selects from the OrderDetail table and joins with the Customer, Product, Country, and 
    # Region tables.
    # Pull out the following columns. 
    # Region
    # Total -- which is calculated from multiplying ProductUnitPrice with QuantityOrdered -- sum first and then round to two decimal places
    # ORDER BY Total Descending 
    ### BEGIN SOLUTION

    sql_statement = """select r.region, round(sum(p.productunitprice * od.quantityordered), 2) as Total
    FROM orderDetail od
    JOIN country co on c.countryID = co.countryID
    JOIN customer c on od.customerID = c.customerID
    INNER JOIN region r on co.regionID = r.regionID
    INNER JOIN product p on od.productID = p.productID
    group by r.regionID
    order by total desc;
    """
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement

def ex5(conn):
    
     # Simply, find the total for all the countries
    # Write an SQL statement that selects from the OrderDetail table and joins with the Customer, Product, and Country table.
    # Pull out the following columns. 
    # Country
    # CountryTotal -- which is calculated from multiplying ProductUnitPrice with QuantityOrdered -- sum first and then round
    # ORDER BY Total Descending 
    ### BEGIN SOLUTION

    sql_statement = """
    SELECT co.Country, round(sum(p.productunitprice*od.quantityordered)) as CountryTotal
    from orderDetail od
    INNER JOIN product p on od.ProductID = p.ProductID
    JOIN country co on c.CountryID = co.CountryID
    JOIN customer c on od.CustomerID = c.CustomerID
    GROUP BY co.CountryID
    ORDER BY CountryTotal DESC;
    """
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement


def ex6(conn):
    
    # Rank the countries within a region based on order total
    # Output Columns: Region, Country, CountryTotal, CountryRegionalRank
    # Hint: Round the the total
    # Hint: Sort ASC by Region
    ### BEGIN SOLUTION

    sql_statement = """
    SELECT r.Region,co.Country,ROUND(SUM(p.ProductUnitPrice * od.QuantityOrdered)) AS CountryTotal, 
    RANK() OVER (PARTITION BY r.Region ORDER BY SUM(p.ProductUnitPrice * od.QuantityOrdered) DESC) AS CountryRegionalRank
    FROM OrderDetail od
    JOIN Product p ON od.ProductID=p.ProductID
    JOIN Customer c ON od.CustomerID=c.CustomerID
    JOIN Country co ON c.CountryID=co.CountryID
    JOIN Region r ON co.RegionID=r.RegionID
    GROUP BY r.Region,co.Country
    ORDER BY r.Region ASC,CountryTotal DESC;
    """
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement



def ex7(conn):
    
   # Rank the countries within a region based on order total, BUT only select the TOP country, meaning rank = 1!
    # Output Columns: Region, Country, CountryTotal, CountryRegionalRank
    # Hint: Round the the total
    # Hint: Sort ASC by Region
    # HINT: Use "WITH"
    ### BEGIN SOLUTION

    sql_statement = """WITH CNR AS (
    SELECT r.Region, co.Country, ROUND(SUM(p.ProductUnitPrice * od.QuantityOrdered), 0) AS CountryTotal, 
           RANK() OVER (PARTITION BY r.Region ORDER BY SUM(p.ProductUnitPrice * od.QuantityOrdered) DESC) AS CountryRegionalRank
    FROM OrderDetail od
    JOIN Customer c ON od.CustomerID = c.CustomerID
    JOIN Product p ON od.ProductID = p.ProductID
    JOIN Region r ON co.RegionID = r.RegionID
    JOIN Country co ON c.CountryID = co.CountryID
    GROUP BY r.Region, co.Country
    )
    SELECT *
    FROM CNR cot
    WHERE cot.CountryRegionalRank = 1
    order by region asc"""

    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement

def ex8(conn):
    
    # Sum customer sales by Quarter and year
    # Output Columns: Quarter,Year,CustomerID,Total
    # HINT: Use "WITH"
    # Hint: Round the the total
    # HINT: YOU MUST CAST YEAR TO TYPE INTEGER!!!!
    ### BEGIN SOLUTION

    sql_statement ="""SELECT 
    'Q' || CAST((strftime('%m', od.OrderDate) - 1) / 3 + 1 AS INTEGER) AS Quarter,
    CAST(strftime('%Y', od.OrderDate) AS INTEGER) AS Year,
    od.CustomerID,
    ROUND(SUM(p.ProductUnitPrice * od.QuantityOrdered),0) AS Total 
    FROM 
    orderdetail od
    JOIN 
    product p 
    ON 
    od.ProductID = p.ProductID 
    GROUP BY 
    Quarter, 
    Year, 
    CustomerID 
    ORDER BY 
    Year ASC;
    """
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement

def ex9(conn):
    
    # Rank the customer sales by Quarter and year, but only select the top 5 customers!
    # Output Columns: Quarter, Year, CustomerID, Total
    # HINT: Use "WITH"
    # Hint: Round the the total
    # HINT: YOU MUST CAST YEAR TO TYPE INTEGER!!!!
    # HINT: You can have multiple CTE tables;
    # WITH table1 AS (), table2 AS ()
    ### BEGIN SOLUTION

    sql_statement = """WITH total_sales AS (
  SELECT 
    'Q' || CAST((strftime('%m', od.OrderDate) - 1) / 3 + 1 AS INTEGER) AS Quarter, 
    CAST(STRFTIME('%Y', OrderDate) AS INTEGER) AS Year,
    CustomerID, 
    ROUND(SUM(p.ProductUnitPrice*od.QuantityOrdered), 0) AS Total
  FROM 
    orderdetail od 
    JOIN product p ON od.ProductID = p.ProductID 
  GROUP BY 
    Quarter, 
    Year, 
    CustomerID
), rank_sales AS (
  SELECT 
    *, 
    RANK() OVER (PARTITION BY Quarter, Year ORDER BY Total DESC) AS CustomerRank 
  FROM 
    total_sales
)
SELECT 
  * 
FROM 
  rank_sales 
WHERE 
  CustomerRank <= 5 
ORDER BY 
  Year ASC;
"""
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement

def ex10(conn):
    
    # Rank the monthly sales
    # Output Columns: Quarter, Year, CustomerID, Total
    # HINT: Use "WITH"
    # Hint: Round the the total
    ### BEGIN SOLUTION

    sql_statement = """WITH MonthNum(Month, Num) AS (
    VALUES
        ('January', '01'),
        ('February', '02'),
        ('March', '03'),
        ('April', '04'),
        ('May', '05'),
        ('June', '06'),
        ('July', '07'),
        ('August', '08'),
        ('September', '09'),
        ('October', '10'),
        ('November', '11'),
        ('December', '12')
),
SalesMonth(Month, Total) AS (
    SELECT
        MonthNum.Month, 
        SUM(ROUND(ProductUnitPrice * QuantityOrdered)) AS Total
    FROM OrderDetail
    INNER JOIN Product ON OrderDetail.ProductID = Product.ProductID
    INNER JOIN MonthNum ON MonthNum.Num = strftime('%m', OrderDate)
    GROUP BY Month
)
SELECT 
    Month, 
    Total, 
    rank() OVER (ORDER BY -Total) AS TotalRank 
FROM 
    SalesMonth 
ORDER BY 
    TotalRank;
"""

    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement

def ex11(conn):
    
    # Find the MaxDaysWithoutOrder for each customer 
    # Output Columns: 
    # CustomerID,
    # FirstName,
    # LastName,
    # Country,
    # OrderDate, 
    # PreviousOrderDate,
    # MaxDaysWithoutOrder
    # order by MaxDaysWithoutOrder desc
    # HINT: Use "WITH"; I created two CTE tables
    # HINT: Use Lag

    ### BEGIN SOLUTION

    sql_statement = """
        WITH cte0 AS (
        SELECT 
            CustomerID, 
            OrderDate, 
            LEAD(OrderDate) OVER(PARTITION BY CustomerId ORDER BY OrderDate ASC) AS lea 
        FROM 
            orderdetail 
        ORDER BY 
            1 ASC, 
            2 ASC
    ),
    cte1 AS (
        SELECT DISTINCT 
            customerID, 
            OrderDate, 
            lea, 
            julianday(lea) - julianday(orderdate) AS lea_diff 
        FROM 
            cte0 
        ORDER BY 
            1 ASC, 
            2 ASC
    ),
    cte2 AS (
        SELECT 
            customerID, 
            OrderDate, 
            lea, 
            lea_diff, 
            RANK() OVER(PARTITION BY customerID ORDER BY lea_diff DESC, OrderDate ASC) AS rn  
        FROM 
            cte1 
    ),
    cte3 AS (
        SELECT 
            customerID, 
            lea, 
            OrderDate AS PreviousOrderDate, 
            lea_diff 
        FROM 
            cte2 
        WHERE 
            rn=1 
        ORDER BY 
            1 ASC, 
            2 ASC
    )
    SELECT 
        a.CustomerID as CustomerID, 
        c.FirstName, 
        c.LastName, 
        co.Country,
        lea AS OrderDate,
        PreviousOrderDate AS PreviousOrderDate, 
        a.lea_diff AS MaxDaysWithoutOrder 
    FROM 
        cte3 a
    JOIN
        customer c
    ON
        a.customerid=c.CustomerID
    JOIN 
        country co
    ON
        c.CountryID = co.CountryID 
    ORDER BY 
     MaxDaysWithoutOrder desc,a.customerid desc"""
    
    ### END SOLUTION
    df = pd.read_sql_query(sql_statement, conn)
    return sql_statement