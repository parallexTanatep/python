import sqlite3
def menu():
    global ch
    print('\tPUBG Global Invitational.S 2021 Score\n [1] Add Team & Score\n [2] Delete Score\n [3] Edit Score\n [4] Show Score \n [x] Exit the program')
    ch = input('Select menu: ')
def Week1():
        conn = sqlite3.connect (r"D:\COMED17\Tanatep_Python\Pubgscore.db")
        cursor  =  conn.cursor ()

        #cursor.execute('''CREATE TABLE Week1 (Team, Round1, Round2, Round3, Total)''')
        print('Add Team & Score Week 1')
        s_team = input('Team: ')
        print('Round1')
        s_r1 = int(input('Kill Round1: '))
        pr1 = int(input('Placement Round1: '))
        print('Round2')
        s_r2 = int(input('Kill Round2: '))
        pr2 = int(input('Placement Round2: '))
        print('Round3')
        s_r3 = int(input('Kill Round3: '))
        pr3 = int(input('Placement Round3: '))
        '''cursor.execute("""
        INSERT INTO Placement_and_kills_Week1(Team, KR1, PR1, KR2, PR2, KR3, PR3, Kill_all)
        VALUES (?,?,?,?,?,?,?,?)
        """, (s_team, s_r1, pr1, s_r2, pr2, s_r3, pr3, s_r1+s_r2+s_r3))'''
        if pr1 == 1:
            pr1 = 0+10
        elif pr1 == 2:
            pr1 = 0+6
        elif pr1 == 3:
            pr1 = 0+5
        elif pr1 == 4:
            pr1 = 0+4
        elif pr1 == 5:
            pr1 = 0+3
        elif pr1 == 6:
            pr1 = 0+2
        elif pr1 == 7:
            pr1 = 0+1
        elif pr1 == 8:
            pr1 = 0+1
        elif pr1 > 8:
            pr1 = 0+0
        if pr2 == 1:
            pr2 = 0+10
        elif pr1 == 2:
            pr2 = 0+6
        elif pr2 == 3:
            pr2 = 0+5
        elif pr2 == 4:
            pr2 = 0+4
        elif pr2 == 5:
            pr2 = 0+3
        elif pr2 == 6:
            pr2 = 0+2
        elif pr2 == 7:
            pr2 = 0+1
        elif pr2 == 8:
            pr2 = 0+1
        elif pr2 > 8:
            pr2 = 0+0
        if pr3 == 1:
            pr3 = 0+10
        elif pr3 == 2:
            pr3= 0+6
        elif pr3 == 3:
            pr3 = 0+5
        elif pr3 == 4:
            pr3 = 0+4
        elif pr3 == 5:
            pr3 = 0+3
        elif pr3 == 6:
            pr3 = 0+2
        elif pr3 == 7:
            pr3 = 0+1
        elif pr3 == 8:
            pr3 = 0+1
        elif pr3 > 8:
            pr3 = 0+0
        cursor.execute("""
        INSERT INTO Week1(Team, Round1, Round2, Round3, Total)
        VALUES (?,?,?,?,?)
        """, (s_team, s_r1+pr1, s_r2+pr2, s_r3+pr3,s_r1+pr1+s_r2+pr2+s_r3+pr3))
        conn.commit ()
        print ( 'Data entered successfully.' )
        conn . close ()
