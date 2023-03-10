from tabulate import tabulate 
import mysql.connector
c = mysql.connector.connect(host = "localhost", user = "root", password =  "Eneeya.Senthil",   database = "pythondb") 

"""
if c:
    print(" connected ")
else:
    print(" error not connected") 
"""

def insert(id, name, age, city):
    res = c.cursor()
    ins = "insert into users (id, name, age, city)  values (%s, %s, %s, %s)"
    user = (id, name, age, city)
    res.execute(ins, user)
    c.commit()
    print(" Data inserted successfully ")


def update( name, age, city, id):
    res = c.cursor()
    upd = "update users set   name =%s, age = %s, city = %s where id = %s"
    user = (name, age, city, id)
    res.execute(upd, user)
    c.commit()
    print(" Updated successfully ")

def select():
    res = c.cursor()
    sel = "select id, name, age, city from users"
    res.execute(sel)
    result = res.fetchall()
    print(tabulate(result, headers = ["ID","NAME","AGE","CITY"]))


def delete(id):
    res = c.cursor()
    dele = "delete from users where id = %s"
    user = (id, )
    res.execute(dele, user)
    c.commit()
    print(" Data deleted successfully ")


while True:
    print("\t 1 insert data \n \t 2 update data \t \n 3 select data \n \t 4 delete \n \t 5 quit ")
    choice =int( input("  Enter the choice: "))
    if choice == 1:
        id = int(input(" Enter the id "))
        name = input(" Enter the name: ")
        age = int(input(" Enter the age "))
        city = input(" Enter the city ")
        insert(id, name, age, city)
    elif choice == 2:
        id = int(input(" Enter the id "))
        name = input(" Enter the name: ")
        age = int(input(" Enter the age "))
        city = input(" Enter the city ")
        update(name, age, city, id)
    elif choice == 3:
        select()
    elif choice == 4:
        id = int(input( " Enter the id "))
        delete(id)
    elif choice == 5:
        quit()
    else:
        print("invalid")





