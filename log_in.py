#super admin username: SDM001 and password: SDMpassword
# Log in as super admin first to create an admin account
import getpass
 

def start_superadmin()
    SDM_username = 'SDM001'
    SDM_password = 'SDMpass001'
   
    superadmin_credentials = f"{SDM_username},{SDM_password}"
   
    with open('login.txt','a+') as file:
        pass
    # Check if super admin credentials already exist
    with open("login.txt", 'r+') as file:
        lines = file.readlines()
        for line in lines:
            if line.strip() == superadmin_credentials:
                return
   
   
       
 
    if superadmin_credentials not in lines:
        # Add super admin credentials if they do not exist
        with open("login.txt", 'a+') as file:
            file.write(f'{superadmin_credentials}\n')
 
   
   
 
def superadmin():
    print('add a new admin account:')
    username = input("username: ")
    password = input('password: ')
 
    with open("login.txt", 'a+') as file:
       
        file.write(f'{username},{password}\n')
 
def ADMmenu(): # Admin perms
    print ('''you are loged in as admin, enter your selection:
           1. Manage librarian staff
           2. Manage librarian member''')
 
    choice = int(input('enter your choice: '))
   
    try:
 
        if choice == 1:
            LBS()
        elif choice == 2:
            LBM()
       
     
           
    except:
        print('try again')
        ADMmenu()
 
def LBS():
    print('''Welcome to staff management system:
          1. Add new staff
          2. View librarian staff
          3. Search librarian staff
          4. Edit staff
          5. Remove staff''')
    LBSchoice = int(input('Enter your selection:'))
    if LBSchoice == 1:
        add_staff()
    elif LBSchoice == 2:
        view_staff()
    elif LBSchoice == 3:
        search_staff()
    elif LBSchoice == 4:
        edit_staff()
    elif LBSchoice == 5:
        remove_staff()

def LBM():
    print('''Welcome to member management system 
          1. Add new member
          2. View all member information
          3. Search member information
          4. Edit member 
          5. Delete member''')
    LBMchoice = int(input('Enter your selection : '))
    if LBMchoice == 1 :
        add_member()
    elif LBMchoice == 2 :
        view_member()
    elif LBMchoice == 3 :
        search_member()
    elif LBMchoice == 4 :
        edit_member()
    elif LBMchoice == 5 :
        delete_member()
    
    

           
 
def add_staff():
    print('add a new account:')
    username = input("username: ")
    password = input('password: ')
    birthday = input('enter birthday(DD/MM/YYYY): ')
    gender = input('enter gender(male/female): ')
    salary = input('salary: ')
    position = input('position: ')
   
    with open('add_staff_member.txt', 'a+') as file:
        file.write(f'{username},{password}\n')
    with open ('staff_info.txt','a+') as file:
        file.write(f'{username}, birthday: {birthday}, gender: {gender}, salary: {salary}, position: {position}\n')
   
 
 
def view_staff():
    with open('staff_info.txt','r') as file:
        for line in file:
            print(line)
 
def search_staff():
        Username = input('enter the ID you want to search:\n ')
        with open('staff_info.txt', 'r') as file:
         for line in file:
            SU, SB, SG, SS, SP = line.strip().split(', ')
            if SU == Username:
             
             print(f"username: {SU}, birthday: {SB}, gender: {SG}, salary: {SS}, position: {SP}")
             
def edit_staff():
    # Read all lines from the file
    with open('staff_info.txt', 'r') as file:
        lines = file.readlines()
   
    # Get the username to edit
    edit_username = input('Enter the ID you want to edit:\n ')
   
    # Open the file in write mode to update it
    with open('staff_info.txt', 'w') as file:
        for line in lines: 
            if line.startswith(edit_username):
                lines = line.strip()
                print(f"Current details: {lines}")
                new_username = input('Enter new username: ')
                birthday = input('Enter new birthday (DD/MM/YYYY): ')
                gender = input('Enter new gender (male/female): ')
                salary = input('Enter new salary: ')
                position = input('Enter new position: ')
                file.write(f'{new_username}, birthday: {birthday}, gender: {gender}, salary:{salary}, position: {position}\n')
            else:
                file.write(line)
 
