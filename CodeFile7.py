import sqlite3

import numpy as np
import pandas as pd
from faker import Faker


def create_connection(db_file, delete_db=False):
    import os
    if delete_db and os.path.exists(db_file):
        os.remove(db_file)

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        conn.execute("PRAGMA foreign_keys = 1")
    except sqlite3.Error as e:
        print(e)

    return conn


conn = create_connection('non_normalized.db')
sql_statement = "select * from Students;"
df = pd.read_sql_query(sql_statement, conn)



def create_df_degrees(non_normalized_db_filename):
    """
    Open connection to the non-normalized database and generate a 'df_degrees' dataframe that contains only
    the degrees. See screenshot below. 
    """
    conn = sqlite3.connect(non_normalized_db_filename)
    df_deg=pd.read_sql_query("SELECT distinct(degree) FROM students", conn)
    return df_deg
    # BEGIN SOLUTION
    pass
    # END SOLUTION


def create_df_exams(non_normalized_db_filename):
    """
    Open connection to the non-normalized database and generate a 'df_exams' dataframe that contains only
    the exams. See screenshot below. Sort by exam!
    hints:
    # https://stackoverflow.com/a/16476974
    # https://stackoverflow.com/a/36108422
    """

    # BEGIN SOLUTION
    conn = create_connection('non_normalized.db')
    df_exams=pd.read_sql_query("SELECT * FROM students", conn)

    temp=df_exams["Exams"]
    exam=dict()
    global temp232
    temp232=[]
    for i in temp:
        tt=i.split(",")
        for j in tt:
            ff=j.split("(")
            rr=(ff[0].strip(" "))
            temp232.append(rr)
            nn=ff[1].strip(")")
            exam.update({rr:int(nn)})
    df_exam_year=pd.DataFrame
    global exams
    exams=[]
    years=[]
    for key,value in exam.items():
        exams.append(key)
        years.append(value)
    df_exam_year=pd.DataFrame({"Exam":exams,"Year":years})
    df_sorted = df_exam_year.sort_values('Exam').reset_index(drop=True)
    return df_sorted


    # END SOLUTION


def create_df_students(non_normalized_db_filename):
    """
    Open connection to the non-normalized database and generate a 'df_students' dataframe that contains the student
    first name, last name, and degree. You will need to add another StudentID column to do pandas merge.
    See screenshot below. 
    You can use the original StudentID from the table. 
    hint: use .split on the column name!
    """

    # BEGIN SOLUTION
    sql_query = "SELECT StudentID, Name, Degree FROM Students;"
    df_students = pd.read_sql_query(sql_query, conn)
    df_names = df_students['Name'].str.split(",", expand=True)
    new_order = [1,0] 
    df_names = df_names.reindex(columns=new_order) 
    df_names = df_names.applymap(lambda x: x.strip(" ") if isinstance(x, str) else x)
    df_students = pd.concat([df_students['StudentID'], df_names.rename(columns={0: 'Last_Name', 1: 'First_Name'}), df_students['Degree']], axis=1)
    return df_students


    # END SOLUTION


def create_df_studentexamscores(non_normalized_db_filename, df_students):
    """
    Open connection to the non-normalized database and generate a 'df_studentexamscores' dataframe that 
    contains StudentID, exam and score
    See screenshot below. 
    """

    # BEGIN SOLUTION
    conn = create_connection(non_normalized_db_filename)
    df=pd.read_sql_query('select * from students', conn)
    df["Scores"] = df["Scores"].apply(lambda x: [int(score) for score in x.split(", ")])
    df=df.explode('Scores').reset_index(drop=True)
    df['Exams']=temp232
    final_df=pd.concat([df['StudentID'],df['Exams'],df['Scores']],axis=1)
    final_df = final_df.rename(columns={
    'Exams': 'Exam',
    'Scores': 'Score'
    })
    final_df.reset_index(drop=True, inplace=True)
    return final_df
    


    # END SOLUTION


def ex1(df_exams):
    """
    return df_exams sorted by year
    """
    # BEGIN SOLUTION
    df_exams.sort_values(by="Year", inplace=True)
    # END SOLUTION
    return df_exams


def ex2(df_students):
    """
    return a df frame with the degree count
    # NOTE -- rename name the degree column to Count!!!
    """
    # BEGIN SOLUTION
    pass
    # END SOLUTION
    return df


def ex3(df_studentexamscores, df_exams):
    """
    return a datafram that merges df_studentexamscores and df_exams and finds the average of the exams. Sort
    the average in descending order. See screenshot below of the output. You have to fix up the column/index names.
    Hints:
    # https://stackoverflow.com/a/45451905
    # https://stackoverflow.com/a/11346337
    # round to two decimal places
    """

    # BEGIN SOLUTION
    pass
    # END SOLUTION
    return df


def ex4(df_studentexamscores, df_students):
    """
    return a datafram that merges df_studentexamscores and df_exams and finds the average of the degrees. Sort
    the average in descending order. See screenshot below of the output. You have to fix up the column/index names.
    Hints:
    # https://stackoverflow.com/a/45451905
    # https://stackoverflow.com/a/11346337
    # round to two decimal places
    """

    # BEGIN SOLUTION
    pass
    # END SOLUTION
    return df


def ex5(df_studentexamscores, df_students):
    """
    merge df_studentexamscores and df_students to produce the output below. The output shows the average of the top 
    10 students in descending order. 
    Hint: https://stackoverflow.com/a/20491748
    round to two decimal places

    """

    # BEGIN SOLUTION
    pass
    # END SOLUTION


# DO NOT MODIFY THIS CELL OR THE SEED

# THIS CELL IMPORTS ALL THE LIBRARIES YOU NEED!!!


np.random.seed(0)
fake = Faker()
Faker.seed(0)


def part2_step1():

    # ---- DO NOT CHANGE
    np.random.seed(0)
    fake = Faker()
    Faker.seed(0)
    # ---- DO NOT CHANGE

    # BEGIN SOLUTION
    pass
    # END SOLUTION
    


def part2_step2():

    # ---- DO NOT CHANGE
    np.random.seed(0)
    # ---- DO NOT CHANGE

    # BEGIN SOLUTION
    pass
    # END SOLUTION


def part2_step3(df2_scores):
    # BEGIN SOLUTION
    pass
    # END SOLUTION


def part2_step4(df2_students, df2_scores, ):
    # BEGIN SOLUTION
    pass
    # END SOLUTION


def part2_step5():
    # BEGIN SOLUTION
    pass
    # END SOLUTION


def part2_step6():
    # BEGIN SOLUTION
    pass
    # END SOLUTION