def Week2():
        conn = sqlite3.connect (r"D:\COMED17\Tanatep_Python\Pubgscore.db")
        cursor  =  conn.cursor ()
       
        print('Add Team & Score Week 2')
        s_team = input('Team: ')
        print('Round1')
        s_r1 = int(input('Kill Round1: '))
        pr1 = int(input('Placement Round1: '))
        print('Round2')
        s_r2 = int(input('Kill Round2: '))
        pr2 = int(input('Placement Round2: '))
        print('Round3')
        s_r3 = int(input('Kill Round3: '))
        pr3 = int(input('Placement Round3: '))
        cursor.execute("""
        INSERT INTO Placement_and_kills_Week2(Team, KR1, PR1, KR2, PR2, KR3, PR3)
        VALUES (?,?,?,?,?,?,?)
        """, (s_team, s_r1, pr1, s_r2, pr2, s_r3, pr3))
        if pr1 == 1:
            pr1 = 0+10
        elif pr1 == 2:
            pr1 = 0+6
        elif pr1 == 3:
            pr1 = 0+5
        elif pr1 == 4:
            pr1 = 0+4
        elif pr1 == 5:
            pr1 = 0+3
        elif pr1 == 6:
            pr1 = 0+2
        elif pr1 == 7:
            pr1 = 0+1
        elif pr1 == 8:
            pr1 = 0+1
        elif pr1 > 8:
            pr1 = 0+0
        if pr2 == 1:
            pr2 = 0+10
        elif pr1 == 2:
            pr2 = 0+6
        elif pr2 == 3:
            pr2 = 0+5
        elif pr2 == 4:
            pr2 = 0+4
        elif pr2 == 5:
            pr2 = 0+3
        elif pr2 == 6:
            pr2 = 0+2
        elif pr2 == 7:
            pr2 = 0+1
        elif pr2 == 8:
            pr2 = 0+1
        elif pr2 > 8:
            pr2 = 0+0
        if pr3 == 1:
            pr3 = 0+10
        elif pr3 == 2:
            pr3= 0+6
        elif pr3 == 3:
            pr3 = 0+5
        elif pr3 == 4:
            pr3 = 0+4
        elif pr3 == 5:
            pr3 = 0+3
        elif pr3 == 6:
            pr3 = 0+2
        elif pr3 == 7:
            pr3 = 0+1
        elif pr3 == 8:
            pr3 = 0+1
        elif pr3 > 8:
            pr3 = 0+0
        cursor.execute("""
        INSERT INTO Week2(Team, Round1, Round2, Round3, Total)
        VALUES (?,?,?,?,?)
        """, (s_team, s_r1+pr1, s_r2+pr2, s_r3+pr3,s_r1+pr1+s_r2+pr2+s_r3+pr3))
        conn.commit ()
        print ( 'Data entered successfully.' )
        conn . close ()
def Week3():
        conn = sqlite3.connect (r"D:\COMED17\Tanatep_Python\Pubgscore.db")
        cursor  =  conn.cursor ()
        
        print('Add Team & Score Week 3')
        s_team = input('Team: ')
        print('Round1')
        s_r1 = int(input('Kill Round1: '))
        pr1 = int(input('Placement Round1: '))
        print('Round2')
        s_r2 = int(input('Kill Round2: '))
        pr2 = int(input('Placement Round2: '))
        print('Round3')
        s_r3 = int(input('Kill Round3: '))
        pr3 = int(input('Placement Round3: '))
        cursor.execute("""
        INSERT INTO Placement_and_kills_Week3(Team, KR1, PR1, KR2, PR2, KR3, PR3)
        VALUES (?,?,?,?,?,?,?)
        """, (s_team, s_r1, pr1, s_r2, pr2, s_r3, pr3))
        if pr1 == 1:
            pr1 = 0+10
        elif pr1 == 2:
            pr1 = 0+6
        elif pr1 == 3:
            pr1 = 0+5
        elif pr1 == 4:
            pr1 = 0+4
        elif pr1 == 5:
            pr1 = 0+3
        elif pr1 == 6:
            pr1 = 0+2
        elif pr1 == 7:
            pr1 = 0+1
        elif pr1 == 8:
            pr1 = 0+1
        elif pr1 > 8:
            pr1 = 0+0
        if pr2 == 1:
            pr2 = 0+10
        elif pr1 == 2:
            pr2 = 0+6
        elif pr2 == 3:
            pr2 = 0+5
        elif pr2 == 4:
            pr2 = 0+4
        elif pr2 == 5:
            pr2 = 0+3
        elif pr2 == 6:
            pr2 = 0+2
        elif pr2 == 7:
            pr2 = 0+1
        elif pr2 == 8:
            pr2 = 0+1
        elif pr2 > 8:
            pr2 = 0+0
        if pr3 == 1:
            pr3 = 0+10
        elif pr3 == 2:
            pr3= 0+6
        elif pr3 == 3:
            pr3 = 0+5
        elif pr3 == 4:
            pr3 = 0+4
        elif pr3 == 5:
            pr3 = 0+3
        elif pr3 == 6:
            pr3 = 0+2
        elif pr3 == 7:
            pr3 = 0+1
        elif pr3 == 8:
            pr3 = 0+1
        elif pr3 > 8:
            pr3 = 0+0
        cursor.execute("""
        INSERT INTO Week3(Team, Round1, Round2, Round3, Total)
        VALUES (?,?,?,?,?)
        """, (s_team, s_r1+pr1, s_r2+pr2, s_r3+pr3,s_r1+pr1+s_r2+pr2+s_r3+pr3))
        conn.commit ()
        print ( 'Data entered successfully.' )
        conn . close ()
