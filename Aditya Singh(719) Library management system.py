import mysql.connector as x
con=x.connect(host="localhost",user="root",password="1234",database="library")

def addb():
   bn=input("Enter book name:")
   c=input("Enter book code:")
   t=input("Total books:")
   s=input("Enter subject:")
   data=(bn,c,t,s)
   sql="insert into books values(%s,%s,%s,%s)"
   c=con.cursor()
   c.execute(sql,data)
   con.commit()
   print("Data Entered Successfully")
   main()
   
def issueb():
   n=input("Enter name:")
   r=input("Enter reg no. :")
   co=input("Enter book code:")
   d=input("Enter date:")
   data=(n,r,co,d)
   sql1="insert into issue values(%s,%s,%s,%s)"
   c=con.cursor()
   c.execute(sql1,data)
   con.commit()
   print("Book Issued to:",n)
   bookup(co,-1)

def submitb():
   n=input("Enter name:")
   r=input("Enter reg no.")
   co=input("Enter book code:")
   d=input("Enter date:")
   data=(n,r,co,d)
   sql2="insert into submit values(%s,%s,%s,%s)"
   c=con.cursor()
   c.execute(sql2,data)
   con.commit()
   print("Book submitted by:",n)
   bookup(co,+1)

def bookup(co,u):
   a="select TOTAL from books where BCODE=%s"
   data=(co,)
   c=con.cursor()
   c.execute(a,data)
   myresult=c.fetchone()
   t=myresult[0]+u
   sql="update books set TOTAL=%s where BCODE=%s"
   d=(t,co)
   c.execute(sql,d)
   con.commit()
   main()

def db():
   ac=input("Enter book code:")
   a="delete from books where BCODE=%s"
   data=(ac,)
   c=con.cursor()
   c.execute(a,data)
   con.commit()
   main()

def dispb():
   a="select*from books"
   c=con.cursor()
   c.execute(a)
   myresult=c.fetchall()
   for i in myresult:
      print("Book Name:",i[0])
      print("Book Code:",i[1])
      print("Total:",i[2])
   main()

def main():
  print("                         LIBRARY MANAGER                        ")
  print("1.ADD BOOK")
  print("2.ISSUE BOOK")
  print("3.SUBMIT BOOK")
  print("4.DELETE BOOK")
  print("5.DISPLAY BOOKS")
  choice=input("Enter Task no :")
  if(choice=="1"):
     addb()
  elif(choice=="2"):
     issueb()
  elif(choice=="3"):
     submitb()
  elif(choice=="4"):
      db()
  elif(choice=="5"):
      dispb()
  else:
     print("Incorrect choice")
     main()

def pswd():
   ps=input("Enter Password:")
   if ps=="Aditya@2005":
      main()
   else:
      print("Incorrect Password")
      pswd()
pswd()
      
   
