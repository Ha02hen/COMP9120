#!/usr/bin/env python3
import psycopg2

#####################################################
##  Database Connection
#####################################################

'''
Connect to the database using the connection string
'''
def openConnection():
    # connection parameters - ENTER YOUR LOGIN AND PASSWORD HERE
    userid = "y22s2c9120_zzho7420"
    passwd = "dD6cPV2p"
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
    conn = openConnection()
    curs = conn.cursor()
    curs.execute("Select * from Administrator")
    adms = curs.fetchall()
    for adm in adms:
        if login == adm[0] and password == adm[1]:
            return adm
    curs.close()
    conn.close()




'''
List all the associated instructions in the database by administrator
'''
def findInstructionsByAdm(login):

    return


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