def deletescore1():
    conn = sqlite3.connect (r"D:\COMED17\Tanatep_Python\Pubgscore.db")
    cursor  =  conn.cursor ()
    teamdel1 = input('Enter Team name you want to delete: ')
    cursor.execute('DELETE FROM Week1 WHERE Team = ?',(teamdel1,))
    cursor.execute('DELETE FROM Placement_and_kills_Week1  WHERE Team = ?',(teamdel1,))
    conn.commit ()
    print('successfully')
    conn.close ()
def deletescore2():
    conn = sqlite3.connect (r"D:\COMED17\Tanatep_Python\Pubgscore.db")
    cursor  =  conn.cursor ()
    teamdel2 = input('Enter Team name you want to delete: ')
    cursor.execute('DELETE FROM Week2 WHERE Team = ?',(teamdel2,))
    cursor.execute('DELETE FROM Placement_and_kills_Week2  WHERE Team = ?',(teamdel2,))
    conn.commit ()
    print('successfully')
    conn.close ()
def deletescore3():
    conn = sqlite3.connect (r"D:\COMED17\Tanatep_Python\Pubgscore.db")
    cursor  =  conn.cursor ()
    teamdel3 = input('Enter Team name you want to delete: ')
    cursor.execute('DELETE FROM Week3 WHERE Team = ?',(teamdel3,))
    cursor.execute('DELETE FROM Placement_and_kills_Week3  WHERE Team = ?',(teamdel3,))
    conn.commit ()
    print('successfully')
    conn.close ()
def editscore1():
    conn = sqlite3.connect (r"D:\COMED17\Tanatep_Python\Pubgscore.db")
    cursor  =  conn.cursor ()
    edt1 = str(input('Team name you want to edit: '))
    edkr1 = int(input('Edit kill round1: '))
    edpr1 = int(input('Edit placement round1: '))
    edkr2 = int(input('Edit kill round2: '))
    edpr2 = int(input('Edit placement round2: '))
    edkr3 = int(input('Edit kill round3: '))
    edpr3 = int(input('Edit placement round3: '))
    cursor.execute('''UPDATE Placement_and_kills_Week1 SET KR1=?, PR1=?, KR2=?, PR2=?, KR3=?, PR3=? WHERE Team = ?''',(edkr1, edpr1,edkr2, edpr2,edkr3, edpr3,edt1,))
    if edpr1 == 1:
        edpr1 = 0+10
    elif edpr1 == 2:
        edpr1 = 0+6
    elif edpr1 == 3:
        edpr1 = 0+5
    elif edpr1 == 4:
        edpr1 = 0+4
    elif edpr1 == 5:
        edpr1 = 0+3
    elif edpr1 == 6:
        edpr1 = 0+2
    elif edpr1 == 7:
        edpr1 = 0+1
    elif edpr1 == 8:
        edpr1 = 0+1
    elif edpr1 > 8:
        edpr1 = 0+0
    if edpr2 == 1:
        edpr2 = 0+10
    elif edpr1 == 2:
        edpr2 = 0+6
    elif edpr2 == 3:
        edpr2 = 0+5
    elif edpr2 == 4:
        edpr2 = 0+4
    elif edpr2 == 5:
        edpr2 = 0+3
    elif edpr2 == 6:
        edpr2 = 0+2
    elif edpr2 == 7:
        edpr2 = 0+1
    elif edpr2 == 8:
        edpr2 = 0+1
    elif edpr2 > 8:
        edpr2 = 0+0
    if edpr3 == 1:
        edpr3 = 0+10
    elif edpr3 == 2:
        edpr3= 0+6
    elif edpr3 == 3:
        edpr3 = 0+5
    elif edpr3 == 4:
        edpr3 = 0+4
    elif edpr3 == 5:
        edpr3 = 0+3
    elif edpr3 == 6:
        edpr3 = 0+2
    elif edpr3 == 7:
        edpr3 = 0+1
    elif edpr3 == 8:
        edpr3 = 0+1
    elif edpr3 > 8:
        edpr3 = 0+0
    cursor.execute('''UPDATE Week1 SET Round1=?, Round2=?, Round3=?, Total=? WHERE Team = ?''',(edkr1+edpr1,edkr2+edpr2,edkr3+edpr3,edkr1+edpr1+edkr2+edpr2+edkr3+edpr3,edt1,))
    conn.commit ()
    print('successfully')
    conn.close ()
