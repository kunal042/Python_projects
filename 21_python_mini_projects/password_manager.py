manage_pwd = input("What is the master password? ")

def view():
    with open("passwords.txt" ,'r') as f:
        for line in f.readlines():
            data= line.rstrip()
            user, pswd = data.split("|")
            print(f"User : {user}  password : {pswd}")

def add():
    user = input("Enter your user name : ")
    pswd = input("password : ")

    with open("passwords.txt", 'a') as f:
        f.write(f" {user} |  {pswd} | \n")
    


while True:
    mode = input("Would you like to add a new password or view existing one (view/add)? and Type Q for quit>: ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("Invalid Mode")
        continue
