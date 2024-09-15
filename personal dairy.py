import datetime
a=input("ENTER PATH OF YOUR DAIRY IN YOUR PC-")
Dairy=open(a,"a+")
c=input("Enter r or R to read to your dairy")
if c=='R' or c=='r':
    Dairy.seek(0)
    r=Dairy.read()
    print(r)
date=str(datetime.datetime.now())
Dairy.write(date+"\n")
d=input("Enter w or W to read to your dairy")
if d=='W' or d=='w':
    a=input("Write in your dairy as you want.To go to next line type<backslash n>.Press enter to finish!\n")
    Dairy.write(a+"\n")
    Dairy.flush()
Dairy.close()
input("Press Enter to print nothing!")
            