def remove_staff():
    # read all line in file and save it in lines
    with open('staff_info.txt', 'r') as file:
        lines = file.readlines()
    with open('login.txt', 'r') as file2:
        file2line = file.readlines()
 
    remove_username = input('Enter the ID you want to remove:\n ')
   
    with open('staff_info.txt', 'w') as file:
       
        for line in lines:
            lines = line.strip()
            if not line.startswith(remove_username):
                file.write(line)
               
           
    with open('login','w') as file2:
        for line in file2line:
            file2line = line.strip()
            if not remove_username.startswith(remove_username):
                file2.write(line)
       

def add_member():
    print('add a new account')
    username = input('New username :')
    with open('add_member.txt','r') as file1:
        for line in file1:
            if line.startswith(username):
                print('username already exist.')
                LBS()
                break

    password = input('New password :')
    birthday = input('enter your birthday (DD/MM/YYY) : ')
    gender = input('enter your gender (male/female) : ')




    with open ('add_member.txt', 'a+') as file:
        file.write(f'{username},{password} \n')
    with open ('member_info.txt', 'a+') as file2:
        file2.write(f'{username}, birthday: {birthday}, gender: {gender}\n')


def view_member():
    with open ('member_info.txt', 'r') as file:
        for line in file:
            print(line)


def search_member():
    with open('member_info.txt','r') as file:
        Username = input('enter the ID you want to search:\n ')
        with open('member_info.txt', 'r') as file:
         for line in file:
            SU, SB, SG = line.strip().split(', ')
            if SU == Username:
             print(SU, SB, SG)



def edit_member():
     # Read all lines from the file
    with open('member_info.txt', 'r') as file:
        lines = file.readlines()
   
    # Get the username to edit
    edit_username = input('Enter the ID you want to edit:\n ')
   
    # Open the file in write mode to update it
    with open('member_info.txt', 'w') as file:
        for line in lines:
            if line.startswith(edit_username):
                lines = line.strip()
                print(f"Current details: {lines}")
                new_username = input('Enter new username: ')
                birthday = input('Enter new birthday (DD/MM/YYYY): ')
                gender = input('Enter new gender (male/female): ')
                file.write(f'{new_username}, birthday: {birthday}, gender: {gender}\n')
            else:
                file.write(line)


def delete_member():
    # read all line in file and save it in lines
    with open('member_info.txt', 'r') as file:
        lines = file.readlines()
    with open('login.txt', 'r') as file2:
        file2line = file.readlines()
 
    remove_username = input('Enter the ID you want to remove:\n ')
   
    with open('member_info.txt', 'w') as file:
       
        for line in lines:
            lines = line.strip()
            if not line.startswith(remove_username):
                file.write(line)
               
           
    with open('login','w') as file2:
        for line in file2line:
            file2line = line.strip()
            if not remove_username.startswith(remove_username):
                file2.write(line)
    

    
                






def login():
    print('Please enter your ID and password')
    username = input('username: ')
    password = getpass.getpass('password: ')
 
    try:
        with open('login.txt', 'r') as file:
            for line in file:
                stored_username, stored_password = line.strip().split(',')
 
                if stored_username == username and stored_password == password:
                    if line.startswith('SDM'):
                        print('You are logged in as super admin\n')
                        superadmin()
                        for i in range(20):
                            repeat = input('Would you like to add another admin?(Y/N): ')
                            repeat = repeat.upper()
                            if repeat == 'Y':
                                superadmin()
                            else:
                                break
                    elif line.startswith('ADM'):
                        ADMmenu()
                       
                       
                       
                        for i in range(20):
                            repeat = input('Return to admin menu?(Y/N): ')
                            repeat = repeat.upper()
                            if repeat == 'Y':
                                ADMmenu()
                            else:
                                break                                  
    except:
        print('Something went wrong, try running the program again')
        exit()                    

 
start_superadmin()
login()
 
