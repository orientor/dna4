from datetime import datetime
def check_name(naam):
    for i in naam:
        if not ( i.isalpha() or  i==' '):
            print("Error: Name should only contain alphabets and spaces.")
            z= input("Negro")
            return 0
    return 1

def check_name_without_space(naam):
    for i in naam:
        if not ( i.isalpha()):
            print("Error: Name should only contain alphabets.")
            return 0
    return 1

def check_positive_int(num, varname):
    if(type(num)==str):
        try:
            num = int(num)
        except ValueError:
            print('Error: {varname} should be integer')
            return 0
    if(num < 0):
        print(f"Error: {varname} should be greater than or equal to zero.")
        return 0
    return 1

def checkgz(num, varname):
    if(type(num)==str):
        try:
            num = int(num)
        except ValueError:
            print('Error: {varname} should be integer')
            return 0
    if(num <= 0):
        print(f"Error: {varname} should be greater than zero.")
        return 0
    return 1

def get_team_captain(team_name, con, cur):
    query = f"SELECT pjn from team_captain where team_name='{team_name}';"
    cur.execute(query)
    captain = None
    for row in cur:
        captain =int(row['pjn'])
    return captain

def delete_captain(team_name, con, cur):
    cpt = get_team_captain(team_name, con, cur)
    if (cpt==None):
        return 0
    query = f"DELETE FROM team_captain where team_name='{team_name}';"
    cur.execute(query)

def check_team(team_name, con, cur):
    query = f"SELECT * from team WHERE name='{team_name}';"
    cur.execute(query)
    for row in cur:
        return 1
    print("Team does not exist.")
    return 0
def check_position(position):
    if position=='forward':
        return 1
    if position=='defence':
        return 1
    if position=='midfielder':
        return 1
    if position=='goalrakshak':
        return 1
    print("Enter correct position")
    return 0
def print_table(x):
    mlen = list()
    for i in range(len(x[0])):
        temp =0
        for j in range(len(x)):
            temp = max(temp, len(str(x[j][i])))
        mlen.append(temp)
    for row in x:
        cnt=0
        for ele in row:
            print(str(ele), end='')
            print((mlen[cnt]-len(str(ele)))*' ',end='')
            print('|',end='')
            cnt+=1
        print("")

def get_player_age(dob):
    today=datetime.now()
    age=today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age
