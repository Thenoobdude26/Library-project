#Guys remember all the code needs to come togethere here, somehow

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
#Also, remember to add comments, makes code easier to understand :3