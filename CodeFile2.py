def eas503_ex27(month, day):

    # The year is divided into four season: spring, summer, fall (or autumn) and winter.
    # While the exact dates that the seasons change vary a little bit from year to
    # year because of the way that the calender is constructed, we will use the following
    # dates for this exercise:

    # Season  -- First Day
    # Spring  -- March 20
    # Summer  -- June 21
    # Fall  -- September 22
    # Winter    -- December 21

    # Complete this function which takes in as inputs a month and day. It should
    # output the season.
    # input 1: month -- str
    # input 2: day -- int

    # output: month -- str (Spring, Summer, Fall, Winter)

    # BEGIN SOLUTION
    month=month.lower()
    if (month=='march' and day>=21) or (month=='april' and day>=1) or (month=='may' and day<=20) or (month=='june' and day<=20):
        return 'Spring'
    elif (month=='june' and day>=21) or (month=='july' and day>=1) or (month=='august' and day<=21) or (month=='september' and day<=21):
        return 'Summer'
    elif (month=='september' and day>=1) or (month=='october' and day>=11) or (month=='november' and day<=22) or (month=="december" and day<=21):
        return 'Fall'
    else:
        return 'Winter'
    # END SOLUTION


def eas503_ex28(year):
    # Complete this function to check if year is a leap year
    # Input: year
    # Output: True or False (Boolean)

    # BEGIN SOLUTION
    temp=False
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                temp=True
            else:
                temp=False
        else:
            temp=True
    else:
        temp=False
    return temp


    # END SOLUTION


def eas503_ex29(month, day, year):
    # Complete this function to check if a data is valid, given month, day, and year.
    # For example, 5/24/1962 is valid, but 9/31/2000 is not
    # Inputs: month, day, year
    # Output: True or False (Boolean)
    # IMPORTANT: Use the function ex28() to determine if year is leap year

    # BEGIN SOLUTION
    temp=False
    date=day
    if (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12) and date<=31:
        temp=True
    elif (month==4 or month==6 or month==9 or month==11)and date<=30:
        temp=True
    elif month==2:
        temp=eas503_ex28(year)
    else:
        temp=False
    return temp
    # END SOLUTION


