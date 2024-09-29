import os
import time
import pyfiglet
import botspeak

time.sleep(1.5)
botspeak.fancy_say("WELCOME TO CRIMINAL RECORDS MANAGEMENT SYSTEM ",font = "SMALL",width = 66)
time.sleep(2)

class DATA_TOO_SHORT_ERROR(Exception):
    pass
class DATA_TOO_LONG_ERROR(Exception):
    pass
class NULL_ERROR(Exception):
    pass
class AGE_ERROR(Exception):
    pass
class INVALID_INPUT(Exception):
    pass
class INVALID_FORMAT(Exception):
    pass
class SAME_ID(Exception):
    pass
class INVALID_RANGE(Exception):
    pass

def CHECK_ID(ID):
    if  (99999 > ID):
        raise DATA_TOO_SHORT_ERROR()
    elif(ID > 1000000):
        raise DATA_TOO_LONG_ERROR()
    else:
        pass

def CHECK_NAME(NAME):
    if len(NAME)>10:
        raise DATA_TOO_LONG_ERROR()
    else:
        pass

def CHECK_AGE(AGE):
    if (AGE < 0) or (AGE >100):
        raise AGE_ERROR()
    else:
        pass

def CHECK_CRIME(CRIME):
    if (len(CRIME)>15):
        raise DATA_TOO_LONG_ERROR()
    elif (CRIME == ""):
        raise NULL_ERROR()
    else:
        pass

def CHECK_GENDER(G):
    if G not in ["M","F"]:
        raise INVALID_INPUT()
    else:
        pass

def CHECK_DATE(DATE):
    if (len(DATE) == 10):
        if ((DATE[4] == "-") and (DATE[7] =="-")):
            L = DATE.split("-")
            Y = L[0]
            M = L[1]
            D = L[2]
            if((len(Y) == 4)and(len(M) == 2) or(len(D) == 2)):
                if((Y.isdigit() == True)and(M.isdigit() == True)and(D.isdigit() == True)):
                    if(int(Y) in range (1800,2021))and(int(M) in range(1,13)):
                        if(int(Y)%4 == 0) and (M == '02'):
                            if(int(D) in range (1,30)):
                               pass
                            else:
                                raise INVALID_INPUT()
                        elif(int(Y)%4 != 0)and(M == "02"):
                            if(int(D) in range (1,29)):
                               pass
                            else:
                                raise INVALID_INPUT()
                        else:
                            if(int(D) in range(1,32)):
                               pass
                            else:
                                raise INVALID_INPUT()
                    else:
                        raise INVALID_INPUT()
                else:
                    raise INVALID_FORMAT()
            else:
                raise INVALID_FORMAT()
        else:
            raise INVALID_FORMAT()
    else:
        raise INVALID_FORMAT()


def CHECK_VERDICT(VER):
    if len(VER)> 50:
        raise DATA_TOO_LONG_ERROR()
    else:
        pass
    
    
def CHECK_RANGE(FROM,TO):
    if(FROM<=TO):
        pass
    else:
        raise INVALID_RANGE()


import mysql.connector
D = mysql.connector.connect(host = "localhost",user = "root" , passwd = "") #Enter Passvorh here <>
C = D.cursor()
C.execute("CREATE DATABASE IF NOT EXISTS ") #Enter database name here (after EXISTS)
C.execute("USE ") #again..enter the name of data base (same as above)
C.execute("SHOW TABLES")
count = 0
for i in C:
    if (i[0] == "crime_management"):
        count += 1
if (count == 0):
    C.execute('''CREATE TABLE crime_management
( ID              INT         PRIMARY KEY,
  FIRST_NAME      CHAR(10)       NOT NULL,
  MIDDLE_NAME     CHAR(10)               ,
  LAST_NAME       CHAR(10)       NOT NULL,
  AGE             INT            NOT NULL,
  CRIME           CHAR(15)       NOT NULL,
  GENDER          CHAR(1)        NOT NULL,
  DATE            DATE           NOT NULL,
  VERDICT         CHAR(50)       DEFAULT 'UNDECIDED' )''')

D.commit()
# ========= DATA ENTRY ===========================================================================================================

