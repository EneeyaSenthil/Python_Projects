pwd = input(" What is the master password? ")

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            print(line)

def add():
    name = input(" Account name: ")
    password = input(" Password: ")
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + password + "\n" )


while True:
    mode = input(" Would you like to add a new password or view the  existing ones? \n  add/view  or Press q to quit? ").lower()
    if mode == 'q':
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode")
        continue