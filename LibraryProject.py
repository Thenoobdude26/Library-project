# super admin username: SDM001 and password: SDMpassword
# Log in as super admin first to create an admin account
import datetime
import time
import hashlib
def encrypt_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
    #changed from putting them into Hex to Base64, more secure


#important Functions below
def start_superadmin():
    SDM_username = 'SDM001'
    SDM_password = 'SDMpass001'
    encrypted_password = encrypt_password(SDM_password)

    superadmin_credentials = f"{SDM_username},{encrypted_password}"

    with open('login.txt', 'a+') as file:
        pass
    # Check if super admin credentials already exist
    with open("login.txt", 'r') as file:
        lines = file.readlines()
        for line in lines:
            if line.strip() == superadmin_credentials:
                return

    if superadmin_credentials not in lines:
        # Add super admin credentials if they do not exist
        with open("login.txt", 'a+') as file:
            file.write(f'{superadmin_credentials}\n')
def add_staff():
    print('Add a new staff account:')
    username = input("Username: ")
    password = input('Password: ')
    encrypted_password = encrypt_password(password)
    name = input('Enter name: ')
    gender = input('Enter gender (male/female): ')
    salary = input('Salary: ')
    position = input('Position: ')

    with open('stafflogin.txt', 'a+') as file:
        for line in file:
            if line.startswith(username):
                print('Account already exists.\n')
                return

    with open('stafflogin.txt', 'a+') as file:
        file.write(f'Name: {username},Password: {encrypted_password}\n')

    with open('staff_info.txt', 'a+') as file:
        file.write(f'ID: {username},Name: {name},Gender: {gender},Salary: {salary},Position: {position}\n')
def view_staff():
    with open('staff_info.txt', 'r') as file:
        file.seek(0)
        for line in file:
            print(line)
def search_staff():
    Username = input('enter the ID you want to search:\n ')
    with open('staff_info.txt', 'r') as file:
        file.seek(0)
        for line in file:
            SU, SB, SG, SS, SP = line.strip().split(',')
            if SU == Username:
                print(f"username: {SU}, birthday: {SB}, gender: {SG}, salary: {SS}, position: {SP}")
def edit_staff():
    # Read all lines from the file
    with open('staff_info.txt', 'r') as file:
        lines = file.readlines()
    with open('stafflogin.txt', 'r') as file:
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
                encrypted_password = encrypt_password(new_password)
                birthday = input('Enter new birthday (DD/MM/YYYY): ')
                gender = input('Enter new gender (male/female): ')
                salary = input('Enter new salary: ')
                position = input('Enter new position: ')
                file.write(f'{new_username}, {birthday}, {gender}, {salary}, {position}\n')
            else:
                file.write(line)

    with open('stafflogin.txt', 'w') as file:
        file.seek(0)
        for line in lines2:
            if line.startswith(edit_username):
                file.write(f'{new_username}, {encrypted_password}\n')
            else:
                file.write(line)
def remove_staff():
    # read all line in file and save it in lines
    with open('staff_info.txt', 'r') as file:
        lines = file.readlines()
    with open('stafflogin.txt', 'r') as file2:
        lines2 = file2.readlines()

    remove_username = input('Enter the ID you want to remove:\n ')

    with open('staff_info.txt', 'w') as file:

        for line in lines:
            lines = line.strip()
            if not line.startswith(remove_username):
                file.write(line)

    with open('stafflogin.txt', 'w') as file:

        for line in lines2:
            lines = line.strip()
            if not line.startswith(remove_username):
                file.write(line)
def add_member():
    print('Add a new member account:')
    username = input('New username: ')
    password = input('New password: ')
    encrypted_password = encrypt_password(password)
    name = input('Enter name: ')
    gender = input('Enter gender (male/female): ')

    with open('memberlogin.txt', 'a+') as file:
        for line in file:
            if line.startswith(username):
                print('Username already exists.')
                return

    with open('memberlogin.txt', 'a') as file:
        file.write(f'Name: {username},Password: {encrypted_password}\n')

    with open('member_info.txt', 'a+') as file:
        file.write(f'ID: {username},Name: {name},Gender: {gender}\n')
def view_member():
    with open('member_info.txt', 'r') as file:
        for line in file:
            print(line.strip())
def search_member():
    with open('member_info.txt', 'r') as file:
        Username = input('enter the ID you want to search:\n ')
        for line in file:
            SU, SB, SG = line.strip().split(',')
            if SU == Username:
                print(f"username: {SU}, birthday: {SB}, gender: {SG}")