def eas503_ex30(month, day, year):
    # Complete this function to calculate the day_number given month, day, and year.
    # Information: The days of the year are often numbered from 1 through 365 (or 366).
    # This number can be computed in three steps using int arithmetic:
    # (a) - day_num = 31 * (month - 1) + day
    # (b) - if the month is after February subtract (4*(month)+23)//10
    # (c) - if it's a leap year and after February 29, add 1
    # Hint: First verify the input date is valid, return False if it is not valid; use is_date_valid
    # IMPORTANT: use the functions you wrote previous, namely, ex28 and ex29.
    # Inputs: month, day, year
    # Output: the day number or False (boolean) if the date is invalid.

    # BEGIN SOLUTION
    temp=False
    temp=eas503_ex29(month,day,year)
    if temp==True:
        day_num=31*(month-1)+day
        if month>2:
            day_num=day_num-((4*(month)+23)//10)
            temp=eas503_ex28(year)
            if temp==True and (((month==2 and day>29) or month>2)):
                day_num=day_num+1
        return day_num
    else:
        temp=False 
        return temp
    
    # END SOLUTION


def eas503_ex31(plate):

    # In a particular jurisdiction, older license plates consist of three uppercase
    # letters followed by three digits. When all of the license plates following
    # that pattern had been used, the format was changed to four digits followed by
    # three uppercase letters.

    # Complete this function whose only input is a license plate and its output
    # is: 1) Older/Valid 2) Newer/Valid 3) Invalid
    # input: plate (str)
    # output: 'Older/Valid' or 'Newer/Valid' or 'Invalid'
    # HINT: Use the comparator operators (>=, <=)!

    # BEGIN SOLUTION
    if len(plate)==6:
    #Newer
        first_half=plate[0:3]
        second_half=plate[3:6]
        if first_half.isupper()==True and second_half.isnumeric()==True:
            return 'Older/Valid'
        else:
            return 'Invalid'
    elif len(plate)==7:
        first_half=plate[0:4]
        second_half=plate[4:7]
        if first_half.isnumeric()==True and second_half.isupper()==True:
            return 'Newer/Valid'
        else:
            return 'Invalid'
    #Older
    else:
    #Invalid
        False
    # END SOLUTION


def eas503_ex32(date):

    # A magic date is a date where the day multiplied by the month is equal
    # to the two digit year. For example, June 10, 1960 is a magic date because
    # June is the sixth month, and 6 times 10 is 60, which is equal to the two
    # digit year. Complete this function to determine whether or not a date is
    # a magic date.

    # input: date (str -- month/day/year) -- e.g., 06/01/2022 -- will have leading zero before month and day
    # output: True or False (bool)
    # Hint: use string indexing to extract the month, day, and year from the date string

    # BEGIN SOLUTION
    day=int(date[3:5])
    last2_digit_of_year=int(date[8:15])
    month=int(date[0:2])
    if (day*month)==last2_digit_of_year:
        return True
    else:
        return False
    # END SOLUTION

def eas503_ex33(password):
    # In this exercise you will complete this function to determine whether or not
    # a password is good. We will define a good password to be a one that is at least
    # 8 characters long and contains at least one uppercase letter, at least one lowercase
    # letter, at least one number, and at least one of the following special characters (!, @, #, $, ^).
    # This function should return True if the password
    # passed to it as its only parameter is good. Otherwise it should return False.
    #
    # input: password (str)
    # output: True or False (bool)
    # BEGIN SOLUTION
    length=len(password)
    temp1=False
    temp2=False
    temp3=False
    temp4=False
    special_chars=['!','@','#','$','^']
    for i in password:
        if i.isupper():
            temp1=True
        elif i.islower():
            temp2=True
        elif i in special_chars:
            temp3=True
        elif i.isnumeric():
            temp4=True
    if length>=9 and temp1==True and temp2==True and temp3==True and temp4==True:
        return True
    else:
        return False
    # END SOLUTION


def eas503_ex34(sentence):
    # Complete this function to calculate the average
    # word length in a sentence
    # Input: sentence
    # Output: average word length in sentence
    # Hint: count punctuations with whatever word they are `touching`
    # Hint: round the average to two decimal places

    # BEGIN SOLUTION
    s=sentence
    list1=s.split()
    list2=list(s)
    count=0
    for i in s:
        if i.isalpha() or i=='!' or i==',' or i=='.' or i=='@' or i=='(' or i==')':
            count=count+1
    return round(count/len(list1),2)
    # END SOLUTION


def eas503_ex35(filename):
    # Complete this function to count the number of lines, words, and chars in a file.
    # Input: filename
    # Output: a tuple with line count, word count, and char count -- in this order

    # BEGIN SOLUTION
    file_text  = open(filename, "r")
    line_count=0
    temp_string=''
    for i in file_text:
        line_count=line_count+1
        temp_string=temp_string+i
    temp_list=list(temp_string)
    char_count=len(temp_list)
    word_split=temp_string.split()
    word_count=len(word_split)


    return line_count,word_count,char_count
    
    
    # END SOLUTION


def eas503_ex36(apr):
    # Complete this function to use a while loop to determine how long it takes for an investment
    # to double at a given interest rate. The input to this function, apr, is the annualized interest rate
    # and the output is the number of years it takes an investment to double. Note: The amount of the initial
    # investment (principal) does not matter; you can use $1.
    # Hint: principal is the amount of money being invested.
    # apr is the annual percentage rate expressed as a decimal number.
    # Relationship: value after one year is given by principal * (1+ apr)

    # BEGIN SOLUTION
    principal = 100
    no_of_years=0
    value2=principal*2
    while principal < value2:
            principal = (principal * (1 + apr))
            no_of_years=no_of_years+1
    return no_of_years
    # END SOLUTION


def eas503_ex37(n):
    # Complete this function to return the number of steps taken to reach 1 in
    # the Collatz sequence (https://en.wikipedia.org/wiki/Collatz_conjecture) given n

    # BEGIN SOLUTION
    count=0
    while n>1:
        if n%2==0:
            n=int(n/2)
            count=count+1
        else:
            n=int((n*3)+1)
            count=count+1
    return count
    # END SOLUTION


def eas503_ex38(n):
    # A positive whole number > 2 is prime if no number between 2 and sqrt(n)
    # (include) evenly divides n. Write a program that accepts a value of n as
    # input and determine if the value is prime. If n is not prime, your program should
    # return False (boolean) as soon as it finds a value that evenly divides n.
    # Hint: if number is 2, return False

    import math

    # BEGIN SOLUTION
    if n==2:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
            else:
                continue
        return True
    # END SOLUTION


def eas503_ex39(n):
    # Complete this function to return all the primes as a list less than or equal to n
    # Input: n
    # Output: a list of numbers
    # hint use ex6

    # BEGIN SOLUTION
    no_list=[]
    for i in range(3,n+1):
        temp=eas503_ex38(i)
        if temp==True:
            no_list.append(i)
        else:
            continue
    return no_list
    # END SOLUTION


def eas503_ex40(m, n):
    # Complete this function to determine the greatest common divisor (GCD).
    # The GCD of two values can be computed using Euclid's algorithm. Starting with the values
    # m and n, we repeatedly apply the formula: n, m = m, n%m until m is 0. At this point, n is the GCD
    # of the original m and n.
    # Inputs: m and n which are both natural numbers
    # Output: gcd

    # BEGIN SOLUTION
    while m>0:
        n,m=m,n%m
    return n
    # END SOLUTION


def eas503_ex41(filename):
    # Complete this function to read grades from a file and determine the student with the highest average
    # test grades and the lowest average test grades.
    # Input: filename
    # Output: a tuple containing four elements: name of student with highest average, their average,
    # name of the student with the lowest test grade, and their average. Example ('Student1', 99.50, 'Student5', 65.50)
    # Hint: Round to two decimal places

    # BEGIN SOLUTION
    
    highest_student = ''
    lowest_student = ''
    lowest_average = 100
    highest_average = 0
    average=0
    grades=[]

    f=open(filename,'r')
    for temp in f:
            data = temp.strip().split(',')
            name = data[0]
            grades = []
            for x in data[1:]:
                grades.append(float(x))
            total=0
            count=0
            for temp in grades:
                total=total+temp
                count=count+1
            average=total/count
            average=round(average,2)

            if average > highest_average:
                    highest_average = average
                    highest_student = name
            if average < lowest_average:
                lowest_average = average
                lowest_student = name
    return (highest_student, highest_average, lowest_student, lowest_average)
    # END SOLUTION 


def eas503_ex42(data, num_outliers):
    # When analyzing data collected as a part of a science experiment it
    # may be desirable to remove the most extreme values before performing
    # other calculations. Complete this function which takes a list of
    # values and an non-negative integer, num_outliers, as its parameters.
    # The function should create a new copy of the list with the num_outliers
    # largest elements and the num_outliers smallest elements removed.
    # Then it should return teh new copy of the list as the function's only
    # result. The order of the elements in the returned list does not have to
    # match the order of the elements in the original list.
    # input1: data (list)
    # input2: num_outliers (int)

    # output: list

    # BEGIN SOLUTION
    data.sort()
    data2=data[num_outliers:-num_outliers]
    return data2
        

    # END SOLUTION


def eas503_ex43(words):
    # Complete this function to remove duplicates from the words list using a loop
    # input: words (list)
    # output: a list without duplicates
    # MUST USE loop and NOT set!
    # Preserve order

    # BEGIN SOLUTION
    final_list=[]
    for i in words:
        if i not in final_list:
            final_list.append(i)
    return final_list
    
    # END SOLUTION


def eas503_ex44(n):
    # A proper divisor ofa  positive integer, n, is a positive integer less than n which divides
    # evenly into n. Complete this function to compute all the proper divisors of a positive
    # integer. The integer is passed to this function as the only parameter. The function will
    # return a list of containing all of the proper divisors as its only result.

    # input: n (int)
    # output: list

    # BEGIN SOLUTION
    answ_list=[]
    for i in range(1,n):
        if n%i==0:
            answ_list.append(i)
        else:
            continue
    return answ_list

    # END SOLUTION


def eas503_ex45(n):
    # An integer, n, is said to be perfect when the sum of all of the proper divisors
    # of n is equal to n. For example, 28 is a perfect number because its proper divisors
    # are 1, 2, 4, 7, and 14 = 28
    # Complete this function to determine if a the number a perfect number or not.
    # input: n (int)
    # output: True or False (bool)

    # BEGIN SOLUTION
    temp=eas503_ex44(n)
    sum=0
    for i in temp:
        sum=sum+i
    if sum==n:
        return True
    else:
        return False
    # END SOLUTION


def eas503_ex46(points):
    # Complete this function to determine the best line.
    # https://www.varsitytutors.com/hotmath/hotmath_help/topics/line-of-best-fit
    # input: points (list of tuples contain x, y values)
    # output: (m, b) # round both values to two decimal places

    # BEGIN SOLUTION
    temp=points
    x=0
    y=0
    xi2=0
    xi=0
    yi=0
    xi_yi=0.0
    xi_yi2=0.0
    for i in range(len(temp)):
        a,b=temp[i]
        print(x,y)
        x=x+a
        y=y+b
    X=x/10
    Y=y/10
    for i in range(len(temp)):
        a,b=temp[i]
        xi_yi=xi_yi+(a-X)*(b-Y)
        xi_yi2=xi_yi2+(a-X)*(a-X)
    m=xi_yi/xi_yi2
    b=round(Y-m*X,2)
    m=round(m,2)
    return m,b
     
    # END SOLUTION


def eas503_ex47(title, header, data, filename):
    # This problem is hard.
    # Open up ex15_*_solution.txt and look at the output based on the input parameters, which
    # can be found in the test_assignment4.py file
    # Function inputs: 
    # title -- title of the table -- a string
    # header -- header of the table  -- a tuple
    # data -- rows of data, which is a tuple of tuples
    # filename -- name of file to write the table to
    # Your job is to create the table in the file and write it to `filename`
    # Note that you need to dynamically figure out the width of each column based on 
    # maximum possible length based on the header and data. This is what makes this problem hard. 
    # Once you have determined the maximum length of each column, make sure to pad it with 1 space
    # to the right and left. Center align all the values. 
    # OUTPUT: you are writing the table to a file

    # BEGIN SOLUTION
    header_=list(header)
    list_data = list(data)
    f_data=[]
    for i in list_data:
        temp=list(i)
        f_data.append(temp)
    f_data.append(header_)
    f_data2=[]
    for i in list_data:
        temp=list(i)
        f_data2.append(temp)

    col1=[]
    col2=[]
    col3=[]
    col4=[]
    col5=[]
    col6=[]
    for i in f_data:
        count=0
        for j in i:
            if count==0:
                col1.append(j)
                count=count+1
            elif count==1:
                col2.append(j)
                count=count+1
            elif count==2:
                col3.append(j)
                count=count+1
            elif count==3:
                col4.append(j)
                count=count+1
            elif count==4:
                col5.append(j)
                count=count+1
            elif count==5 and len(header)==6:
                col6.append(j)
                count=count+1
    col1_=[]
    for i in col1:
        temp=str(i)
        col1_.append(len(temp))
    col2_=[]
    for i in col2:
        temp=str(i)
        col2_.append(len(temp))
    col3_=[]
    for i in col3:
        temp=str(i)
        col3_.append(len(temp))
    col4_=[]
    for i in col4:
        temp=str(i)
        col4_.append(len(temp))
    col5_=[]
    for i in col5:
        temp=str(i)
        col5_.append(len(temp))
    col6_=[]
    for i in col6:
        temp=str(i)
        col6_.append(len(temp))
    max_col1=max(col1_)
    max_col2=max(col2_)
    max_col3=max(col3_)
    max_col4=max(col4_)
    max_col5=max(col5_)
    if len(header)==6:
        max_col6=max(col6_)
    else:
        max_col6=0
    max_col=[max_col1,max_col2,max_col3,max_col4,max_col5,max_col6]
    total_length=max_col1+max_col2+max_col3+max_col4+max_col5+max_col6+len(header)*2+len(header)+1
    line='-'*(total_length)
    title_= '|' + '{:^{}}'.format(title,total_length-2) + '|'
    if len(header)==6:
        line2='+'+'-'*(max_col1+2)+'+'+'-'*(max_col2+2)+'+'+'-'*(max_col3+2)+'+'+'-'*(max_col4+2)+'+'+'-'*(max_col5+2)+'+'+'-'*(max_col6+2)+'+'
    else:
        line2='+'+'-'*(max_col1+2)+'+'+'-'*(max_col2+2)+'+'+'-'*(max_col3+2)+'+'+'-'*(max_col4+2)+'+'+'-'*(max_col5+2)+'+'
    head = ''.join('| {:^{}} '.format(header[i], max_col[i]) for i in range(len(header)))
    head += '|'
    row=""
    final_row=""
    count=1
    for i in f_data2:
        for j in range(len(header)):
            row=row+'| {:^{}} '.format(i[j], max_col[j]).center(max_col[j])
        if len(data)>count:
            final_row=final_row+row+"|\n"
            row=""
            count+=1
        else:
            final_row=final_row+row+"|"
            row=""
            count+=1
        file_content = '\n'.join((line,title_,line2,head,line2,final_row,line2))
    with open(filename, 'w') as file:
        file.write(file_content)


    pass
    # END SOLUTION

def eas503_ex48(filename):
    """
    In this problem you will read data from a file and perform a simple mathematical operation on each data point. 
    Each line is supposed to contain a floating point number.
    But what you will observe is that some lines might have erroneous entries. 
    You need to ignore those lines (Hint: Use Exception handling).

    The idea is to implement a function which reads in a file and computes the median 
    of the numbers and returns the output. You may use the inbuilt function sort when computing the median.

    DO NOT USE ANY INBUILT OR OTHER FUNCTION TO DIRECTLY COMPUTE MEDIAN

    """
    list1 = []
    temp2=0
    f=open(filename,'r')
    temp = f.readlines()
    for i in temp:
        try:
            temp2 = float(i)
            list1.append(temp2)
        except:
            pass
    list1.sort()
    n = len(list1)
    if any(list1)==True:
        list1.sort()
        no_of_elements=int(len(list1))
        if no_of_elements%2==0:
            median=(list1[no_of_elements//2]+list1[no_of_elements//2-1])/2
        else:
            median=list1[(no_of_elements//2)]
        return median
    else:
        return 'The file does not have any valid number to compute the median'
    ### END SOLUTION