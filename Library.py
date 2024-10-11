#Guys remember all the code needs to come togethere here, somehow


# dear admin team, sorry for touching your code, just a little optimization ~T

#Super admin code will aslo be optimized in due time
# def start_superadmin():
#     SDM_username = 'SDM001'
#     SDM_password = 'SDMpass001'
#     #Super admin (exiting account)
   
#     superadmin_credentials = f"{SDM_username},{SDM_password}"
   
#     with open('login.txt','a+') as file:
#         pass
#     # Automatically create login.txt
 
#     with open("login.txt", 'r+') as file:
#         lines = file.readlines()
#         for line in lines:
#             if line.strip() == superadmin_credentials:
#                 return


def Addstaff():
    dik = {"STAFF": []}
    name_staff = input('Insert Name: ')
    id_staff = input('Insert ID: (ADM-ADMIN, LB-librarian)')  # ADM001/LB0001
    email_staff = input('Insert Email: ')
    password_staff = input('Insert Password: ')
    AdminPerms = input('Has Admins (Yes/No): ')  # Librarians don't have admin status
    encryption = password_staff.encode("utf-8").hex()  # Convert password to hex

    # Combine staff details and password into one dictionary
    new_staff = {
        'Name': name_staff, 
        'ID': id_staff, 
        'Email': email_staff, 
        'HasPerms': AdminPerms, 
        'Password': encryption
    }
    
    # Append staff to list
    dik["STAFF"].append(new_staff)
    
    # Store staff data in a file
    with open('staff_list.txt', "a") as t:
        t.write(str(dik) + '\n')
    
    print(f'Added staff: {name_staff}')

def Addmember():
    dic = {"MEMBER": []}
    name_member = input('Insert Name: ')
    id_member = input('Insert ID: (M###)')  # M001
    email_member = input('Insert Email: ')
    password_member = input('Insert Password: ')
    encryption = password_member.encode("utf-8").hex()  # Convert password to hex

    # Combine member details and password into one dictionary
    new_member = {
        'Name': name_member, 
        'ID': id_member, 
        'Email': email_member, 
        'Password': encryption
    }
    
    # Append member to list
    dic["MEMBER"].append(new_member)
    
    # Store member data in a file
    with open('member_list.txt', "a") as t:
        t.write(str(dic) + '\n')
    
    print(f'Added member: {name_member}')

def view_staff():
    # Read and print staff list from file
    with open('staff_list.txt', 'r') as file:
        for line in file:
            print(line)
def view_member():
    # Read and print staff list from file
    with open('member_list.txt', 'r') as file:
        for line in file:
            print(line)
def editmember():
    # Read all lines from the file
    with open('member_list.txt', 'r') as file:
        lines = file.readlines()
    
    # Get the member ID to edit
    UserID = input('Enter the ID you want to edit:\n')
    
    # Open the file in write mode to update the member info
    with open('member_list.txt', 'w') as file:
        for line in lines:
            if UserID in line:
                # Extract the current details
                print(f"Current details: {line.strip()}")
                
                # Prompt for new details
                new_username = input('Enter new Name: ')
                passwordchange = input('Insert New Password: ')
                encryption = passwordchange.encode("utf-8").hex()  # Encrypt the new password
                
                # Update the member's details
                updated_line = line.replace(line.strip(), f"Name: {new_username}, Password: {encryption}")
                file.write(updated_line + '\n')
            else:
                # Write the unchanged lines back to the file
                file.write(line)
#Note from T to team: Remember to find a way to allow members to change their data and only their data. make a diferent function maybe?
#Note from T to team, edit members doesn't work  yet, it works but not the way it's supposed to, imma leave fixing it to the admin team :D
def LBS(): # First step is to add new staff
    print('''Welcome to staff management system:
          1. Add new staff
          2. View librarian staff
          3. Search librarian staff
          4. Edit staff
          5. Remove staff''')
    LBSchoice = int(input('Enter your selection:'))
    if LBSchoice == 1:
        Addstaff()
    elif LBSchoice == 2:
        view_staff()
    elif LBSchoice == 3:
        search_staff()#hmm
    elif LBSchoice == 4:
        edit_staff()# Will be added soon
    elif LBSchoice == 5:
        remove_staff()#eh

def LBM():
    print('''Welcome to member management system 
          1. Add new member
          2. View all member information
          3. Search member information
          4. Edit member 
          5. Delete member''')
    LBMchoice = int(input('Enter your selection : '))
    if LBMchoice == 1 :
        Addmember()
    elif LBMchoice == 2 :
        view_member()
    elif LBMchoice == 3 :
        search_member()
    elif LBMchoice == 4 :
        editmember()
    elif LBMchoice == 5 :
        delete_member()
    
#What is getpass?
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

#Also, remember to add comments, makes code easier to understand :3