def edit_member():
    # Read all lines from the file
    with open('member_info.txt', 'r') as file:
        lines = file.readlines()
    with open('memberlogin.txt', 'r') as file:
        lines2 = file.readlines()

    # Get the username to edit
    edit_username = input('Enter the ID you want to edit:\n ')

    # Open the file in write mode to update it
    with open('member_info.txt', 'w') as file:
        for line in lines:
            if line.startswith(edit_username):
                lines = line.strip()
                SU, SB, SG = lines.split(',')
                print(f"Current details: username:{SU}, birthday: {SB}, Gender: {SG}")
                new_username = input('Enter new username: ')
                new_password = input('Enter new password: ')
                encrypted_password = encrypt_password(new_password)
                birthday = input('Enter new birthday (DD/MM/YYYY): ')
                gender = input('Enter new gender (male/female): ')
                file.write(f'{new_username},{birthday},{gender}\n')
            else:
                file.write(line)

    with open('memberlogin.txt', 'w') as file:
        file.seek(0)
        for line in lines2:
            if line.startswith(edit_username):
                file.write(f'{new_username}, {encrypted_password}\n')
            else:
                file.write(line)
def delete_member():
    # read all line in file and save it in lines
    with open('member_info.txt', 'r') as file:
        lines = file.readlines()
    with open('memberlogin.txt', 'r') as file2:
        lines2 = file2.readlines()

    remove_username = input('Enter the ID you want to remove:\n ')

    with open('member_info.txt', 'w') as file:

        for line in lines:
            lines = line.strip()
            if not line.startswith(remove_username):
                file.write(line)

    with open('memberlogin.txt', 'w') as file2:
        for line in lines2:
            file2line = line.strip()
            if not remove_username.startswith(remove_username):
                file2.write(line)
def AddBook():
    print("Insert Book details Below: ")
    print("------------------------------")
    name_book = input('Insert Name: ')
    ISBN = input('INSERT ISBN: ')  #
    author = input('Insert Author/s ')
    genre = input('Genre: ')
    publishDate = input('Date Published: ')
    current_date_time = datetime.datetime.now()
    addDate = current_date_time.date()  # date added to catalogue
    Available = "Yes"

    new_book = {
        'Book Name': name_book,
        'ISBN': ISBN,
        'Author': author,
        'Genre': genre,
        'Date Published': publishDate,
        'Date Added': addDate,
        'Available': Available
    }

    with open('Book_catalogue.txt', "a") as t:
        t.write(str(new_book) + '\n')

    print(f'{name_book} has been added to the catalogue, under {genre}')
def view_Allbooks():
    # Read and print staff list from file
    with open('Book_catalogue.txt', 'r') as file:
        for line in file:
            print(line)
def search_book():
    print("What book are you looking for?: ")
    search_term = input(" ")
    with open('Book_catalogue.txt', 'r') as file:
        found = False
        for line in file:
            if search_term.lower() in line.lower():
                print(line)
                found = True
        if not found:
            print("No matching books found.")
def loan_book():
    print("Insert ISBN of the book to be loaned: ")
    isbn = input(" ")
    print("Member ID of loaner: ")
    loaner = input(" ")
    print("Date Loaned (YYYY/MM/DD): ")
    dateloaned = input("")
    loanID = "LID" + dateloaned + loaner + isbn

    with open('Book_catalogue.txt', 'r') as file:
        lines = file.readlines()

    with open('Book_catalogue.txt', 'w') as file:
        for line in lines:
            if isbn in line and "'Available': 'Yes'" in line:
                book = eval(line.strip())
                book['Available'] = 'No'
                file.write(str(book) + '\n')
                print(f"Book with ISBN {isbn} has been loaned out.")
            else:
                file.write(line)

    with open('loan_logs.txt', 'a') as log_file:
        log_file.write(f"LOANID: {loanID}, ISBN: {isbn}, Member ID: {loaner}, Date Loaned: {dateloaned}\n")
def return_book():
    print("Insert ISBN of the book to be returned: ")
    isbn = input(" ")
    print("Member ID of returner: ")
    returner = input(" ")
    print("Date Returned (YYYY/MM/DD): ")
    datereturned = input("")
    returnID = "LID" + datereturned + returner + isbn

    with open('Book_catalogue.txt', 'r') as file:
        lines = file.readlines()

    with open('Book_catalogue.txt', 'w') as file:
        for line in lines:
            if isbn in line and "'Available': 'No'" in line:
                book = eval(line.strip())
                book['Available'] = 'Yes'
                file.write(str(book) + '\n')
                print(f"Book with ISBN {isbn} has been returned.")
            else:
                file.write(line)

    with open('return_logs.txt', 'a') as log_file:
        log_file.write(f" RETURNID: {returnID}, ISBN: {isbn}, Member ID: {returner}, Date Returned: {datereturned}\n")