def DATA_ENTRY():
    S = ("INSERT INTO crime_management VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    try:
        ID_NUM = int(input("ENTER ID NUMBER [6 DIGIT NUMBER]:                               "))
        CHECK_ID(ID_NUM)
        counter = 0
        C.execute("SELECT *  FROM crime_management WHERE ID = (%s)",(ID_NUM,))
        for i in C:
            counter += 1
        if counter != 0:
            raise SAME_ID()

        F_Name = input("ENTER FIRST NAME [MAX 10 CHARACTERS]:                           ").upper()
        if (F_Name == ""):
            raise NULL_ERROR()
        else:
            CHECK_NAME(F_Name)

        M_Name = input("ENTER MIDDLE NAME[PRESS 'ENTER' IF NOT AVAILABLE]:              ").upper()
        if (M_Name == ""):
            M_Name = None
        else:
            CHECK_NAME(M_Name)

        L_Name = input("ENTER LAST NAME [MAX 10 CHARACTERS]:                            ").upper()
        if (L_Name == ""):
            raise NULL_ERROR()
        else:
            CHECK_NAME(L_Name)

        Age = int(input("ENTER AGE [0-100]:                                              "))
        CHECK_AGE(Age)
        
        Crime = input("ENTER CRIME [15 CHARACTERS]:                                    ").upper()
        CHECK_CRIME(Crime)
        
        Gender = input("ENTER GENDER[M/F]:                                              ").upper()
        CHECK_GENDER(Gender)

        Date = input("ENTER DATE [YYYY-MM-DD]:                                        ").upper()
        CHECK_DATE(Date)

        Verdict = input("ENTER VERDICT {MAX 50 CHAR}[PRESS 'ENTER' IF NOT AVAILABLE]:    ").upper()
        if (Verdict == ""):
            Verdict = None
        else:
            CHECK_VERDICT(Verdict)
    except SAME_ID:
        print("ID ALREADY EXISTS IN THE RECORDS. PLEASE ENTER A DIFFERENT ID NUMBER.")
        print("")
        print("")
    except ValueError:
        print("PLEASE ENTER POSITIVE INTEGERS ONLY.")
        print("")
        print("")
    except DATA_TOO_SHORT_ERROR:
        print("ENTERED DATA IS TOO SHORT. PLEASE ENTER DATA ACCORDING TO SPECIFIED LENGTH.")
        print("")
        print("")
    except DATA_TOO_LONG_ERROR:
        print("ENTERED DATA IS TOO LONG. PLEASE ENTER DATA ACCORDING TO SPECIFIED LENGTH.")
        print("")
        print("")
    except NULL_ERROR:
        print("NULL VALUES NOT ACCEPTED. PLEASE ENTER VALID DATA.")
        print("")
        print("")
    except AGE_ERROR:
        print("ENTERED AGE IS INVALID. PLEASE ENTER AGE WITHIN THE SPECIFIED RANGE.")
        print("")
        print("")
    except INVALID_INPUT:
        print("INVALID INPUT. PLEASE ENTER VALID DATA .")
        print("")
        print("")
    except INVALID_FORMAT:
        print("INVALID FORMAT. PLEASE ENTER DATA ACCORDING TO THE SPECIFIED FORMAT.")
        print("")
        print("")
    except:
        print("SOME ERROR OCCURED. PLEASE TRY AGAIN")
        print("")
        print("")
    else:
        print("")
        print("DATA ENTERED.")
        VALUES = (ID_NUM,F_Name,M_Name,L_Name,Age,Crime,Gender,Date,Verdict)
        C.execute(S,VALUES)
        D.commit()
        print("")
        print("")
# ========================================================================================================================================================================

# ========== DISPLAY ALL ==============================================================================================================================================
def DISPLAY_ALL():
    try:
        C.execute("SELECT * FROM crime_management")
        counter = 0
        for i in C:
            if(i[2] == None):
                NAME = i[1]+" "+i[3]
            else:
                NAME = i[1]+" "+i[2]+" "+i[3]
            if(i[8] == None):
                VERDICT = "DATA UNAVAILABLE"
            else:
                VERDICT = i[8]

            counter += 1
            print("(",counter,")",sep="",end = "  ")         
            print("ID NUMBER:      ",i[0])
            print("     FULL NAME:      ",NAME)
            print("     AGE      :      ",i[4])
            print("     CRIME    :      ",i[5])
            print("     GENDER   :      ",i[6])
            print("     DATE     :      ",i[7])
            print("     VERDICT  :      ",VERDICT)
            print("")
            print("")

        if (counter == 0):
            print("NO DATA HAS BEEN ENTERED IN THE DATABASE.")
            print("")
            print("")
    except:
        print("SOME ERROR OCCURED!")
        print("")
        print("")

#==============================================================================

# ========== SEARCH DATA ======================================================

def SEARCH_DATA():
    
        Q = input("""SELECT CATEGORY TO SEARCH:
 1. ID NUMBER
 2. NAME
 3. AGE
 4. CRIME
 5. GENDER
 6. DATE
 7. VERDICT
[PLEASE ENTER OPTION NUMBERS ONLY]
""")
        print("")
        if(Q == "1"):
            try:
                ID_num = int(input("ENTER ID NUMBER TO BE SEARCHED [6 DIGITS]: "))
                print("")
                CHECK_ID(ID_num)
            except ValueError:
                print("PLEASE ENTER POSITIVE INTERGERS ONLY.")
                print("")
                print("")
            except DATA_TOO_SHORT_ERROR:
                print("ENTERED DATA IS TOO SHORT. PLEASE ENTER DATA ACCORDING TO SPECIFIED LENGTH.")
                print("")
                print("")
            except DATA_TOO_LONG_ERROR:
                print("ENTERED DATA IS TOO LONG. PLEASE ENTER DATA ACCORDING TO SPECIFIED LENGTH.")
                print("")
                print("")
            except:
                print("SOME ERROR OCCURED. PLEASE TRY AGAIN.")
                print("")
                print("")
            else:
                COMM = ("SELECT* FROM crime_management WHERE ID = (%s)")
                T = (ID_num,)
                C.execute(COMM,T)
                counter = 0
                for i in C:
                    
                    if(i[2] == None):
                        NAME = i[1]+" "+i[3]
                    else:
                        NAME = i[1]+" "+i[2]+" "+i[3]
                    if(i[8] == None):
                        VERDICT = "DATA UNAVAILABLE"
                    else:
                        VERDICT = i[8]
                    counter += 1
                    print("(",counter,")",sep="",end = "  ")
                    print("ID NUMBER:      ",i[0])
                    print("     FULL NAME:      ",NAME)
                    print("     AGE      :      ",i[4])
                    print("     CRIME    :      ",i[5])
                    print("     GENDER   :      ",i[6])
                    print("     DATE     :      ",i[7])
                    print("     VERDICT  :      ",VERDICT)
                    print("")
                    print("")
                if (counter == 0):
                    print("NO DATA WITH THE GIVEN ID FOUND.")
                    print("")
                    print("")


        elif(Q == "2"):
            q = input('''SEARCH BY:
 1) FIRST NAME
 2) MIDDLE NAME
 3) LAST NAME
 4) FULL NAME
[PLEASE SELECT OPTION NUMBERS ONLY]
''')
            print("")
            if (q=="1"):
                try:
                    F_Name = input("ENTER FIRST NAME TO INITIATE DATA SEARCH [MAX 10 CHAR]: ").upper()
                    print("")
                    if (F_Name == ""):
                        raise NULL_ERROR()
                    else:
                        CHECK_NAME(F_Name)

                except DATA_TOO_LONG_ERROR:
                    print("ENTERED DATA IS TOO LONG. PLEASE ENTER DATA ACCORDING TO SPECIFIED LENGTH.")
                    print("")
                    print("")
                except NULL_ERROR:
                    print("NULL VALUES NOT ACCEPTED. PLEASE ENTER VALID DATA.")
                    print("")
                    print("")
                except:
                    print("SOME ERROR OCCURED. PLEASE TRY AGAIN.")
                    print("")
                    print("")
                else:
                    COMM = ("SELECT* FROM crime_management WHERE FIRST_NAME = (%s)")
                    T = (F_Name,)
                    C.execute(COMM,T)
                    counter = 0
                    for i in C:
                    
                        if(i[2] == None):
                            NAME = i[1]+" "+i[3]
                        else:
                            NAME = i[1]+" "+i[2]+" "+i[3]
                        if(i[8] == None):
                            VERDICT = "DATA UNAVAILABLE"
                        else:
                            VERDICT = i[8]
                        counter += 1
                        print("(",counter,")",sep="",end = "  ")
                        print("ID NUMBER:      ",i[0])
                        print("     FULL NAME:      ",NAME)
                        print("     AGE      :      ",i[4])
                        print("     CRIME    :      ",i[5])
                        print("     GENDER   :      ",i[6])
                        print("     DATE     :      ",i[7])
                        print("     VERDICT  :      ",VERDICT)
                        print("")
                        print("")
                    if (counter == 0):
                        print("NO DATA WITH THE GIVEN FIRST NAME FOUND.")
                        print("")
                        print("")



            elif (q=="2"):
                try:
                    M_Name = input('''ENTER MIDDLE NAME TO INITIATE DATA SEARCH [MAX 10 CHAR]
{PRESS 'ENTER' IF DATA OF PEOPLE WITH NO MIDDLE NAME IS TO BE SEARCHED}: ''').upper()
                    print("")
                    if (M_Name == ""):
                        M_Name = None
                    else:
                        CHECK_NAME(M_Name)

                except DATA_TOO_LONG_ERROR:
                    print("ENTERED DATA IS TOO LONG. PLEASE ENTER DATA ACCORDING TO SPECIFIED LENGTH.")
                    print("")
                    print("")
                except:
                    print("SOME ERROR OCCURED. PLEASE TRY AGAIN.")
                    print("")
                    print("")
                else:
                    if (M_Name == None):
                        COMM = ("SELECT* FROM crime_management WHERE MIDDLE_NAME IS NULL")
                        C.execute(COMM)
                    
                    else:
                        COMM = ("SELECT* FROM crime_management WHERE MIDDLE_NAME = (%s)")
                        T = (M_Name,)
                        C.execute(COMM,T)
                    print("")
                    counter = 0
                    for i in C:
                    
                        if(i[2] == None):
                            NAME = i[1]+" "+i[3]
                        else:
                            NAME = i[1]+" "+i[2]+" "+i[3]
                        if(i[8] == None):
                            VERDICT = "DATA UNAVAILABLE"
                        else:
                            VERDICT = i[8]
                        counter += 1
                        print("(",counter,")",sep="",end ="  ")
                        print("ID NUMBER:      ",i[0])
                        print("     FULL NAME:      ",NAME)
                        print("     AGE      :      ",i[4])
                        print("     CRIME    :      ",i[5])
                        print("     GENDER   :      ",i[6])
                        print("     DATE     :      ",i[7])
                        print("     VERDICT  :      ",VERDICT)
                        print("")
                        print("")
                    if (counter == 0):
                        print("NO DATA WITH THE GIVEN MIDDLE NAME FOUND.")
                        print("")
                        print("")


            elif (q=="3"):
                try:
                    L_Name = input("ENTER LAST NAME TO INITIATE DATA SEARCH [MAX 10 CHAR]: ").upper()
                    print("")
                    if (L_Name == ""):
                        raise NULL_ERROR()
                    else:
                        CHECK_NAME(L_Name)

                except DATA_TOO_LONG_ERROR:
                    print("ENTERED DATA IS TOO LONG. PLEASE ENTER DATA ACCORDING TO SPECIFIED LENGTH.")
                    print("")
                    print("")
                except NULL_ERROR:
                    print("NULL VALUES NOT ACCEPTED. PLEASE ENTER VALID DATA.")
                    print("")
                    print("")
                except:
                    print("SOME ERROR OCCURED. PLEASE TRY AGAIN.")
                    print("")
                    print("")
                else:
                    COMM = ("SELECT* FROM crime_management WHERE LAST_NAME = (%s)")
                    T = (L_Name,)
                    C.execute(COMM,T)
                    counter = 0
                    for i in C:
                    
                        if(i[2] == None):
                            NAME = i[1]+" "+i[3]
                        else:
                            NAME = i[1]+" "+i[2]+" "+i[3]
                        if(i[8] == None):
                            VERDICT = "DATA UNAVAILABLE"
                        else:
                            VERDICT = i[8]
                        counter += 1
                        print("(",counter,")",sep="",end = "  ")
                        print("ID NUMBER:      ",i[0])
                        print("     FULL NAME:      ",NAME)
                        print("     AGE      :      ",i[4])
                        print("     CRIME    :      ",i[5])
                        print("     GENDER   :      ",i[6])
                        print("     DATE     :      ",i[7])
                        print("     VERDICT  :      ",VERDICT)
                        print("")
                        print("")
                    if (counter == 0):
                        print("NO DATA WITH THE GIVEN LAST NAME FOUND.")
                        print("")
                        print("")

            elif(q == "4"):
                try:
                    Full_Name = input("ENTER FULL NAME TO INITIATE DATA SEARCH: ").upper()
                    print("")
                    C.execute("SELECT * FROM crime_management")
                    counter = 0
                    for i in C:
                        if(i[2] == None):
                            NAME = i[1]+" "+i[3]
                        else:
                            NAME = i[1]+" "+i[2]+" "+i[3]
                        if (Full_Name == NAME):
                            if(i[8] == None):
                                VERDICT = "DATA UNAVAILABLE"
                            else:
                                VERDICT = i[8]

                            counter += 1
                            print("(",counter,")",sep="",end = "  ")
                            print("ID NUMBER:      ",i[0])
                            print("     FULL NAME:      ",NAME)
                            print("     AGE      :      ",i[4])
                            print("     CRIME    :      ",i[5])
                            print("     GENDER   :      ",i[6])
                            print("     DATE     :      ",i[7])
                            print("     VERDICT  :      ",VERDICT)
                            print("")
                            print("")

                    if (counter == 0):
                        print("NO DATA WITH THE GIVEN FULL NAME WAS FOUND.")
                        print("")
                        print("")
                except:
                    print("SOME ERROR OCCURED. PLEASE TRY AGAIN")
                    print("")
                    print("")

            else:
                print("INVALID INPUT. PLEASE TRY AGAIN.")
                print("")
                print("")

        elif (Q == "3"):
            q = input('''SEARCH:
 1) SPECIFIC AGE
 2) WITHIN A RANGE
[PLEASE SELECT OPTION NUMBERS ONLY]
''')
            print("")
            if(q == "1"):
                try:
                    AGE = int(input("ENTER AGE TO BE SEARCHED [1-100]: "))
                    print("")
                    CHECK_AGE(AGE)
                except AGE_ERROR:
                    print("ENTERED AGE IS INVALID. PLEASE ENTER AGE WITHIN THE SPECIFIED RANGE.")
                    print("")
                    print("")
                except ValueError:
                    print("PLEASE ENTER POSITIVE INTEGERS ONLY.")
                    print("")
                    print("")
                except:
                    print("SOME ERROR OCCURED. PLEASE TRY AGAIN.")
                    print("")
                    print("")
                else:
                    COMM = "SELECT * FROM crime_management WHERE AGE = (%s)"
                    T = (AGE,)
                    C.execute(COMM,T)
                    counter = 0
                    for i in C:
                        if(i[2] == None):
                            NAME = i[1]+" "+i[3]
                        else:
                            NAME = i[1]+" "+i[2]+" "+i[3]
                        if(i[8] == None):
                            VERDICT = "DATA UNAVAILABLE"
                        else:
                            VERDICT = i[8]

                        counter += 1
                        print("(",counter,")",sep="",end = "  ")
                        print("ID NUMBER:      ",i[0])
                        print("     FULL NAME:      ",NAME)
                        print("     AGE      :      ",i[4])
                        print("     CRIME    :      ",i[5])
                        print("     GENDER   :      ",i[6])
                        print("     DATE     :      ",i[7])
                        print("     VERDICT  :      ",VERDICT)
                        print("")
                        print("")

                    if (counter == 0):
                        print("NO DATA WITH THE GIVEN AGE WAS FOUND.")
                        print("")
                        print("")
            
            elif(q == "2"):
                try:
                    A1 = int(input("ENTER LOWER LIMIT {FROM} OF AGE TO BE SEARCHED [1-100]:  "))
                    CHECK_AGE(A1)
                    A2 = int(input("ENTER UPPER LIMIT {TO} OF AGE TO BE SEARCHED [1-100]:    "))
                    CHECK_AGE(A2)
                    CHECK_RANGE(A1,A2)
                except INVALID_RANGE:
                    print("")
                    print("INVALID RANGE. PLEASE ENTER VALID RANGE.")
                    print("")
                    print("")    
                except AGE_ERROR:
                    print("")
                    print("ENTERED AGE IS INVALID. PLEASE ENTER AGE WITHIN THE SPECIFIED RANGE.")
                    print("")
                    print("")
                except ValueError:
                    print("")
                    print("PLEASE ENTER POSITIVE INTEGERS ONLY.")
                    print("")
                    print("")
                except:
                    print("")
                    print("SOME ERROR OCCURED. PLEASE TRY AGAIN.")
                    print("")
                    print("")
                else:
                    COMM = "SELECT * FROM crime_management "
                    C.execute(COMM)
                    counter = 0
                    print("")
                    for i in C:
                        if (i[4] >= A1) and (i[4] <= A2): 
                            if(i[2] == None):
                                NAME = i[1]+" "+i[3]
                            else:
                                NAME = i[1]+" "+i[2]+" "+i[3]
                            if(i[8] == None):
                                VERDICT = "DATA UNAVAILABLE"
                            else:
                                VERDICT = i[8]
                            
                            counter += 1
                            print("(",counter,")",sep="",end = "  ")
                            print("ID NUMBER:      ",i[0])
                            print("     FULL NAME:      ",NAME)
                            print("     AGE      :      ",i[4])
                            print("     CRIME    :      ",i[5])
                            print("     GENDER   :      ",i[6])
                            print("     DATE     :      ",i[7])
                            print("     VERDICT  :      ",VERDICT)
                            print("")
                            print("")

                    if (counter == 0):
                        print("NO DATA WITHIN THE GIVEN RANGE OF AGE WAS FOUND.")
                        print("")
                        print("")

            else:
                print("INVALID INPUT. PLEASE TRY AGAIN.")
                print("")
                print("")


        elif(Q == "4"):
            try:
                Crime = input("ENTER CRIME TO INITIATE SEARCH [MAX 15 CHAR]: ")
                print("")
                CHECK_CRIME(Crime)
                
            except DATA_TOO_LONG_ERROR:
                print("ENTERED DATA IS TOO LONG. PLEASE ENTER DATA ACCORDING TO SPECIFIED LENGTH.")
                print("")
                print("")
            except NULL_ERROR:
                print("NULL VALUES NOT ACCEPTED. PLEASE ENTER VALID DATA.")
                print("")
                print("")
            except:
                print("SOME ERROR OCCURED. PLEASE TRY AGAIN")
                print("")
                print("")
            else:
                COMM = "SELECT * FROM crime_management WHERE CRIME = (%s)"
                T = (Crime,)
                C.execute(COMM,T)
                counter = 0
                for i in C:
                    if(i[2] == None):
                        NAME = i[1]+" "+i[3]
                    else:
                        NAME = i[1]+" "+i[2]+" "+i[3]
                    if(i[8] == None):
                        VERDICT = "DATA UNAVAILABLE"
                    else:
                        VERDICT = i[8]

                    counter += 1
                    print("(",counter,")",sep="",end = "  ")
                    print("ID NUMBER:      ",i[0])
                    print("     FULL NAME:      ",NAME)
                    print("     AGE      :      ",i[4])
                    print("     CRIME    :      ",i[5])
                    print("     GENDER   :      ",i[6])
                    print("     DATE     :      ",i[7])
                    print("     VERDICT  :      ",VERDICT)
                    print("")
                    print("")

                if (counter == 0):
                    print("NO DATA WITH THE GIVEN CRIMES WAS FOUND.")
                    print("")
                    print("")

        elif(Q == "5"):
            try:
                Gender = input("ENTER GENDER TO INITIATE SEARCH [M/F]: ").upper()
                print("")
                CHECK_GENDER(Gender)
            except INVALID_INPUT:
                print("INVALID INPUT. PLEASE ENTER VALID DATA .")
                print("")
                print("")
            except:
                print("SOME ERROR OCCURED. PLEASE TRY AGAIN")
                print("")
                print("")
            else:
                COMM = "SELECT * FROM crime_management WHERE GENDER = (%s)"
                T = (Gender,)
                C.execute(COMM,T)
                counter = 0
                for i in C:
                    if(i[2] == None):
                        NAME = i[1]+" "+i[3]
                    else:
                        NAME = i[1]+" "+i[2]+" "+i[3]
                    if(i[8] == None):
                        VERDICT = "DATA UNAVAILABLE"
                    else:
                        VERDICT = i[8]

                    counter += 1
                    print("(",counter,")",sep="",end = "  ")
                    print("ID NUMBER:      ",i[0])
                    print("     FULL NAME:      ",NAME)
                    print("     AGE      :      ",i[4])
                    print("     CRIME    :      ",i[5])
                    print("     GENDER   :      ",i[6])
                    print("     DATE     :      ",i[7])
                    print("     VERDICT  :      ",VERDICT)
                    print("")
                    print("")

                if (counter == 0):
                    print("NO DATA WITH THE GIVEN GENDER WAS FOUND.")
                    print("")
                    print("")

        elif(Q=="6"):
            q = input('''SEARCH:
 1) SPECIFIC DATE
 2) WITHIN A RANGE
[PLEASE SELECT OPTION NUMBERS ONLY]
''')
            print("")
            if(q == "1"):
                try:
                    Date = input("ENTER DATE TO INITIATE SEARCH [YYYY-MM-DD]: ")
                    print("")
                    CHECK_DATE(Date)
                except INVALID_INPUT:
                    print("INVALID INPUT. PLEASE ENTER VALID DATA .")
                    print("")
                    print("")
                except INVALID_FORMAT:
                    print("INVALID FORMAT. PLEASE ENTER DATA ACCORDING TO THE SPECIFIED FORMAT.")
                    print("")
                    print("")
                except:
                    print("SOME ERROR OCCURED. PLEASE TRY AGAIN")
                    print("")
                    print("")
                else:
                    COMM = "SELECT * FROM crime_management WHERE DATE = (%s)"
                    T = (Date,)
                    C.execute(COMM,T)
                    counter = 0
                    for i in C:
                        if(i[2] == None):
                            NAME = i[1]+" "+i[3]
                        else:
                            NAME = i[1]+" "+i[2]+" "+i[3]
                        if(i[8] == None):
                            VERDICT = "DATA UNAVAILABLE"
                        else:
                            VERDICT = i[8]

                        counter += 1
                        print("(",counter,")",sep="",end = "  ")
                        print("ID NUMBER:      ",i[0])
                        print("     FULL NAME:      ",NAME)
                        print("     AGE      :      ",i[4])
                        print("     CRIME    :      ",i[5])
                        print("     GENDER   :      ",i[6])
                        print("     DATE     :      ",i[7])
                        print("     VERDICT  :      ",VERDICT)
                        print("")
                        print("")

                    if (counter == 0):
                        print("NO DATA WITH THE GIVEN DATE WAS FOUND.")
                        print("")
                        print("")

            elif(q == "2"):
                try:
                    D1 = input("ENTER LOWER LIMIT {FROM} OF DATE [YYYY-MM-DD]:  ")
                    CHECK_DATE(D1)
                    D2 = input("ENTER UPPER LIMIT {TO} OF DATE [YYYY-MM-DD]:    ")
                    CHECK_DATE(D2)
                    CHECK_RANGE(D1,D2)
                    print("")
                except INVALID_RANGE:
                    print("")
                    print("INVALID RANGE. PLEASE ENTER VALID RANGE.")
                    print("")
                    print("")
                except INVALID_INPUT:
                    print("")
                    print("INVALID INPUT. PLEASE ENTER VALID DATA.")
                    print("")
                    print("")
                except INVALID_FORMAT:
                    print("")
                    print("INVALID FORMAT. PLEASE ENTER DATA ACCORDING TO THE SPECIFIED FORMAT.")
                    print("")
                    print("")
                except:
                    print("")
                    print("SOME ERROR OCCURED. PLEASE TRY AGAIN")
                    print("")
                    print("")
                else:
                    COMM = "SELECT * FROM crime_management"
                    C.execute(COMM)
                    counter = 0
                    for i in C:
                        DATE = str(i[7])
                        if(DATE >= D1)and(DATE <= D2):
                            if(i[2] == None):
                                NAME = i[1]+" "+i[3]
                            else:
                                NAME = i[1]+" "+i[2]+" "+i[3]
                            if(i[8] == None):
                                VERDICT = "DATA UNAVAILABLE"
                            else:
                                VERDICT = i[8]

                            counter += 1
                            print("(",counter,")",sep="",end = "  ")
                            print("ID NUMBER:      ",i[0])
                            print("     FULL NAME:      ",NAME)
                            print("     AGE      :      ",i[4])
                            print("     CRIME    :      ",i[5])
                            print("     GENDER   :      ",i[6])
                            print("     DATE     :      ",i[7])
                            print("     VERDICT  :      ",VERDICT)
                            print("")
                            print("")

                    if (counter == 0):
                        print("NO DATA WITHIN THE GIVEN RANGE WAS FOUND.")
                        print("")
                        print("")

            else:
                print("INVALID INPUT. PLEASE TRY AGAIN.")
                print("")
                print("")

        elif(Q == "7"):
            try:
                VER = input('''ENTER VERDICT TO INITIATE SEARCH[MAX 50 CHAR]
{PRESS 'ENTER' IF DATA OF PEOPLE WITH NO VERDICT IS TO BE SEARCHED}: ''').upper()
                print("")
                if (VER == ""):
                    COMM = "SELECT * FROM crime_management WHERE VERDICT IS NULL"
                    C.execute(COMM)
                else:
                    CHECK_VERDICT(VER)
                    COMM = "SELECT * FROM crime_management WHERE VERDICT = (%s)"
                    T = (VER,)
                    C.execute(COMM,T)
            except DATA_TOO_LONG_ERROR:
                    print("ENTERED DATA IS TOO LONG. PLEASE ENTER DATA ACCORDING TO SPECIFIED LENGTH.")
                    print("")
                    print("")
            except:
                print("SOME ERROR OCCURED. PLEASE TRY AGAIN")
                print("")
                print("")
            else:
                counter = 0
                for i in C:
                    if(i[2] == None):
                        NAME = i[1]+" "+i[3]
                    else:
                        NAME = i[1]+" "+i[2]+" "+i[3]
                    if(i[8] == None):
                        VERDICT = "DATA UNAVAILABLE"
                    else:
                        VERDICT = i[8]

                    counter += 1
                    print("(",counter,")",sep="",end = "  ")
                    print("ID NUMBER:      ",i[0])
                    print("     FULL NAME:      ",NAME)
                    print("     AGE      :      ",i[4])
                    print("     CRIME    :      ",i[5])
                    print("     GENDER   :      ",i[6])
                    print("     DATE     :      ",i[7])
                    print("     VERDICT  :      ",VERDICT)
                    print("")
                    print("")

                if (counter == 0):
                    print("NO DATA WITH THE GIVEN VERDICT FOUND.")
                    print("")
                    print("")

        else:
            print("INVALID INPUT. PLEASE TRY AGAIN")
  # SEARCH_DATA IS READY. CHECK THIS USER DEFINEFUNCTION AGAIN.

#==============================================================================


# ========== UPDATE DATA ======================================================

def UPDATE_DATA():
    try:    
        ID = int(input("ENTER THE ID NUMBER OF THE RECORD TO BE UPDATED:  "))
        print("")
    except ValueError:
        print("PLEASE ENTER POSITIVE INTEGERS ONLY.")
        print("")
        print("")
    except:
        print("SOME ERROR OCCURED. PLEASE TRY AGAIN")
        print("")
        print("")
    else:
        C.execute("SELECT * FROM crime_management WHERE ID = (%s) ",(ID,))
        counter = 0
        for i in C:
            counter += 1
            
        if (counter == 0):
            print("NO RECORD WITH THE GIVEN ID FOUND. PLEASE TRY AGAIN.")
            print("")
            print("")
        else:
            print("THE FOLLOWING DATA WILL BE UPDATED:")
            print("")
            COMM = ("SELECT* FROM crime_management WHERE ID = (%s)")
            T = (ID,)
            C.execute(COMM,T)
            counter = 0
            for i in C:
                        
                if(i[2] == None):
                    NAME = i[1]+" "+i[3]
                else:
                    NAME = i[1]+" "+i[2]+" "+i[3]
                if(i[8] == None):
                    VERDICT = "DATA UNAVAILABLE"
                else:
                    VERDICT = i[8]
                counter += 1
                print("(",counter,")",sep="",end = "  ")
                print("ID NUMBER:      ",i[0])
                print("     FULL NAME:      ",NAME)
                print("     AGE      :      ",i[4])
                print("     CRIME    :      ",i[5])
                print("     GENDER   :      ",i[6])
                print("     DATE     :      ",i[7])
                print("     VERDICT  :      ",VERDICT)
                print("")

            Q = input("""SELECT THE DATA TO BE UPDATED:
     1. ID NUMBER
     2. NAME
     3. AGE
     4. CRIME
     5. GENDER
     6. DATE
     7. VERDICT
    [PLEASE ENTER OPTION NUMBERS ONLY]
    """)
            print("")
             
            if(Q == "1"):
                try:
                    new_ID = int(input("ENTER NEW ID: "))
                    print("")
                    CHECK_ID(new_ID)
                except ValueError:
                    print("PLEASE ENTER POSITIVE INTEGERS ONLY.")
                    print("")
                    print("")
                except DATA_TOO_SHORT_ERROR:
                    print("ENTERED DATA IS TOO SHORT. PLEASE ENTER DATA ACCORDING TO SPECIFIED LENGTH.")
                    print("")
                    print("")
                except DATA_TOO_LONG_ERROR:
                    print("ENTERED DATA IS TOO LONG. PLEASE ENTER DATA ACCORDING TO SPECIFIED LENGTH.")
                    print("")
                    print("")
                except:
                    print("SOME ERROR OCCURED. PLEASE TRY AGAIN")
                    print("")
                    print("")
                    
                else:
                    q = input("ARE YOU SURE YOU WOULD LIKE TO PROCEED WITH THE UPDATE?[Y/N] ").upper()
                    print("")
                    if (q == "Y"):
                        COMM = "UPDATE crime_management SET ID = (%s) WHERE ID = (%s)"
                        T = (new_ID,ID)
                        C.execute(COMM,T)
                        print("UPDATED DATA IS DISPLAYED BELOW: ")
                        print("")
                        C.execute("SELECT * FROM crime_management WHERE ID = (%s)",(new_ID,))
                        counter = 0
                        for i in C:
                        
                            if(i[2] == None):
                                NAME = i[1]+" "+i[3]
                            else:
                                NAME = i[1]+" "+i[2]+" "+i[3]
                            if(i[8] == None):
                                VERDICT = "DATA UNAVAILABLE"
                            else:
                                VERDICT = i[8]
                            counter += 1
                            print("(",counter,")",sep="",end = "  ")
                            print("ID NUMBER:      ",i[0])
                            print("     FULL NAME:      ",NAME)
                            print("     AGE      :      ",i[4])
                            print("     CRIME    :      ",i[5])
                            print("     GENDER   :      ",i[6])
                            print("     DATE     :      ",i[7])
                            print("     VERDICT  :      ",VERDICT)
                            print("")
                            print("DATA UPDATED.")
                            print("")
                            print("")
                        D.commit()

                    elif(q == "N"):
                        print("UPDATE CANCELLED.")
                        print("")
                        print("")
                    else:
                        print("INVALID INPUT.")
                        print("")
                        print("")


            elif (Q == "2"):
                SELECT = input('''WHICH OF THE FOLLOWING WOULD YOU LIKE TO UPDATE:
     1) FIRST NAME
     2) MIDDLE NAME
     3) LAST NAME
     4) FULL NAME
    [PLEASE SELECT OPTION NUMBERS ONLY]
    ''')
                print("")
                if(SELECT == "1"):
                    try:
                        new_FIRST_NAME = input("ENTER NEW FIRST NAME[10 CHARACTERS] : ").upper()
                        print("")
                        if (new_FIRST_NAME == ""):
                            raise NULL_ERROR()
                        else:
                            CHECK_NAME(new_FIRST_NAME)
                    except NULL_ERROR:
                        print("NULL VALUES NOT ACCEPTED. PLEASE ENTER VALID DATA.")
                        print("")
                        print("")    
            
                    except DATA_TOO_LONG_ERROR:
                        print("ENTERED DATA IS TOO LONG. PLEASE ENTER DATA ACCORDING TO SPECIFIED LENGTH.")
                        print("")
                        print("")
                    except:
                        print("SOME ERROR OCCURED. PLEASE TRY AGAIN")
                        print("")
                        print("")
                        
                    else:
                        q = input("ARE YOU SURE YOU WOULD LIKE TO PROCEED WITH THE UPDATE?[Y/N] ").upper()
                        print("")
                        
                        if (q == "Y"):
                            COMM = "UPDATE crime_management SET FIRST_NAME = (%s) WHERE ID = (%s)"
                            T = (new_FIRST_NAME,ID)
                            C.execute(COMM,T)
                            print("UPDATED DATA IS DISPLAYED BELOW: ")
                            print("")
                            C.execute("SELECT * FROM crime_management WHERE ID = (%s)",(ID,))
                            counter = 0
                            for i in C:
                            
                                if(i[2] == None):
                                    NAME = i[1]+" "+i[3]
                                else:
                                    NAME = i[1]+" "+i[2]+" "+i[3]
                                if(i[8] == None):
                                    VERDICT = "DATA UNAVAILABLE"
                                else:
                                    VERDICT = i[8]
                                counter += 1
                                print("(",counter,")",sep="",end = "  ")
                                print("ID NUMBER:      ",i[0])
                                print("     FULL NAME:      ",NAME)
                                print("     AGE      :      ",i[4])
                                print("     CRIME    :      ",i[5])
                                print("     GENDER   :      ",i[6])
                                print("     DATE     :      ",i[7])
                                print("     VERDICT  :      ",VERDICT)
                                print("")
                                print("DATA UPDATED.")
                                print("")
                                print("")
                            D.commit()

                        elif(q == "N"):
                            print("UPDATE CANCELLED.")
                            print("")
                            print("")
                        else:
                            print("INVALID INPUT.")
                            print("")
                            print("")

                elif(SELECT == "2"):
                    try:
                        new_MIDDLE_NAME = input("ENTER NEW MIDDLE NAME[10 CHARACTERS]{PRESS 'ENTER' FOR NO MID NAME}: ").upper()
                        print("")
                        if (new_MIDDLE_NAME == ""):
                            new_MIDDLE_NAME = None
                        else:
                            CHECK_NAME(new_MIDDLE_NAME)  
            
                    except DATA_TOO_LONG_ERROR:
                        print("ENTERED DATA IS TOO LONG. PLEASE ENTER DATA ACCORDING TO SPECIFIED LENGTH.")
                        print("")
                        print("")
                    except:
                        print("SOME ERROR OCCURED. PLEASE TRY AGAIN")
                        print("")
                        print("")
                        
                    else:
                        q = input("ARE YOU SURE YOU WOULD LIKE TO PROCEED WITH THE UPDATE?[Y/N] ").upper()
                        print("")
                        if (q == "Y"):
                            COMM = "UPDATE crime_management SET MIDDLE_NAME = (%s) WHERE ID = (%s)"
                            T = (new_MIDDLE_NAME,ID)
                            C.execute(COMM,T)
                            print("UPDATED DATA IS DISPLAYED BELOW: ")
                            print("")
                            C.execute("SELECT * FROM crime_management WHERE ID = (%s)",(ID,))
                            counter = 0
                            for i in C:
                            
                                if(i[2] == None):
                                    NAME = i[1]+" "+i[3]
                                else:
                                    NAME = i[1]+" "+i[2]+" "+i[3]
                                if(i[8] == None):
                                    VERDICT = "DATA UNAVAILABLE"
                                else:
                                    VERDICT = i[8]
                                counter += 1
                                print("(",counter,")",sep="",end = "  ")
                                print("ID NUMBER:      ",i[0])
                                print("     FULL NAME:      ",NAME)
                                print("     AGE      :      ",i[4])
                                print("     CRIME    :      ",i[5])
                                print("     GENDER   :      ",i[6])
                                print("     DATE     :      ",i[7])
                                print("     VERDICT  :      ",VERDICT)
                                print("")
                                print("DATA UPDATED.")
                                print("")
                                print("")
                            D.commit()

                        elif(q == "N"):
                            print("UPDATE CANCELLED.")
                            print("")
                            print("")
                        else:
                            print("INVALID INPUT.")
                            print("")
                            print("")



                elif(SELECT == "3"):
                    try:
                        new_LAST_NAME = input("ENTER NEW LAST NAME[10 CHARACTERS] : ").upper()
                        print("")
                        if (new_LAST_NAME == ""):
                            raise NULL_ERROR()
                        else:
                            CHECK_NAME(new_LAST_NAME)
                    except NULL_ERROR:
                        print("NULL VALUES NOT ACCEPTED. PLEASE ENTER VALID DATA.")
                        print("")
                        print("")    
            
                    except DATA_TOO_LONG_ERROR:
                        print("ENTERED DATA IS TOO LONG. PLEASE ENTER DATA ACCORDING TO SPECIFIED LENGTH.")
                        print("")
                        print("")
                    except:
                        print("SOME ERROR OCCURED. PLEASE TRY AGAIN")
                        print("")
                        print("")
                        
                    else:
                        q = input("ARE YOU SURE YOU WOULD LIKE TO PROCEED WITH THE UPDATE?[Y/N] ").upper()
                        print("")
                        if (q == "Y"):
                            COMM = "UPDATE crime_management SET LAST_NAME = (%s) WHERE ID = (%s)"
                            T = (new_LAST_NAME,ID)
                            C.execute(COMM,T)
                            print("UPDATED DATA IS DISPLAYED BELOW: ")
                            print("")
                            C.execute("SELECT * FROM crime_management WHERE ID = (%s)",(ID,))
                            counter = 0
                            for i in C:
                            
                                if(i[2] == None):
                                    NAME = i[1]+" "+i[3]
                                else:
                                    NAME = i[1]+" "+i[2]+" "+i[3]
                                if(i[8] == None):
                                    VERDICT = "DATA UNAVAILABLE"
                                else:
                                    VERDICT = i[8]
                                counter += 1
                                print("(",counter,")",sep="",end = "  ")
                                print("ID NUMBER:      ",i[0])
                                print("     FULL NAME:      ",NAME)
                                print("     AGE      :      ",i[4])
                                print("     CRIME    :      ",i[5])
                                print("     GENDER   :      ",i[6])
                                print("     DATE     :      ",i[7])
                                print("     VERDICT  :      ",VERDICT)
                                print("")
                                print("DATA UPDATED.")
                                print("")
                                print("")
                            D.commit()

                        elif(q == "N"):
                            print("UPDATE CANCELLED.")
                            print("")
                            print("")
                        else:
                            print("INVALID INPUT.")
                            print("")
                            print("")

                elif(SELECT == "4"):
                    try:
                        new_FULL_NAME = input("ENTER NEW FULL NAME[10 CHARACTERS PER PART]: ").upper()
                        print("")
                        L = new_FULL_NAME.split(" ")
                        if (len(L) == 3):
                            new_FIRST_NAME = L[0]
                            CHECK_NAME(new_FIRST_NAME)
                            
                            new_MIDDLE_NAME = L[1]
                            CHECK_NAME(new_MIDDLE_NAME)

                            new_LAST_NAME = L[2]
                            CHECK_NAME(new_LAST_NAME)

                            CONT = 1

                        elif (len(L) == 2):
                            new_FIRST_NAME = L[0]
                            CHECK_NAME(new_FIRST_NAME)

                            new_MIDDLE_NAME = None
                            
                            new_LAST_NAME = L[1]
                            CHECK_NAME(new_LAST_NAME)
                            CONT = 1
                        
                        elif (len(L) < 2) :
                            print("MINIMUM FIRST AND LAST NAME REQUIRED. PLEASE TRY AGAIN.")
                            print("")
                            print("")
                            CONT = 0

                        elif (len(L) > 3) :
                            print("MAXIMUM FIRST,MIDDLE AND LAST NAME CAN BE ENTERED. PLEASE TRY AGAIN.")
                            print("")
                            print("")
                            CONT = 0

                            
                    except DATA_TOO_LONG_ERROR:
                        print("ENTERED DATA IS TOO LONG. PLEASE ENTER DATA ACCORDING TO SPECIFIED LENGTH.")
                        print("")
                        print("")
                    except:
                        print("SOME ERROR OCCURED. PLEASE TRY AGAIN")
                        print("")
                        print("")
                        
                    else:
                        if (CONT != 0): 
                            q = input("ARE YOU SURE YOU WOULD LIKE TO PROCEED WITH THE UPDATE?[Y/N] ").upper()
                            print("")
                            if (q == "Y"):
                                COMM = "UPDATE crime_management SET FIRST_NAME = (%s) WHERE ID = (%s)"
                                T = (new_FIRST_NAME,ID)
                                C.execute(COMM,T)
                                
                                COMM = "UPDATE crime_management SET MIDDLE_NAME = (%s) WHERE ID = (%s)"
                                T = (new_MIDDLE_NAME,ID)
                                C.execute(COMM,T)
                                
                                COMM = "UPDATE crime_management SET LAST_NAME = (%s) WHERE ID = (%s)"
                                T = (new_LAST_NAME,ID)
                                C.execute(COMM,T)
                                
                                print("UPDATED DATA IS DISPLAYED BELOW: ")
                                print("")
                                C.execute("SELECT * FROM crime_management WHERE ID = (%s)",(ID,))
                                counter = 0
                                for i in C:
                                
                                    if(i[2] == None):
                                        NAME = i[1]+" "+i[3]
                                    else:
                                        NAME = i[1]+" "+i[2]+" "+i[3]
                                    if(i[8] == None):
                                        VERDICT = "DATA UNAVAILABLE"
                                    else:
                                        VERDICT = i[8]
                                    counter += 1
                                    print("(",counter,")",sep="",end = "  ")
                                    print("ID NUMBER:      ",i[0])
                                    print("     FULL NAME:      ",NAME)
                                    print("     AGE      :      ",i[4])
                                    print("     CRIME    :      ",i[5])
                                    print("     GENDER   :      ",i[6])
                                    print("     DATE     :      ",i[7])
                                    print("     VERDICT  :      ",VERDICT)
                                    print("")
                                    print("DATA UPDATED.")
                                    print("")
                                    print("")
                                D.commit()

                            elif(q == "N"):
                                print("UPDATE CANCELLED.")
                                print("")
                                print("")
                            else:
                                print("INVALID INPUT.")
                                print("")
                                print("")
                        
                else:
                    print("INVALID INPUT. PLEASE TRY AGAIN.")
                    print("")
                    print("")

            elif(Q == "3"):
                try:
                    new_AGE = int(input("ENTER NEW AGE (0-100): "))
                    print("")
                    CHECK_AGE(new_AGE)
                except ValueError:
                    print("PLEASE ENTER POSITIVE INTEGERS ONLY.")
                    print("")
                    print("")
                except AGE_ERROR:
                    print("ENTERED AGE IS INVALID. PLEASE ENTER AGE WITHIN THE SPECIFIED RANGE.")
                    print("")
                    print("")
                except:
                    print("SOME ERROR OCCURED. PLEASE TRY AGAIN")
                    print("")
                    print("")
                    
                else:
                    q = input("ARE YOU SURE YOU WOULD LIKE TO PROCEED WITH THE UPDATE?[Y/N] ").upper()
                    print("")
                    if (q == "Y"):
                        COMM = "UPDATE crime_management SET AGE = (%s) WHERE ID = (%s)"
                        T = (new_AGE,ID)
                        C.execute(COMM,T)
                        print("UPDATED DATA IS DISPLAYED BELOW: ")
                        C.execute("SELECT * FROM crime_management WHERE ID = (%s)",(ID,))
                        counter = 0
                        for i in C:
                        
                            if(i[2] == None):
                                NAME = i[1]+" "+i[3]
                            else:
                                NAME = i[1]+" "+i[2]+" "+i[3]
                            if(i[8] == None):
                                VERDICT = "DATA UNAVAILABLE"
                            else:
                                VERDICT = i[8]
                            counter += 1
                            print("(",counter,")",sep="",end = "  ")
                            print("ID NUMBER:      ",i[0])
                            print("     FULL NAME:      ",NAME)
                            print("     AGE      :      ",i[4])
                            print("     CRIME    :      ",i[5])
                            print("     GENDER   :      ",i[6])
                            print("     DATE     :      ",i[7])
                            print("     VERDICT  :      ",VERDICT)
                            print("")
                            print("DATA UPDATED.")
                            print("")
                            print("")
                        D.commit()

                    elif(q == "N"):
                        print("UPDATE CANCELLED.")
                        print("")
                        print("")
                    else:
                        print("INVALID INPUT.")
                        print("")
                        print("")


            elif(Q == "4"):
                try:
                    new_CRIME = input("ENTER NEW CRIME [15 CHARACTES]: ").upper()
                    print("")
                    CHECK_CRIME(new_CRIME)
                except DATA_TOO_LONG_ERROR:
                    print("ENTERED DATA IS TOO LONG. PLEASE ENTER DATA ACCORDING TO SPECIFIED LENGTH.")
                    print("")
                    print("")
                except NULL_ERROR:
                    print("NULL VALUES NOT ACCEPTED. PLEASE ENTER VALID DATA.")
                    print("")
                    print("")
                except:
                    print("SOME ERROR OCCURED. PLEASE TRY AGAIN")
                    print("")
                    print("")
                    
                else:
                    q = input("ARE YOU SURE YOU WOULD LIKE TO PROCEED WITH THE UPDATE?[Y/N] ").upper()
                    print("")
                    if (q == "Y"):
                        COMM = "UPDATE crime_management SET CRIME = (%s) WHERE ID = (%s)"
                        T = (new_CRIME,ID)
                        C.execute(COMM,T)
                        print("UPDATED DATA IS DISPLAYED BELOW: ")
                        C.execute("SELECT * FROM crime_management WHERE ID = (%s)",(ID,))
                        counter = 0
                        for i in C:
                        
                            if(i[2] == None):
                                NAME = i[1]+" "+i[3]
                            else:
                                NAME = i[1]+" "+i[2]+" "+i[3]
                            if(i[8] == None):
                                VERDICT = "DATA UNAVAILABLE"
                            else:
                                VERDICT = i[8]
                            counter += 1
                            print("(",counter,")",sep="",end = "  ")
                            print("ID NUMBER:      ",i[0])
                            print("     FULL NAME:      ",NAME)
                            print("     AGE      :      ",i[4])
                            print("     CRIME    :      ",i[5])
                            print("     GENDER   :      ",i[6])
                            print("     DATE     :      ",i[7])
                            print("     VERDICT  :      ",VERDICT)
                            print("")
                            print("DATA UPDATED.")
                            print("")
                            print("")
                        D.commit()

                    elif(q == "N"):
                        print("UPDATE CANCELLED.")
                        print("")
                        print("")
                    else:
                        print("INVALID INPUT.")
                        print("")
                        print("")



            elif(Q == "5"):
                try:
                    new_GENDER = input("ENTER NEW GENDER [M/F]: ").upper()
                    print("")
                    CHECK_GENDER(new_GENDER)
                except INVALID_INPUT:
                    print("INVALID INPUT. PLEASE ENTER VALID DATA .")
                    print("")
                    print("")
                except:
                    print("SOME ERROR OCCURED. PLEASE TRY AGAIN")
                    print("")
                    print("")
                    
                else:
                    q = input("ARE YOU SURE YOU WOULD LIKE TO PROCEED WITH THE UPDATE?[Y/N] ").upper()
                    print("")
                    if (q == "Y"):
                        COMM = "UPDATE crime_management SET GENDER = (%s) WHERE ID = (%s)"
                        T = (new_GENDER,ID)
                        C.execute(COMM,T)
                        print("UPDATED DATA IS DISPLAYED BELOW: ")
                        C.execute("SELECT * FROM crime_management WHERE ID = (%s)",(ID,))
                        counter = 0
                        for i in C:
                        
                            if(i[2] == None):
                                NAME = i[1]+" "+i[3]
                            else:
                                NAME = i[1]+" "+i[2]+" "+i[3]
                            if(i[8] == None):
                                VERDICT = "DATA UNAVAILABLE"
                            else:
                                VERDICT = i[8]
                            counter += 1
                            print("(",counter,")",sep="",end = "  ")
                            print("ID NUMBER:      ",i[0])
                            print("     FULL NAME:      ",NAME)
                            print("     AGE      :      ",i[4])
                            print("     CRIME    :      ",i[5])
                            print("     GENDER   :      ",i[6])
                            print("     DATE     :      ",i[7])
                            print("     VERDICT  :      ",VERDICT)
                            print("")
                            print("DATA UPDATED.")
                            print("")
                            print("")
                        D.commit()

                    elif(q == "N"):
                        print("UPDATE CANCELLED.")
                        print("")
                        print("")
                    else:
                        print("INVALID INPUT.")
                        print("")
                        print("")



            elif(Q == "6"):
                try:
                    new_DATE = input("ENTER NEW DATE [YYYY-MM-DD]: ")
                    print("")
                    CHECK_DATE(new_DATE)
                except INVALID_INPUT:
                    print("INVALID INPUT. PLEASE ENTER VALID DATA .")
                    print("")
                    print("")
                except INVALID_FORMAT:
                    print("INVALID FORMAT. PLEASE ENTER DATA ACCORDING TO THE SPECIFIED FORMAT.")
                    print("")
                    print("")
                except:
                    print("SOME ERROR OCCURED. PLEASE TRY AGAIN")
                    print("")
                    print("")
                    
                else:
                    q = input("ARE YOU SURE YOU WOULD LIKE TO PROCEED WITH THE UPDATE?[Y/N] ").upper()
                    print("")
                    if (q == "Y"):
                        COMM = "UPDATE crime_management SET DATE = (%s) WHERE ID = (%s)"
                        T = (new_DATE,ID)
                        C.execute(COMM,T)
                        print("UPDATED DATA IS DISPLAYED BELOW: ")
                        C.execute("SELECT * FROM crime_management WHERE ID = (%s)",(ID,))
                        counter = 0
                        for i in C:
                        
                            if(i[2] == None):
                                NAME = i[1]+" "+i[3]
                            else:
                                NAME = i[1]+" "+i[2]+" "+i[3]
                            if(i[8] == None):
                                VERDICT = "DATA UNAVAILABLE"
                            else:
                                VERDICT = i[8]
                            counter += 1
                            print("(",counter,")",sep="",end = "  ")
                            print("ID NUMBER:      ",i[0])
                            print("     FULL NAME:      ",NAME)
                            print("     AGE      :      ",i[4])
                            print("     CRIME    :      ",i[5])
                            print("     GENDER   :      ",i[6])
                            print("     DATE     :      ",i[7])
                            print("     VERDICT  :      ",VERDICT)
                            print("")
                            print("DATA UPDATED.")
                            print("")
                            print("")
                        D.commit()

                    elif(q == "N"):
                        print("UPDATE CANCELLED.")
                        print("")
                        print("")
                    else:
                        print("INVALID INPUT.")
                        print("")
                        print("")

            elif(Q == "7"):
                try:
                    new_VERDICT = input("ENTER NEW VERDICT[50 CHARACTERS]{PRESS 'ENTER' FOR NO VERDICT}: ").upper()
                    print("")
                    if (new_VERDICT == ""):
                        new_VERDICT = None
                    else:
                        CHECK_VERDICT(new_VERDICT)  
            
                except DATA_TOO_LONG_ERROR:
                    print("ENTERED DATA IS TOO LONG. PLEASE ENTER DATA ACCORDING TO SPECIFIED LENGTH.")
                    print("")
                    print("")
                except:
                    print("SOME ERROR OCCURED. PLEASE TRY AGAIN")
                    print("")
                    print("")
                        
                else:
                    q = input("ARE YOU SURE YOU WOULD LIKE TO PROCEED WITH THE UPDATE?[Y/N] ").upper()
                    print("")
                    if (q == "Y"):
                        COMM = "UPDATE crime_management SET VERDICT = (%s) WHERE ID = (%s)"
                        T = (new_VERDICT,ID)
                        C.execute(COMM,T)
                        print("UPDATED DATA IS DISPLAYED BELOW: ")
                        print("")
                        C.execute("SELECT * FROM crime_management WHERE ID = (%s)",(ID,))
                        counter = 0
                        for i in C:
                        
                            if(i[2] == None):
                                NAME = i[1]+" "+i[3]
                            else:
                                NAME = i[1]+" "+i[2]+" "+i[3]
                            if(i[8] == None):
                                VERDICT = "DATA UNAVAILABLE"
                            else:
                                VERDICT = i[8]
                            counter += 1
                            print("(",counter,")",sep="",end = "  ")
                            print("ID NUMBER:      ",i[0])
                            print("     FULL NAME:      ",NAME)
                            print("     AGE      :      ",i[4])
                            print("     CRIME    :      ",i[5])
                            print("     GENDER   :      ",i[6])
                            print("     DATE     :      ",i[7])
                            print("     VERDICT  :      ",VERDICT)
                            print("")
                            print("DATA UPDATED.")
                            print("")
                            print("")
                        D.commit()

                    elif(q == "N"):
                        print("UPDATE CANCELLED.")
                        print("")
                        print("")
                    else:
                        print("INVALID INPUT.")
                        print("")
                        print("")

            else:
                print("INVALID INPUT. PLEASE TRY AGAIN.")
                print("")
                print("")

        #___________
                        

#=== UPDATE_DATA IS READY.
# == RUN AS MANY TASTS AS POSSIBLE.


def DELETE_DATA():
    try:
        ID_TO_DELETE = int(input("ENTER THE ID NUMBER OF THE RECORD TO BE DELETED[6 DIGITS]: "))
        print("")
        CHECK_ID(ID_TO_DELETE)
    except ValueError:
        print("PLEASE ENTER POSITIVE INTEGERS ONLY.")
        print("")
        print("")
    except DATA_TOO_SHORT_ERROR:
        print("ENTERED DATA IS TOO SHORT. PLEASE ENTER DATA ACCORDING TO SPECIFIED LENGTH.")
        print("")
        print("")
    except DATA_TOO_LONG_ERROR:
        print("ENTERED DATA IS TOO LONG. PLEASE ENTER DATA ACCORDING TO SPECIFIED LENGTH.")
        print("")
        print("")
    
    else:
        C.execute("SELECT * FROM crime_management WHERE ID = (%s) ",(ID_TO_DELETE,))
        counter = 0
        for i in C:
            counter += 1
            
        if (counter == 0):
            print("NO RECORD WITH THE GIVEN ID FOUND. PLEASE TRY AGAIN.")
            print("")
            print("")
        else:
            print("THE FOLLOWING DATA WILL BE DELETED:")
            print("")
            COMM = ("SELECT* FROM crime_management WHERE ID = (%s)")
            T = (ID_TO_DELETE,)
            C.execute(COMM,T)
            counter = 0
            for i in C:
                        
                if(i[2] == None):
                    NAME = i[1]+" "+i[3]
                else:
                    NAME = i[1]+" "+i[2]+" "+i[3]
                if(i[8] == None):
                    VERDICT = "DATA UNAVAILABLE"
                else:
                    VERDICT = i[8]
                counter += 1
                print("(",counter,")",sep="",end = "  ")
                print("ID NUMBER:      ",i[0])
                print("     FULL NAME:      ",NAME)
                print("     AGE      :      ",i[4])
                print("     CRIME    :      ",i[5])
                print("     GENDER   :      ",i[6])
                print("     DATE     :      ",i[7])
                print("     VERDICT  :      ",VERDICT)
                print("")
        CONFIRM = input("ARE YOU SURE YOU WOULD LIKE TO 'PERMANENTLY' DELETE THE ABOVE RECORD?[Y/N]").upper()
        if(CONFIRM == "Y"):
            C.execute("DELETE FROM crime_management WHERE ID = (%s)",(ID_TO_DELETE,))
            print("RECORD DELETED PERMANENTLY.")
            print("")
            print("")
            D.commit()
        elif(CONFIRM == "N"):
            print("DELETION CANCELED.")
            print("")
            print("")
        else:
            print("INVALID INPUT.")
            print("")
            print("")



# ==================WORKING HERE

#COPY PASTE PROJECT_USER_ID_AND_PASSWORD OVER HERE AND DELETE THE BELOW PORTION

import stdiomask
ADMIN_DATA = {"ADMIN":"ADMIN123"}

def MENU_FOR_USER():
    EXIT = 1  #PUT EXIT = 1
    while (EXIT != 0):
        
        os.system('cls')
        time.sleep(0.2)
        try:
            print("")
            print("---------------------- CRIMINAL RECORDS MANAGEMENT SYSTEM ----------------------")
            print("")
            print("")
            Q1 = input('''WHICH OF THE FOLLOWING ACTIONS DO YOU WANT TO PERFORM:
 1) ENTER INFORMATION
 2) DISPLAY ALL INFORMATION
 3) SEARCH 
 4) UPDATE
 5) DELETE

 [PLEASE ENTER OPTION NUMBER]
 ''')
            print("")
            if(Q1 == "1"):
                DATA_ENTRY()
            elif(Q1 == "2"):
                DISPLAY_ALL()
            elif(Q1 == "3"):
                SEARCH_DATA()
            elif(Q1 == "4"):
                UPDATE_DATA()
            elif(Q1 == "5"):
                DELETE_DATA()
            else:
                print("INVALID INPUT. PLEASE TRY AGAIN.")
                print("")
                print("")
            
            
        except:
            print("SOME ERROR OCCURED!")
            print("")
            print("")


        Q2 = 1
        while(Q2 == 1):
            Q3 = input("Do you wish to continue? [Y/N] ").upper()
            print("")
            if(Q3 == "Y"):
                Q2 = 0
                EXIT = 1
                
            elif(Q3 == "N"):
                Q2 = 0
                EXIT = 0
            else:
                print("INVALID INPUT! Please try again.")
                print("")
                Q2 = 1
               
    else:
         print("")
         print("EXITING")
         time.sleep(0.75)
         os.system('cls')
         print("")
         print("")
         print(pyfiglet.figlet_format("           BYE !",font = '3-d'))          ########
         time.sleep(2.5)
         PROCEED = "YES"




def MENU_FOR_GUEST():
    EXIT = 1  #PUT EXIT = 1
    while (EXIT != 0):
        
        os.system('cls')
        time.sleep(0.2)
        try:
            print("")
            print("---------------------- CRIMINAL RECORDS MANAGEMENT SYSTEM ----------------------")
            print("")
            print("")
            Q1 = input('''WHICH OF THE FOLLOWING ACTIONS DO YOU WANT TO PERFORM:
 1) DISPLAY ALL INFORMATION
 2) SEARCH 
 
 [PLEASE ENTER OPTION NUMBER]
 ''')
            print("")
            if(Q1 == "1"):
                DISPLAY_ALL()
            elif(Q1 == "2"):
                SEARCH_DATA()
            else:
                print("INVALID INPUT. PLEASE TRY AGAIN.")
                print("")
                print("")
            
            
        except:
            print("SOME ERROR OCCURED!")
            print("")
            print("")


        Q2 = 1
        while(Q2 == 1):
            Q3 = input("Do you wish to continue? [Y/N] ").upper()
            print("")
            if(Q3 == "Y"):
                Q2 = 0
                EXIT = 1
                
            elif(Q3 == "N"):
                Q2 = 0
                EXIT = 0
            else:
                print("INVALID INPUT! Please try again.")
                print("")
                Q2 = 1
               
    else:
        print("")
        print("EXITING")
        time.sleep(0.75)
        os.system('cls')
        print("")
        print("")
        print(pyfiglet.figlet_format("           BYE !",font = '3-d'))            ########
        time.sleep(2.5)
    

#____MAIN MENU_________________
     
PROCEED = "NO"

while (PROCEED == "NO"):
    time.sleep(2)
    os.system('cls')
    time.sleep(0.2)
    print("")
    print("---------------------- CRIMINAL RECORDS MANAGEMENT SYSTEM ----------------------")
    print("")
    print("")
    ASK = input('''PLEASE SELECT AN OPTION :
 1) ENTER AS USER
 2) ENTER AS GUEST
 3) CREATE NEW USER/UPDATE PASSWORD FOR USER[ADMIN ONLY]
 4) EXIT
[PLEASE ENTER OPTION NUMBERS ONLY]
''')
    print("")
    if (ASK == "1"):
        try:
            F = open("USER_ID_AND_PASSWORD.txt","r")
            R = F.readlines()[0]
            DICT = eval(R)
            USER_ID = input("ENTER USER ID: ")
            count = 0
            for i in DICT.keys():
                if (USER_ID == i):
                    count+=1
            if(count == 0):
                print("INVALID USER ID. PLEASE TRY AGAIN")
                print("")
                print("")
            else:
                PASSWORD = stdiomask.getpass(prompt='PLEASE ENTER PASSWORD: ', mask='*')
                 
                if (DICT[USER_ID] == PASSWORD):
                    os.system('cls')
                    print("")
                    print("")
                    print("")
                    print(pyfiglet.figlet_format("     WELCOME !",font = 'slant'))                       #######
                    print("")
                    time.sleep(2)
                    MENU_FOR_USER()
                    PROCEED = "YES"
                else:
                    print("")
                    print("INCORRECT PASSWORD! PLEASE TRY AGAIN.")
                    print("")
            F.close()
        except FileNotFoundError:
            print("")
            print("SORRY! NO FILE AVAILABLE. NEW FILE HAS BEEN CREATED.")
            print("PLEASE REQUEST ADMIN TO ENTER USER ID AND PASSWORD.")
            print("THEN TRY AGAIN. THANK YOU.")
            print("")
            F = open("USER_ID_AND_PASSWORD.txt","x")
            F.close()
        except:
            print("SORRY! SOME ERROR OCCURED.")
            print("")
            

    elif(ASK == "2"):
        os.system('cls')
        print("")
        print("")
        print("")
        print(pyfiglet.figlet_format("     WELCOME !",font = 'slant'))             #######
        print("")
        time.sleep(2)
        MENU_FOR_GUEST()
        PROCEED = "YES"
        


    elif(ASK == "3"):
        try:
            ADMIN_ID = input("ENTER 'ADMIN ID': ")
            count = 0
            for i in ADMIN_DATA.keys():
                if (i == ADMIN_ID):
                    count += 1
            if (count != 0):
                print("")
                ADMIN_PASSWORD = stdiomask.getpass(prompt='PLEASE ENTER PASSWORD: ', mask='*')
                if(ADMIN_DATA[ADMIN_ID] == ADMIN_PASSWORD):
                    os.system('cls')
                    print("")
                    print(pyfiglet.figlet_format("            WELCOME"))                    ######
                    print(pyfiglet.figlet_format("            ADMIN !"))    
                    print("")
                    time.sleep(2)
                    F = open("USER_ID_AND_PASSWORD.txt","r")
                    R = F.readlines()[0]
                    DICT = eval(R)
                    DICT[ADMIN_ID] = ADMIN_PASSWORD
                    F.close()
                    NEW_USER_ID = input("ENTER USER ID TO BE ENTERED/UPDATED: ")
                    N = 0
                    for i in DICT.keys():
                        if (i == NEW_USER_ID):
                            N +=1
                    if(N != 0):
                        print("THIS USER ID ALREADY EXISTS.")
                        UPDT = input("DO YOU WISH TO UPDATE THIS USER ID[Y/N]: ").upper()
                        if(UPDT == "Y"):
                            NEW_PASSWORD = stdiomask.getpass(prompt="ENTER NEW PASSWORD FOR USER ID: ", mask='*')
                            DICT[NEW_USER_ID] = NEW_PASSWORD
                            F = open("USER_ID_AND_PASSWORD.txt","w")
                            F.write(str(DICT))
                            F.close()
                            print("")
                            print("PASSWORD FOR USER ID UPDATED")
                            print("")
                            print("")
                
                        elif(UPDT == "N"):
                            print("")
                            print("PASSWORD UPDATE CANCELED")
                            print("")
                            print("")
                        else:
                            print("")
                            print("INVALID INPUT. PLEASE TRY AGAIN")
                            print("")
                            print("")
                    else:
                        NEW_PASSWORD = stdiomask.getpass(prompt="ENTER NEW PASSWORD FOR USER ID: ", mask='*')
                        DICT[NEW_USER_ID] = NEW_PASSWORD
                        F = open("USER_ID_AND_PASSWORD.txt","w")
                        F.write(str(DICT))
                        F.close()
                        print("")
                        print("NEW USER ID ENTERED")
                        print("")
                        print("")
                else:
                    print("INVALID PASSWORD.")
                    print("")

            else:
                print("INVALID ADMIN ID.")
                print("")
        except FileNotFoundError:
            print("")
            print("SORRY! NO FILE AVAILABLE. NEW FILE HAS BEEN CREATED.")
            print("PLEASE REQUEST ADMIN TO ENTER USER ID AND PASSWORD.")
            print("THEN TRY AGAIN. THANK YOU.")
            print("")
            F = open("USER_ID_AND_PASSWORD.txt","x")
            F.close()            
        # except:
        #     print("")
        #     print("SOME ERROR OCCORED.")
        #     print("")
        #     print("")
            
                
    elif(ASK == "4"):
        print("")
        print("EXITING")
        time.sleep(0.75)
        os.system('cls')
        print("")
        print("")
        print(pyfiglet.figlet_format("           BYE !",font = '3-d'))                    ########
        time.sleep(2.5)
        PROCEED = "YES"

    else:
        print("")
        print("INVALID INPUT. PLEASE TRY AGAIN.")
        print("")
        print("")
