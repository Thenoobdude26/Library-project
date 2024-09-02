#super admin username: SDM001 and password: SDMpassword

def start_superadmin():
    SDM_username = 'SDM001'
    SDM_password = 'SDMpassword'
    superadmin_credentials = f"{SDM_username},{SDM_password}\n"

    # Check if super admin credentials already exist
    with open("login.txt", 'r') as file:
        lines = file.readlines()
        

    if superadmin_credentials not in lines:
        # Add super admin credentials if they do not exist
        with open("login.txt", 'a+') as file:
            file.write(f"{SDM_username},{SDM_password}\n")

    
    

def superadmin():
    print('add a new account:')
    username = input("username: ")
    password = input('password: ')

    with open("login.txt", 'a+') as file:
        
        file.write(f'{username},{password}\n')
        

def login():
    print('Please enter your ID and password')
    username = input('username: ')
    password = input('password: ')

    try:
        with open('login.txt', 'r+') as file:
            for line in file:
                stored_username, stored_password = line.strip().split(',')

                if stored_username == username and stored_password == password:
                    if line.startswith('SDM'):
                        print('You are logged in as super admin\n')
                        superadmin()
                        break
                    elif line.startswith('ADM'):
                        print('You are logged in as admin')
                        pass
                    elif line.startswith('LBM'):
                        print('You are logged in as member')
                        pass
    except:
        print('incorrect password or username')
        exit()                    
                
         
                

start_superadmin()
login()