def edit_catalogue():
    print("Insert ISBN of the book to be edited: ")
    isbn = input(" ")
    print("What would you like to edit? (Name/Author/Genre/Date Published/Available): ")
    field = input(" ")
    print("What would you like to change it to?: ")
    new_value = input(" ")

    with open('Book_catalogue.txt', 'r') as file:
        lines = file.readlines()

    with open('Book_catalogue.txt', 'w') as file:
        for line in lines:
            if isbn in line:
                book = eval(line.strip())
                book[field] = new_value
                file.write(str(book) + '\n')
                print(f"Book with ISBN {isbn} has been updated.")
            else:
                file.write(line)
def view_logs():
    print("Loan Logs:")
    with open('loan_logs.txt', 'r') as file:
        for line in file:
            print(line.strip())

    print("\nReturn Logs:")
    with open('return_logs.txt', 'r') as file:
        for line in file:
            print(line.strip())
def search_loan():
    print("Insert Member ID: ")
    memberid = input(" ")
    loans = []

    with open('loan_logs.txt', 'r') as file:
        for line in file:
            if memberid.lower() in line.lower():
                loans.append(line.strip())

    if not loans:
        print("No Loans found for user.")
        return

    # Find the most recent loan
    most_recent_loan = None
    for loan in loans:
        if "Date Loaned" in loan:
            most_recent_loan = loan

    if most_recent_loan:
        print(most_recent_loan)
        loan_date_str = most_recent_loan.split("Date Loaned: ")[1].split(",")[0]
        loan_date = datetime.datetime.strptime(loan_date_str.strip(), "%Y/%m/%d").date()
        current_date = datetime.datetime.now().date()
        days_since_loan = (current_date - loan_date).days

        # Check if the loan has been returned
        with open('return_logs.txt', 'r') as return_file:
            returned = False
            return_date_str = None
            for return_line in return_file:
                if memberid.lower() in return_line.lower() and "Date Returned" in return_line:
                    return_date_str = return_line.split("Date Returned: ")[1].split(",")[0]
                    returned = True
                    break

        if returned:
            return_date = datetime.datetime.strptime(return_date_str.strip(), "%Y/%m/%d").date()
            days_late = (return_date - loan_date).days - 14
            if days_late > 0:
                if days_late == 1:
                    fee = 2
                elif days_late == 2:
                    fee = 3
                elif days_late == 3:
                    fee = 4
                elif days_late == 4:
                    fee = 5
                elif days_late == 5:
                    fee = 6
                else:
                    fee = 10
                print(f"Late fee: {fee} RM")
            else:
                print("No late fee.")
            print(f"Date Returned: {return_date_str}")
        else:
            days_left = 14 - days_since_loan
            if days_left > 0:
                print(f"Time left before fee: {days_left} days")
            else:
                days_late = abs(days_left)
                if days_late == 1:
                    fee = 2
                elif days_late == 2:
                    fee = 3
                elif days_late == 3:
                    fee = 4
                elif days_late == 4:
                    fee = 5
                elif days_late == 5:
                    fee = 6
                else:
                    fee = 10
                print(f"Late fee: {fee} RM")
    else:
        print("No recent loans found.")
def edit_logs():
    print("Insert Loan ID: ")
    loanid = input(" ")
    print("What would you like to edit? (ISBN/Member ID/Date Loaned): ")
    field = input(" ")
    print("What would you like to change it to?: ")
    new_value = input(" ")

    with open('loan_logs.txt', 'r') as file:
        lines = file.readlines()

    with open('loan_logs.txt', 'w') as file:
        for line in lines:
            if loanid in line:
                loan = eval(line.strip())
                loan[field] = new_value
                file.write(str(loan) + '\n')
                print(f"Loan with ID {loanid} has been updated.")
            else:
                file.write(line)

    with open('return_logs.txt', 'r') as file:
        lines = file.readlines()

    with open('return_logs.txt', 'w') as file:
        for line in lines:
            if loanid in line:
                loan = eval(line.strip())
                loan[field] = new_value
                file.write(str(loan) + '\n')
                print(f"Loan with ID {loanid} has been updated.")
            else:
                file.write(line)

#menu functions below
#PS remember to fix check credentials
def superadmin():
    print('add a new admin account:')
    username = input("username: ")
    password = input('password: ')
    encrypted_password = encrypt_password(password)

    with open('login.txt', 'r') as file:
        for line in file:
            if line.startswith(username):
                print('account already exist, run the program again')
                return

    with open("login.txt", 'a+') as file:
        file.write(f'{username},{encrypted_password}\n')