def editscore2():
    conn = sqlite3.connect (r"D:\COMED17\Tanatep_Python\Pubgscore.db")
    cursor  =  conn.cursor ()
    edt1 = str(input('Team name you want to edit: '))
    edkr1 = int(input('Edit kill round1: '))
    edpr1 = int(input('Edit placement round1: '))
    edkr2 = int(input('Edit kill round2: '))
    edpr2 = int(input('Edit placement round2: '))
    edkr3 = int(input('Edit kill round3: '))
    edpr3 = int(input('Edit placement round3: '))
    cursor.execute('''UPDATE Placement_and_kills_Week2 SET KR1=?, PR1=?, KR2=?, PR2=?, KR3=?, PR3=? WHERE Team = ?''',(edkr1, edpr1,edkr2, edpr2,edkr3, edpr3,edt1,))
    if edpr1 == 1:
        edpr1 = 0+10
    elif edpr1 == 2:
        edpr1 = 0+6
    elif edpr1 == 3:
        edpr1 = 0+5
    elif edpr1 == 4:
        edpr1 = 0+4
    elif edpr1 == 5:
        edpr1 = 0+3
    elif edpr1 == 6:
        edpr1 = 0+2
    elif edpr1 == 7:
        edpr1 = 0+1
    elif edpr1 == 8:
        edpr1 = 0+1
    elif edpr1 > 8:
        edpr1 = 0+0
    if edpr2 == 1:
        edpr2 = 0+10
    elif edpr1 == 2:
        edpr2 = 0+6
    elif edpr2 == 3:
        edpr2 = 0+5
    elif edpr2 == 4:
        edpr2 = 0+4
    elif edpr2 == 5:
        edpr2 = 0+3
    elif edpr2 == 6:
        edpr2 = 0+2
    elif edpr2 == 7:
        edpr2 = 0+1
    elif edpr2 == 8:
        edpr2 = 0+1
    elif edpr2 > 8:
        edpr2 = 0+0
    if edpr3 == 1:
        edpr3 = 0+10
    elif edpr3 == 2:
        edpr3= 0+6
    elif edpr3 == 3:
        edpr3 = 0+5
    elif edpr3 == 4:
        edpr3 = 0+4
    elif edpr3 == 5:
        edpr3 = 0+3
    elif edpr3 == 6:
        edpr3 = 0+2
    elif edpr3 == 7:
        edpr3 = 0+1
    elif edpr3 == 8:
        edpr3 = 0+1
    elif edpr3 > 8:
        edpr3 = 0+0
    cursor.execute('''UPDATE Week2 SET Round1=?, Round2=?, Round3=?, Total=? WHERE Team = ?''',(edkr1+edpr1,edkr2+edpr2,edkr3+edpr3,edkr1+edpr1+edkr2+edpr2+edkr3+edpr3,edt1,))
    conn.commit ()
    print('successfully')
    conn.close ()
def editscore3():
    conn = sqlite3.connect (r"D:\COMED17\Tanatep_Python\Pubgscore.db")
    cursor  =  conn.cursor ()
    edt1 = str(input('Team name you want to edit: '))
    edkr1 = int(input('Edit kill round1: '))
    edpr1 = int(input('Edit placement round1: '))
    edkr2 = int(input('Edit kill round2: '))
    edpr2 = int(input('Edit placement round2: '))
    edkr3 = int(input('Edit kill round3: '))
    edpr3 = int(input('Edit placement round3: '))
    cursor.execute('''UPDATE Placement_and_kills_Week3 SET KR1=?, PR1=?, KR2=?, PR2=?, KR3=?, PR3=? WHERE Team = ?''',(edkr1, edpr1,edkr2, edpr2,edkr3, edpr3,edt1,))
    if edpr1 == 1:
        edpr1 = 0+10
    elif edpr1 == 2:
        edpr1 = 0+6
    elif edpr1 == 3:
        edpr1 = 0+5
    elif edpr1 == 4:
        edpr1 = 0+4
    elif edpr1 == 5:
        edpr1 = 0+3
    elif edpr1 == 6:
        edpr1 = 0+2
    elif edpr1 == 7:
        edpr1 = 0+1
    elif edpr1 == 8:
        edpr1 = 0+1
    elif edpr1 > 8:
        edpr1 = 0+0
    if edpr2 == 1:
        edpr2 = 0+10
    elif edpr1 == 2:
        edpr2 = 0+6
    elif edpr2 == 3:
        edpr2 = 0+5
    elif edpr2 == 4:
        edpr2 = 0+4
    elif edpr2 == 5:
        edpr2 = 0+3
    elif edpr2 == 6:
        edpr2 = 0+2
    elif edpr2 == 7:
        edpr2 = 0+1
    elif edpr2 == 8:
        edpr2 = 0+1
    elif edpr2 > 8:
        edpr2 = 0+0
    if edpr3 == 1:
        edpr3 = 0+10
    elif edpr3 == 2:
        edpr3= 0+6
    elif edpr3 == 3:
        edpr3 = 0+5
    elif edpr3 == 4:
        edpr3 = 0+4
    elif edpr3 == 5:
        edpr3 = 0+3
    elif edpr3 == 6:
        edpr3 = 0+2
    elif edpr3 == 7:
        edpr3 = 0+1
    elif edpr3 == 8:
        edpr3 = 0+1
    elif edpr3 > 8:
        edpr3 = 0+0
    cursor.execute('''UPDATE Week3 SET Round1=?, Round2=?, Round3=?, Total=? WHERE Team = ?''',(edkr1+edpr1,edkr2+edpr2,edkr3+edpr3,edkr1+edpr1+edkr2+edpr2+edkr3+edpr3,edt1,))
    conn.commit ()
    print('successfully')
    conn.close ()
