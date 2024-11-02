import getpass
import os

def start_superadmin():
    SDM_username = 'SDM001'
    SDM_password = 'SDMpass001'
    superadmin_credentials = f"{SDM_username},{SDM_password}"

    if not os.path.exists('login.txt'):
        with open('login.txt', 'w') as file:
            pass

    with open('login.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.strip() == superadmin_credentials:
                return

    with open('login.txt', 'a') as file:
        file.write(f'{superadmin_credentials}\n')

def superadmin():
    print('Add a new admin account:')
    username = input("Username: ")
    password = input('Password: ')

    with open('login.txt', 'r') as file:
        for line in file:
            if line.startswith(username):
                print('Account already exists, run the program again')
                return

    with open('login.txt', 'a') as file:
        file.write(f'{username},{password}\n')

def ADMmenu():
    print('''
           1. Manage librarian staff
           2. Manage librarian member
           3. Logout''')

    choice = int(input('Enter your choice: '))

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
    LBMchoice = int(input('Enter your selection: '))
    if LBMchoice == 1:
        add_member()
    elif LBMchoice == 2:
        view_member()
    elif LBMchoice == 3:
        search_member()
    elif LBMchoice == 4:
        edit_member()
    elif LBMchoice == 5:
        delete_member()
    elif LBMchoice > 5 or LBMchoice < 1:
        return

def add_staff():
    print('Add a new account:')
    username = input("Username: ")
    password = input('Password: ')
    birthday = input('Enter birthday (DD/MM/YYYY): ')
    gender = input('Enter gender (male/female): ')
    salary = input('Salary: ')
    position = input('Position: ')

    with open('stafflogin.txt', 'a+') as file:
        file.seek(0)
        for line in file:
            if line.startswith(username):
                print('Account already exists.\n')
                return

    with open('stafflogin.txt', 'a') as file:
        file.write(f'{username},{password}\n')

    with open('staff_info.txt', 'a') as file:
        file.write(f'{username},{birthday},{gender},{salary},{position}\n')

def view_staff():
    with open('staff_info.txt', 'r') as file:
        for line in file:
            print(line.strip())

def search_staff():
    username = input('Enter the ID you want to search:\n ')
    with open('staff_info.txt', 'r') as file:
        for line in file:
            SU, SB, SG, SS, SP = line.strip().split(',')
            if SU == username:
                print(f"Username: {SU}, Birthday: {SB}, Gender: {SG}, Salary: {SS}, Position: {SP}")

def edit_staff():
    with open('staff_info.txt', 'r') as file:
        lines = file.readlines()
    with open('stafflogin.txt', 'r') as file:
        lines2 = file.readlines()

    edit_username = input('Enter the ID you want to edit:\n ')

    with open('staff_info.txt', 'w') as file:
        for line in lines:
            if line.startswith(edit_username):
                SU, SB, SG, SS, SP = line.strip().split(',')
                print(f"Current details: Username: {SU}, Birthday: {SB}, Gender: {SG}, Salary: {SS}, Position: {SP}")
                new_username = input('Enter new username: ')
                new_password = input('Enter new password: ')
                birthday = input('Enter new birthday (DD/MM/YYYY): ')
                gender = input('Enter new gender (male/female): ')
                salary = input('Enter new salary: ')
                position = input('Enter new position: ')
                file.write(f'{new_username},{birthday},{gender},{salary},{position}\n')
            else:
                file.write(line)

    with open('stafflogin.txt', 'w') as file:
        for line in lines2:
            if line.startswith(edit_username):
                file.write(f'{new_username},{new_password}\n')
            else:
                file.write(line)

def remove_staff():
    with open('staff_info.txt', 'r') as file:
        lines = file.readlines()
    with open('stafflogin.txt', 'r') as file:
        lines2 = file.readlines()

    remove_username = input('Enter the ID you want to remove:\n ')

    with open('staff_info.txt', 'w') as file:
        for line in lines:
            if not line.startswith(remove_username):
                file.write(line)

    with open('stafflogin.txt', 'w') as file:
        for line in lines2:
            if not line.startswith(remove_username):
                file.write(line)

def add_member():
    print('Add a new account:')
    username = input('New username: ')
    password = input('New password: ')
    birthday = input('Enter your birthday (DD/MM/YYYY): ')
    gender = input('Enter your gender (male/female): ')

    with open('memberlogin.txt', 'a+') as file:
        file.seek(0)
        for line in file:
            if line.startswith(username):
                print('Username already exists.')
                return

    with open('memberlogin.txt', 'a') as file:
        file.write(f'{username},{password}\n')

    with open('member_info.txt', 'a') as file:
        file.write(f'{username},{birthday},{gender}\n')

def view_member():
    with open('member_info.txt', 'r') as file:
        for line in file:
            print(line.strip())

def search_member():
    username = input('Enter the ID you want to search:\n ')
    with open('member_info.txt', 'r') as file:
        for line in file:
            SU, SB, SG = line.strip().split(',')
            if SU == username:
                print(f"Username: {SU}, Birthday: {SB}, Gender: {SG}")

def edit_member():
    with open('member_info.txt', 'r') as file:
        lines = file.readlines()
    with open('memberlogin.txt', 'r') as file:
        lines2 = file.readlines()

    edit_username = input('Enter the ID you want to edit:\n ')

    with open('member_info.txt', 'w') as file:
        for line in lines:
            if line.startswith(edit_username):
                SU, SB, SG = line.strip().split(',')
                print(f"Current details: Username: {SU}, Birthday: {SB}, Gender: {SG}")
                new_username = input('Enter new username: ')
                new_password = input('Enter new password: ')
                birthday = input('Enter new birthday (DD/MM/YYYY): ')
                gender = input('Enter new gender (male/female): ')
                file.write(f'{new_username},{birthday},{gender}\n')
            else:
                file.write(line)

    with open('memberlogin.txt', 'w') as file:
        for line in lines2:
            if line.startswith(edit_username):
                file.write(f'{new_username},{new_password}\n')
            else:
                file.write(line)

def delete_member():
    with open('member_info.txt', 'r') as file:
        lines = file.readlines()
    with open('memberlogin.txt', 'r') as file:
        lines2 = file.readlines()

    remove_username = input('Enter the ID you want to remove:\n ')

    with open('member_info.txt', 'w') as file:
        for line in lines:
            if not line.startswith(remove_username):
                file.write(line)

    with open('memberlogin.txt', 'w') as file:
        for line in lines2:
            if not line.startswith(remove_username):
                file.write(line)

def login():
    print('Please enter your ID and password')
    username = input('Username: ')
    password = input('Password: ')

    try:
        with open('login.txt', 'r') as file:
            for line in file:
                stored_username, stored_password = line.strip().split(',')

                if stored_username == username and stored_password == password:
                    if line.startswith('SDM'):
                        print('You are logged in as super admin\n')
                        superadmin()
                        for i in range(20):
                            repeat = input('Would you like to add another admin? (Y/N): ')
                            if repeat.upper() == 'Y':
                                superadmin()
                            else:
                                return

                    elif line.startswith('ADM'):
                        print(f'You are logged in as {username}, enter your selection:')
                        ADMmenu()
                        for i in range(20):
                            repeat = input('Return to admin menu? (Y/N): ')
                            if repeat.upper() == 'Y':
                                ADMmenu()
                            else:
                                return
            else:
                print('Incorrect username or password')
                exit()
    except Exception as e:
        print(f'An error occurred: {e}')
        exit()

start_superadmin()
login()