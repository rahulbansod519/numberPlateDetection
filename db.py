import re
import sqlite3
import datetime
con= sqlite3.connect('db.db')
cur = con.cursor()
# cur.execute('''CREATE TABLE "dbs" ("num_plate" TEXT NOT NULL,"dateTime" TEXT NOT NULL)''')
def dbEntry(num_plate):
    if num_plate:
        cur.execute("INSERT INTO dbs VALUES(?,dateTime('now','localtime'))",(num_plate,))
        #print("ok")
    con.commit()
    #con.close()

#DATE
def convertDate(fdate,ldate,stime,etime):
    format='%d-%m-%Y'
    fdate=datetime.datetime.strptime(fdate,format)
    ldate=datetime.datetime.strptime(ldate,format)
    d1=fdate.date()
    d2=ldate.date()
    # for r in cur.execute('SELECT * FROM dbs WHERE date BETWEEN ? 00:00:00 AND ? 00:00:00',(d1,d2)):
    #     print(r)
    for r in cur.execute(f"SELECT * FROM dbs WHERE dateTime BETWEEN '{d1} {stime}:00:00' AND '{d2} {etime}:00:00'"):
        print(r)
    #print("ok2")
    
#TIME
def convertTime(stime,etime):
    # format = '%H:%M'
    # stime = datetime.datetime.strptime(stime,format)
    # etime = datetime.datetime.strptime(etime,format)
    # t1=stime.time()
    # t2=etime.time()
    # res=cur.execute('SELECT * FROM dbs WHERE time BETWEEN ? AND ?',(t1,t2))
    # for r in res:
    #     print(r)
    
    for i in cur.execute(f"SELECT * FROM dbs WHERE time BETWEEN '{stime}:00:00' AND '{etime}:00:00'"):
        print(i)
#NUMBER
def getNumberFromNumber(num):
    if num:
        for r in cur.execute('select * from dbs where num_plate=:num',{'num':num}):
            print(r)



#TIME


    

#getFromNumberPlate(num)
while True:
    ch=int(input("1.To Create new Record\n2.getNumberFromDate\n3.getNumberFromTime\n4.getNumberFromNumber\n"))
    if ch==1:
        num_plate=input("Enter Number Plate: ")
        if num_plate:
            dbEntry(num_plate)
    elif ch==2:
        fdate=input("Enter Starting Date 'DD-MM-YYYY' format:  ")
        ldate=input("Enter Ending Date 'DD-MM-YYYY' format: ")
        stime=input("Enter Starting Time")
        etime=input("Enter Ending Time")
        # if fdate and ldate:
        convertDate(fdate,ldate,stime,etime)
    elif ch==3:
        stime=input("Enter Starting Time")
        etime=input("Enter Ending Time")
        if stime and etime:
            convertTime(stime,etime)

    elif ch==4:
        num = input("enter number to get info: ")
        getNumberFromNumber(num)

