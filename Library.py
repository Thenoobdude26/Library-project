#super admin username: SDM001 and password: SDMpassword
# Log in as super admin first to create an admin account
import getpass
 

def start_superadmin():
    SDM_username = 'SDM001'
    SDM_password = 'SDMpass001'
   
    superadmin_credentials = f"{SDM_username},{SDM_password}"
   
    with open('Admin.txt', 'a+') as file:
        pass
    # Check if super admin credentials already exist
    with open("Admin.txt", 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.strip() == superadmin_credentials:
                return
   
   
       
 
    if superadmin_credentials != lines:
        # Add super admin credentials if they do not exist
        with open("Admin.txt", 'a+') as file:
            file.write(f'{superadmin_credentials}\n')
 
   
   
 
def superadmin():
    print('add a new admin account:')
    username = input("username: ")
    password = input('password: ')

    with open('Admin.txt', 'r') as file:
        for line in file:
            if line.startswith(username):
                print('account already exist, run the program again')
                return
                
 
    with open("Admin.txt", 'a+') as file:
       
        file.write(f'{username},{password}\n')
 
def ADMmenu(): # Admin perms
    print ('''
           1. Manage librarian staff
           2. Manage librarian member
           3. logout''')
 
    choice = int(input('enter your choice: '))
   
 
    if choice == 1:
            LBS()
    elif choice == 2:
            LBM()
    elif choice == 3:
            exit()
       
     
           

 
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
    elif LBMchoice > 5 or LBMchoice < 1:
        return
    
    

           
 
def add_staff():
    print('add a new account:')
    username = input("username: ")
    password = input('password: ')
    birthday = input('enter birthday(DD/MM/YYYY): ')
    gender = input('enter gender(male/female): ')
    salary = input('salary: ')
    position = input('position: ')

    with open('staff_list.txt', 'a+') as file:
        file.seek(0)
        for line in file:
            if line.startswith(username):
                print('account already exist.\n')
                return 
             
            
    with open('staff_list.txt', 'a+') as file:
        file.seek(0)
        file.write(f'{username},{password}\n')

    with open ('Staff_info.txt','a+') as file:
        file.seek(0)
        file.write(f'{username},{birthday},{gender},{salary},{position}\n')
   
 
 
def view_staff():
    with open('Staff_info.txt','r') as file:
        file.seek(0)
        for line in file:
            print(line.strip())
 
def search_staff():
        Username = input('enter the ID you want to search:\n ')
        with open('Staff_info.txt', 'r') as file:
            file.seek(0)
            for line in file:
                SU, SB, SG, SS, SP = line.strip().split(',')
                if SU == Username:
                    print(f"username: {SU}, birthday: {SB}, gender: {SG}, salary: {SS}, position: {SP}")
             
def edit_staff():
    # Read all lines from the file
    with open('staff_info.txt', 'r') as file:
        lines = file.readlines()
    with open('add_staff_member.txt','r') as file:
        lines2 = file.readlines()
    
    # Get the username to edit
    edit_username = input('Enter the ID you want to edit:\n ')
    
    # Open the file in write mode to update it
    with open('staff_info.txt', 'w') as file:
        file.seek(0)
        for line in lines:
            if line.startswith(edit_username):
                lines = line.strip()
                print(f"Current details: {lines}")
                new_username = input('Enter new username: ')
                new_password = input('Enter new password:')
                birthday = input('Enter new birthday (DD/MM/YYYY): ')
                gender = input('Enter new gender (male/female): ')
                salary = input('Enter new salary: ')
                position = input('Enter new position: ')
                file.write(f'{new_username}, {birthday}, {gender}, {salary}, {position}\n')
            else:
                file.write(line)

    with open('add_staff_member.txt', 'w') as file:
        file.seek(0)
        for line in lines2:
            if line.startswith(edit_username):
                file.write(f'{new_username}, {new_password}\n')
            else:
                file.write(line)
                

        
 
def remove_staff():
    # read all line in file and save it in lines
    with open('staff_info.txt', 'r') as file:
        lines = file.readlines()
    with open('add_staff_member.txt', 'r') as file2:
        lines2 = file2.readlines()
 
    remove_username = input('Enter the ID you want to remove:\n ')
   
    with open('staff_info.txt', 'w') as file:
       
        for line in lines:
            lines = line.strip()
            if not line.startswith(remove_username):
                file.write(line)
    
    with open('staff_list.txt', 'w') as file:
       
        for line in lines2:
            lines = line.strip()
            if not line.startswith(remove_username):
                file.write(line)
               
           

       

def add_member():
    print('add a new account')
    username = input('New username :')
    password = input('New password :')
    birthday = input('enter your birthday (DD/MM/YYY) : ')
    gender = input('enter your gender (male/female) : ')

    with open('member_list.txt','a+') as file1:
        file1.seek(0)
        for line in file1:
            if line.startswith(username):
                print('username already exist.')
                return






    with open ('member_list.txt', 'a+') as file:
        file.seek(0)
        file.write(f'{username},{password}\n')
        
    with open ('member_info.txt', 'a+') as file2:
        file2.seek(0)
        file2.write(f'{username},{birthday},{gender}\n')


def view_member():
    with open ('member_info.txt', 'r') as file:
        for line in file:
            print(line.strip())


def search_member():
    with open('member_info.txt','r') as file:
        Username = input('enter the ID you want to search:\n ')
        for line in file:
            SU, SB, SG = line.strip().split(',')
            if SU == Username:
                print(f"username: {SU}, birthday: {SB}, gender: {SG}")



def edit_member():
     # Read all lines from the file
    with open('member_info.txt', 'r') as file:
        lines = file.readlines()
    with open('add_member.txt','r') as file:
        lines2 = file.readlines()
   
    # Get the username to edit
    edit_username = input('Enter the ID you want to edit:\n ')
   
    # Open the file in write mode to update it
    with open('member_info.txt', 'w') as file:
        for line in lines:
            if line.startswith(edit_username):
                lines = line.strip()
                print(f"Current details: {lines}")
                new_username = input('Enter new username: ')
                new_password = input('Enter new password: ')
                birthday = input('Enter new birthday (DD/MM/YYYY): ')
                gender = input('Enter new gender (male/female): ')
                file.write(f'{new_username},{birthday},{gender}\n')
            else:
                file.write(line)

    with open('add_member.txt', 'w') as file:
        file.seek(0)
        for line in lines2:
            if line.startswith(edit_username):
                file.write(f'{new_username}, {new_password}\n')
            else:
                file.write(line)


def delete_member():
    # read all line in file and save it in lines
    with open('member_info.txt', 'r') as file:
        lines = file.readlines()
    with open('add_member.txt', 'r') as file2:
        lines2 = file2.readlines()
 
    remove_username = input('Enter the ID you want to remove:\n ')
   
    with open('member_info.txt', 'w') as file:
       
        for line in lines:
            lines = line.strip()
            if not line.startswith(remove_username):
                file.write(line)
               
           
    with open('login','w') as file2:
        for line in lines2:
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
                                return

                    elif line.startswith('ADM'):
                        print(f'you are loged in as {username}, enter your selection:')
                        ADMmenu()
                        
                       
                       
                       
                        for i in range(20):
                            repeat = input('Return to admin menu?(Y/N): ')
                            repeat = repeat.upper()
                            if repeat == 'Y':
                                ADMmenu()
                            else:
                                return
                                 
            else:
                print('incorrect username or password')   
                exit()                          
    except:
        print('The program has been exited')
        exit()                    

 
start_superadmin()
login()
