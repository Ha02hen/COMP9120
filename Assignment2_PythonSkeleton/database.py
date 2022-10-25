#!/usr/bin/env python3
from unittest import result
from itsdangerous import NoneAlgorithm
import psycopg2

#####################################################
##  Database Connection
######################################################

'''
Connect to the database using the connection string
'''
def openConnection():
    # connection parameters - ENTER YOUR LOGIN AND PASSWORD HERE
    userid = "y22s2c9120_unikey"
    passwd = ""
    myHost = "soit-db-pro-2.ucc.usyd.edu.au"

    # Create a connection to the database
    conn = None
    try:
        # Parses the config file and connects using the connect string
        conn = psycopg2.connect(database=userid,
                                    user=userid,
                                    password=passwd,
                                    host=myHost)
    except psycopg2.Error as sqle:
        print("psycopg2.Error : " + sqle.pgerror)
    
    # return the connection to use
    return conn

'''
Validate administrator based on login and password
'''
def checkAdmCredentials(login, password):

    return ['daegis', 'adm222', 'Derien', 'Aegis', 'derien.aegis@yahoomail.com', 95700.15]


'''
List all the associated instructions in the database by administrator
'''
def findInstructionsByAdm(login):

    conn = openConnection()
    curs = conn.cursor()
    curs.execute("""SELECT A.instructionid, 
                    A.amount, 
                    A.frequency, 
                    A.expirydate, 
                    concat(B.firstname, ' ', B.lastname) AS fullname, 
                    A.code,
                    A.notes,
                    CASE A.expirydate>=current_date WHEN TRUE THEN 1
                    ELSE 2 END AS ifexpiry
                    FROM investinstruction A
                    LEFT JOIN customer B
                    ON A.customer = B.login
                    LEFT JOIN ETF C
                    ON C.code = A.code
                    WHERE administrator = %s
                    ORDER BY ifexpiry, A.expirydate ASC, fullname DESC""", (login,))
    
    result = curs.fetchall()

    instruction_list = list()
    for instruction in result:
        instruction_list.append(
            {
                'instruction_id': instruction[0],
                'amount': instruction[1],
                'frequency': instruction[2],
                'expirydate': instruction[3],
                'customer': instruction[4],
                'etf': instruction[5],
                'notes': instruction[6]
            }
        )
    
    curs.close()
    conn.close()

    if result is None:
        return None
    else:
        return instruction_list


'''
Find a list of instructions based on the searchString provided as parameter
See assignment description for search specification
'''
def findInstructionsByCriteria(searchString):

    return


'''
Add a new instruction
'''
def addInstruction(amount, frequency, customer, administrator, etf, notes):

    return


'''
Update an existing instruction
'''
def updateInstruction(instructionid, amount, frequency, expirydate, customer, administrator, etf, notes):

    return