def showscore1():
    conn = sqlite3.connect (r"D:\COMED17\Tanatep_Python\Pubgscore.db")
    cursor  =  conn.cursor ()
    cursor.execute('SELECT * FROM Week1 ORDER BY Total DESC')
    cursor.execute('SELECT * FROM Placement_and_kills_Week1')
    conn.commit ()
    result = cursor.fetchall()
    y=0
    print('-'*20)
    print ("{:<5} {:<8} {:<8} ".format('No','Team','Score','Kill'))
    print('-'*20)
    for x,k in result :
        y=y+1
        print ("{:<5} {:<9} {:<8} ".format(y, x[0], x[4],k[1]))
        #print(y,x[0],'Score:',x[4])
    print('-'*20)    
    conn.close ()
def showscore2():
    conn = sqlite3.connect (r"D:\COMED17\Tanatep_Python\Pubgscore.db")
    cursor  =  conn.cursor ()
    cursor.execute('SELECT * FROM Week2 ORDER BY Total DESC')
    conn.commit ()
    result = cursor.fetchall()
    y=0
    print('-'*20)
    print ("{:<5} {:<8} {:<8} ".format('No','Team','Score'))
    print('-'*20)
    for x in result :
        y=y+1
        print ("{:<5} {:<9} {:<8} ".format(y, x[0], x[4]))
        #print(y,x[0],'Score:',x[4])
    print('-'*20)    
    conn.close ()
def showscore3():
    conn = sqlite3.connect (r"D:\COMED17\Tanatep_Python\Pubgscore.db")
    cursor  =  conn.cursor ()
    cursor.execute('SELECT * FROM Week3 ORDER BY Total DESC')
    conn.commit ()
    result = cursor.fetchall()
    y=0
    print('-'*20)
    print ("{:<5} {:<8} {:<8} ".format('No','Team','Score'))
    print('-'*20)
    for x in result :
        y=y+1
        print ("{:<5} {:<9} {:<8} ".format(y, x[0], x[4]))
        #print(y,x[0],'Score:',x[4])
    print('-'*20)    
    conn.close ()
while True:
    menu()
    if ch=='x':
        f=input('You want to exit y/n: ')
        if f=='y' :
            break
        elif f=='n':
            continue
    while True:
        if ch =='1':
            print('\tSelect a week to add score.\n[1] Week1\n[2] Week2\n[3] Week3\n[4] Exit menu')
            ws = input('Select menu: ')
            if ws =='1':
                Week1()
            elif ws =='2':
                Week2()
            elif ws =='3':
                Week3()
            elif ws == '4':
                break
            
        elif ch =='2':
            print('\tSelect a week to delete score.\n[1] Week1\n[2] Week2\n[3] Week3\n[4] Exit menu')
            wsd = input('Select menu: ')
            if wsd =='1':
                deletescore1()
            elif wsd =='2':
                deletescore2()
            elif wsd =='3':
                deletescore3()
            elif wsd == '4':
                break
            
        elif ch == '3':
            print('\tSelect a week to edit score.\n[1] Week1\n[2] Week2\n[3] Week3\n[4] Exit menu')
            wse = input('Select menu: ')
            if wse =='1':
                editscore1()
            elif wse =='2':
                editscore2()
            elif wse =='3':
                editscore3()
            elif wse == '4':
                break
        elif ch == '4':
            print('\tSelect a week to show score.\n[1] Week1\n[2] Week2\n[3] Week3\n[4] Exit menu')
            wso = input('Select menu: ')
            if wso =='1':
                showscore1()
            elif wso =='2':
                showscore2()
            elif wso =='3':
                showscore3()()
            elif wso == '4':
                break
        else :
            print('Select agian')
            continue

    
