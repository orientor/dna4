import subprocess as sp
import pymysql
import pymysql.cursors
from aditya import *
from suyash import *
from tushar import *
from aditya_q import *
from suyash_q import *
from tushar_q import *

def option2():
    """
    Function to implement option 1
    """
    print("Not implemented")


def option3():
    """
    Function to implement option 2
    """
    print("Not implemented")


def option4():
    """
    Function to implement option 3
    """
    print("Not implemented")


def hireAnEmployee():
    """
    This is a sample function implemented for the refrence.
    This example is related to the Employee Database.
    In addition to taking input, you are required to handle domain errors as well
    For example: the SSN should be only 9 characters long
    Sex should be only M or F
    If you choose to take Super_SSN, you need to make sure the foreign key constraint is satisfied
    HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
    """
    try:
        # Takes emplyee details as input
        row = {}
        print("Enter new employee's details: ")
        name = (input("Name (Fname Minit Lname): ")).split(' ')
        row["Fname"] = name[0]
        row["Minit"] = name[1]
        row["Lname"] = name[2]
        row["Ssn"] = input("SSN: ")
        row["Bdate"] = input("Birth Date (YYYY-MM-DD): ")
        row["Address"] = input("Address: ")
        row["Sex"] = input("Sex: ")
        row["Salary"] = float(input("Salary: "))
        row["Dno"] = int(input("Dno: "))

        query = "INSERT INTO EMPLOYEE(Fname, Minit, Lname, Ssn, Bdate, Address, Sex, Salary, Dno) VALUES('%s', '%c', '%s', '%s', '%s', '%s', '%c', %f, %d)" % (
            row["Fname"], row["Minit"], row["Lname"], row["Ssn"], row["Bdate"], row["Address"], row["Sex"], row["Salary"], row["Dno"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return
def dispatch(ch, con, cur):
    """
    Function that maps helper functions to option entered
    """

    if(ch == 1):
        query_1(con,cur)
    elif(ch == 2):
        query_2(con,cur)
    elif(ch == 3):
        query_3(con, cur)
    elif(ch == 4):
        query_4(con,cur)
    elif(ch == 6):
        query_6(con,cur)
    elif(ch == 7):
        query_7(con,cur)
    elif(ch == 11):
        query_11(con,cur)
    elif(ch==15):
        query_15(con, cur)
    elif(ch==16):
        query_16(con, cur)
    suy(ch, con, cur)
    tushar(ch, con, cur)


# Global
while(1):

    # Can be skipped if you want to hard core username and password
    #tmp = sp.call('clear', shell=True)
    username = input("Username: ")
    password = input("Password: ")
    port = int(input("Port: "))
    # Set db name accordingly which have been create by you
    # Set host to the server's address if you don't want to use local SQL server
    con = pymysql.connect(host='localhost',
      user=username,
      password=password,
      db='futsal',
      port=port,
      cursorclass=pymysql.cursors.DictCursor)
    #tmp = sp.call('clear', shell=True)

    if(con.open):
        print("Connected")
    else:
        print("Failed to connect")

    tmp = input("Enter any key to CONTINUE>")

    with con.cursor() as cur:
        while(1):
        #tmp = sp.call('clear', shell=True)
        # Here taking example of Employee Mini-world
            print("1. REGISTER A TEAM") # Hire an Employee
            print("2. KICK A TEAM") # Fire an Employee
            print("3. REGISTER A PLAYER") # Promote Employee
            print("4. DELETE A PLAYER") # Employee Statistics
            print("6. UPDATE MATCH STATUS")
            print("7. SET MATCH STATUS TO DRAW")
            print("8. REGISTER A COACH")
            print("9. REPLACE A COACH")
            print("10. REGISTER A REFEREE")
            print("11. DISCONTINUE AS A REFEREE")
            print("12. BOOK TICKET")
            print("13. ADD STADIUM")
            print("14. GOAL UPDATE")
            print("15. GET TEAM DATA(PLAYERS)")
            print("16. GET TEAMS WITH SCORE ATLEAST Y")
            print("17. GET THE HIGHEST SCORING PLAYER")
            print("18. SEARCH PLAYER BY NAME")
            print("19. SEE CHAMPIONSHIP STANDINGS TABLE")
            print("20. CHAMPIONSHIP STANDINGS OF TOP X TEAMS")
            print("21. GET TEAM STATS")
            print("22. FETCH MATCH DETAILS")
            print("23. GET COACHES OF TOP 3 TEAMS")
            print("24. CREATE STADIUM OF TOP X HIGHEST SCORING MATCHES")
            print("25. GET GOALS SCORED BY A PLAYER IN A MATCH")
            print("26. GET REFEREE DETAILS")
            print("27. GET MATCHES TO BE WATCHED BY A SPECTATOR")
            print("28. Exit")
            try:
                ch = int(input("Enter choice> "))
            except:
                print("Enter valid query!")
                continue
            if(ch==28):
                exit()
            #tmp = sp.call('clear', shell=True)
            dispatch(ch, con, cur)