def ADMmenu():  # Admin perms
    print('''
=====================================
||       Admin Management         ||
=====================================
||  1. Manage librarian staff     ||
||  2. Manage librarian member    ||
||  3. Logout                     ||
=====================================
''')

    choice = int(input('enter your choice: '))

    if choice == 1:
        LBS()
    elif choice == 2:
        LBM()
    elif choice == 3:
        login()
        return
def LBS():
    print('''
=====================================
||     Staff Management System     ||
=====================================
||  1. Add new staff               ||
||  2. View librarian staff        ||
||  3. Search librarian staff      ||
||  4. Edit staff                  ||
||  5. Remove staff                ||
||  6. Back                        ||
=====================================
''')
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
    print('''
=====================================
||    Member Management System     ||
=====================================
||  1. Add new member              ||
||  2. View all member information ||
||  3. Search member information   ||
||  4. Edit member                 ||
||  5. Delete member               ||
||  6. Back                        ||
=====================================
''')
    LBMchoice = int(input('Enter your selection : '))
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
def librarian_menu():
    while True:
        print("\n")
        print("=====================================")
        print("||  Welcome to the Library System  ||")
        print("=====================================")
        print("||                                 ||")
        print("||  1. Add Book                    ||")
        print("||  2. View All Books              ||")
        print("||  3. Search Book                 ||")
        print("||  4. Loan Book                   ||")
        print("||  5. Return Book                 ||")
        print("||  6. Edit Catalogue              ||")
        print("||  7. View Loan Logs              ||")
        print("||  8. Search Loan                 ||")
        print("||  9. Edit Logs                   ||")
        print("|| 10. Logout                      ||")
        print("||                                 ||")
        print("=====================================")
        choice = input("Enter your choice: ")

        if choice == '1':
            AddBook()
        elif choice == '2':
            view_Allbooks()
        elif choice == '3':
            search_book()
        elif choice == '4':
            loan_book()
        elif choice == '5':
            return_book()
        elif choice == '6':
            edit_catalogue()
        elif choice == '7':
            view_logs()
        elif choice == '8':
            search_loan()
        elif choice == '9':
            edit_logs()
        elif choice == '10':
            login()
            return
        else:
            print("Invalid choice. Please try again.")

        time.sleep(2)
def check_credentials(file_path, username, encrypted_password):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) < 2:
                    continue  # Skip lines that do not have both username and password
                stored_username = parts[0].split(':')[1].strip() if ':' in parts[0] else parts[0].strip()
                stored_password = parts[1].split(':')[1].strip() if ':' in parts[1] else parts[1].strip()
                if stored_username == username and stored_password == encrypted_password:
                    return True
    except FileNotFoundError:
        pass
    return False
def get_name(file_path, user_id):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if user_id in line:
                    parts = line.split(',')
                    for part in parts:
                        if part.startswith('Name:'):
                            return part.split(':')[1].strip()
    except FileNotFoundError:
        pass
    return None
def login():
    print('Please enter your ID and password')
    username = input('ID: ')
    password = input('password: ')
    encrypted_password = encrypt_password(password)

    if check_credentials('login.txt', username, encrypted_password):
        if username.startswith('SDM'):
            print('You are logged in as super admin\n')
            superadmin()
            for i in range(20):
                repeat = input('Would you like to add another admin?(Y/N): ')
                repeat = repeat.upper()
                if repeat == 'Y':
                    superadmin()
                else:
                    return
        elif username.startswith('ADM'):
            print(f'You are logged in as {username}, enter your selection:')
            ADMmenu()
            for i in range(20):
                repeat = input('Return to admin menu?(Y/N): ')
                repeat = repeat.upper()
                if repeat == 'Y':
                    ADMmenu()
                else:
                    return
    elif check_credentials('memberlogin.txt', username, encrypted_password):
        if username.startswith('M'):
            name = get_name('member_info.txt', username)
            print(f'You are logged in as {name}')
            # Add member-specific menu or actions here
    elif check_credentials('stafflogin.txt', username, encrypted_password):
        if username.startswith('LB'):
            name = get_name('staff_info.txt', username)
            print(f'You are logged in as {name}')
            librarian_menu()
            for i in range(20):
                repeat = input('Return to librarian menu?(Y/N): ')
                repeat = repeat.upper()
                if repeat == 'Y':
                    librarian_menu()
                else:
                    return
    else:
        print('Incorrect username or password')
        exit()

start_superadmin()
# librarian_menu()
login()


