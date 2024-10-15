# Guys remember all the code needs to come togethere here, somehow


# dear admin team, sorry for touching your code, just a little optimization ~T



def Addstaff():
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
    # Store staff data in a file
    with open('staff_list.txt', "a") as t:
        t.write(str(new_staff) + '\n')

    print(f'Added staff: {name_staff}')


def Addmember():
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

    # Store member data in a file
    with open('member_list.txt', "a") as t:
        t.write(str(new_member) + '\n')

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


# Note from T to team: Remember to find a way to allow members to change their data and only their data. make a diferent function maybe?
# Note from T to team, edit members doesn't work  yet, it works but not the way it's supposed to, imma leave fixing it to the admin team :D
def ADMINTERMINAL():  # First step is to add new staff
    print('''Welcome to library staff and member management system:
          1. Add new staff
          2. View librarian staff
          3. Search librarian staff
          4. Edit staff
          5. Remove staff
          6. Add new member
          7. View all member information
          8. Search member information
          9. Edit member 
          10. Delete member''')
    ADMchoice = int(input('Enter your selection:'))
    if ADMchoice == 1:
        Addstaff()
    elif ADMchoice == 2:
        view_staff()
    elif ADMchoice == 3:
        search_staff()  # hmm
    elif ADMchoice == 4:
        edit_staff()  # Will be added soon
    elif ADMchoice == 5:
        remove_staff()  # eh
    elif ADMchoice == 6:
        Addmember()
    elif ADMchoice == 7:
        view_member()
    elif ADMchoice == 8:
        search_member()
    elif ADMchoice == 9:
        editmember()
    elif ADMchoice == 10:
        delete_member()


# What is getpass?
def login():
    print('Please enter your ID and password')
    username = input('ID: ')
    password = input("Password: ")
    encrypted_password = password.encode("utf-8").hex()  # Encrypt input password to hex to compare with hex in list

    def check_credentials(file_name, user_type):
        # Quick funtion to check both lists (￣_,￣ )
        try:
            with open(file_name, 'r') as file:
                for line in file:
                    # Extract the user information and encrypted password from the file
                    if user_type == 'staff':
                        user_info = eval(line.strip())["STAFF"]
                    elif user_type == 'member':
                        user_info = eval(line.strip())["MEMBER"]

                    for user in user_info:
                        if user['ID'] == username and user['Password'] == encrypted_password:
                            return user  # Return the user details if match found
        except FileNotFoundError:
            print(f"Error: {file_name} not found.")
            return None

    superADM_user = check_credentials('SuperAdmin.txt', 'SuperAdmin')
    # Check staff list for the user
    staff_user = check_credentials('staff_list.txt', 'staff')

    # Check member list for the user
    member_user = check_credentials('member_list.txt', 'member')

    # Handle login logic based on whether the user was found in staff or member list
    if staff_user:
        # If staff, check if they are an admin or librarian


        if superADM_user['ID'].startswith('ADM'):
            print('You are logged in as an Admin\n')
            ADMINTERMINAL()
            for i in range(20):
                repeat = input('Return to Admin menu? (Y/N): ').upper()
                if repeat == 'Y':
                    ADMINTERMINAL()
        if staff_user['ID'].startswith('SDM'):
            print('You are logged in as super admin\n')
            ADMINTERMINAL()
            for i in range(20):
                repeat = input('Would you like to add another admin? (Y/N): ').upper()
                if repeat == 'Y':
                    ADMINTERMINAL()
                else:
                    break

        elif staff_user['ID'].startswith('LB'):
            print('You are logged in as a librarian\n')
            print("TBA")
            for i in range(20):
                repeat = input('Return to librarian menu? (Y/N): ').upper()
                if repeat == 'Y':
                    print("TBA")
                else:
                    break

    elif member_user:
        print(f'Welcome {member_user["Name"]}, you are logged in as a library member.')
        # Add member-specific functionality here if needed

    else:
        print('Invalid credentials. Please try again.')


# Note from T: Librarian menu for books will be made
login()
# Also, remember to add comments, makes code easier to understand :3