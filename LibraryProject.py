# super admin username: SDM001 and password: SDMpass001
# Log in as super admin first to create an admin account
import datetime
import time
import hashlib
def encrypt_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
    #changed from putting them into Hex to Base64, more secure



#important Functions below.
def add_admin():
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
    print('Admin account created successfully')
    print('Returning to main menu')
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    superadminmenu()
def view_admin():
    with open('login.txt', 'r') as file:
        for line in file:
            print(line)
    print('Type Y to return to main menu')
    choice = input(' ')
    if choice == 'Y':
        print("returning to main menu")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        superadminmenu()
    else:
        print("I think you meant Y. returning to menu")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        superadminmenu()
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
        file.write(f'ID: {username},Password: {encrypted_password}\n')

    with open('staff_info.txt', 'a+') as file:
        file.write(f'ID: {username},Name: {name},Gender: {gender},Salary: {salary},Position: {position}\n')
def view_staff():
    with open('staff_info.txt', 'r') as file:
        file.seek(0)
        for line in file:
            print(line)
def search_staff():
    username = input('Enter the ID you want to search:\n ')
    with open('staff_info.txt', 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            if parts[0].split(':')[1].strip() == username:
                print(f"ID: {parts[0].split(':')[1].strip()}, Name: {parts[1].split(':')[1].strip()}, Gender: {parts[2].split(':')[1].strip()}, Salary: {parts[3].split(':')[1].strip()}, Position: {parts[4].split(':')[1].strip()}")
                return
    print("Staff not found.")
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
        for line in lines:
            if line.startswith(f'ID: {edit_username}'):
                parts = line.strip().split(',')
                print(f"Current details: {line.strip()}")
                new_name = input('Enter new name: ')
                gender = input('Enter new gender (male/female): ')
                salary = input('Enter new salary: ')
                position = input('Enter new position: ')
                file.write(f'ID: {edit_username},Name: {new_name},Gender: {gender},Salary: {salary},Position: {position}\n')
            else:
                file.write(line)

    with open('stafflogin.txt', 'w') as file:
        for line in lines2:
            if line.startswith(f'ID: {edit_username}'):
                parts = line.strip().split(',')
                new_password = input('Enter new password: ')
                encrypted_password = encrypt_password(new_password)
                file.write(f'ID: {edit_username},Password: {encrypted_password}\n')
            else:
                file.write(line)
def remove_staff():
    # read all line in file and save it in lines
    with open('staff_info.txt', 'r') as file:
        lines = file.readlines()
    with open('stafflogin.txt', 'r') as file2:
        lines2 = file2.readlines()

    remove_username = input('Enter the ID you want to remove:\n ')
    new_remove = f"ID: {remove_username}"

    with open('staff_info.txt', 'w') as file:
        file.seek(0)
        for line in lines:
            lines = line.strip()
            if not line.startswith(new_remove):
                file.write(line)

    with open('stafflogin.txt', 'w') as file:
        file.seek(0)
        for line in lines2:
            lines = line.strip()
            if not line.startswith(new_remove):
                file.write(line)
    # # read all line in file and save it in lines
    # with open('staff_info.txt', 'r') as file:
    #     lines = file.readlines()
    # with open('stafflogin.txt', 'r') as file2:
    #     lines2 = file2.readlines()
    #
    # remove_username = input('Enter the ID you want to remove:\n ')
    #
    # with open('staff_info.txt', 'w') as file:
    #
    #     for line in lines:
    #         lines = line.strip()
    #         if not line.startswith(remove_username):
    #             file.write(line)
    #
    # with open('stafflogin.txt', 'w') as file:
    #
    #     for line in lines2:
    #         lines = line.strip()
    #         if not line.startswith(remove_username):
    #             file.write(line)
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
    # Open the 'member_info.txt' file in read mode.
    with open('member_info.txt', 'r') as file:
        username = input('Enter the ID you want to search:\n ')
        for line in file:
            # Split the line into components based on commas
            parts = line.strip().split(',')

            # Check if the first component (ID) matches the user input
            if parts[0].split(':')[1].strip() == username:
                print(
                    f"ID: {parts[0].split(':')[1].strip()}, Name: {parts[1].split(':')[1].strip()}, Gender: {parts[2].split(':')[1].strip()}")
                return

    # If no match is found, print "Member not found."
    print("Member not found.")
def edit_member():
    # Read all lines from the file
    with open('member_info.txt', 'r') as file:
        lines = file.readlines()
    with open('memberlogin.txt', 'r') as file:
        lines2 = file.readlines()
 
    # Get the username to edit
    edit_username = input('Enter the ID you want to edit:\n ')
    new_username2 = f"ID: {edit_username}"
 
    # Open the file in write mode to update it
    with open('member_info.txt', 'w') as file:
        for line in lines:
            if line.startswith(new_username2):
                lines = line.strip()
                SU, SN, SG = lines.split(',')
                print(f"Current details:{SU},{SN},{SG}")
                new_password = input('Enter new password: ')
                encrypted_password = encrypt_password(new_password)
                name = input('Enter new name: ')
                gender = input('Enter new gender (male/female): ')
                file.write(f'ID: {edit_username},Name: {name},Gender: {gender}\n')
            else:
                file.write(line)
 
    with open('memberlogin.txt', 'w') as file:
        file.seek(0)
        for line in lines2:
            if line.startswith(edit_username):
                file.write(f'ID: {edit_username},Password: {encrypted_password}\n')
            else:
                file.write(line)
def delete_member():
    # read all line in file and save it in lines
    with open('member_info.txt', 'r') as file:
        lines = file.readlines()
    with open('memberlogin.txt', 'r') as file2:
        lines2 = file2.readlines()

    remove_username = input('Enter the ID you want to remove:\n ')
    new_remove = f"ID: {remove_username}"

    with open('member_info.txt', 'w') as file:
        file.seek(0)
        for line in lines:
            lines = line.strip()
            if not line.startswith(new_remove):
                file.write(line)

    with open('memberlogin.txt', 'w') as file:
        file.seek(0)
        for line in lines2:
            lines = line.strip()
            if not line.startswith(new_remove):
                file.write(line)
    # with open('member_info.txt', 'r') as file:
    #     lines = file.readlines()
    # with open('memberlogin.txt', 'r') as file2:
    #     lines2 = file2.readlines()
    #
    # remove_username = input('Enter the ID you want to remove:\n ')
    #
    # with open('member_info.txt', 'w') as file:
    #
    #     for line in lines:
    #         lines = line.strip()
    #         if not line.startswith(remove_username):
    #             file.write(line)
    #
    # with open('memberlogin.txt', 'w') as file2:
    #     for line in lines2:
    #         file2line = line.strip()
    #         if not remove_username.startswith(remove_username):
    #             file2.write(line)
def AddBook():
    print("Insert Book details Below: ")
    print("------------------------------")
    name_book = input('Insert Name: ')
    ISBN = input('INSERT ISBN: ')  #
    author = input('Insert Author/s ')
    genre = input('Genre: ')
    publishDate = input('Date Published: ')
    current_date_time = datetime.datetime.now()
    addDate = current_date_time.strftime("%Y-%m-%d")  # formating date as string because of old bugs
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
    print("Would you like to add another book?")
    choice = input('Y/N: ')
    if choice == 'Y':
        AddBook()
    else:
        print("Returning to main menu.")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        librarian_menu()
def view_Allbooks():
    # Show all books and their details
    with open('Book_catalogue.txt', 'r') as file:
        for line in file:
            print(line)
    print("Press enter to return to the main menu.")
    input()
    print("Returning to main menu.")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    librarian_menu()
def search_book():
    #Seacrch only uses ISBN. for exact seacrches. shows full book details
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
        print("Would you like to search for another book?")
        choice = input('Y/N: ')
        if choice == 'Y':
            search_book()
        else:
            print("Returning to main menu.")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            librarian_menu()
def loan_book():
    print("Insert ISBN of the book to be loaned: ")
    isbn = input(" ")
    print("Member ID of loaner: ")
    loaner = input(" ")
    print("Date Loaned (YYYY/MM/DD): ")
    dateloaned = input("")
    loanID = "LID" + dateloaned + loaner + isbn

    # Check if the member has already loaned 5 books that are not returned
    loan_count = 0
    with open('loan_logs.txt', 'r') as loan_file:
        for line in loan_file:
            if f"Member ID: {loaner}" in line:
                loan_count += 1

    with open('return_logs.txt', 'r') as return_file:
        for line in return_file:
            if f"Member ID: {loaner}" in line:
                loan_count -= 1

    if loan_count >= 5:
        print("This member has already loaned 5 books and cannot loan another.")
        return

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

    print("Would you like to return to the main menu?")
    choice = input('Y/N: ')
    if choice == 'Y':
        print("Returning to main menu.")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        librarian_menu()
    else:
        loan_book()
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

    # Calculate late fees
    with open('loan_logs.txt', 'r') as loan_file:
        for line in loan_file:
            if f"Member ID: {returner}" in line and f"ISBN: {isbn}" in line:
                loan_date_str = line.split("Date Loaned: ")[1].split(",")[0]
                loan_date = datetime.datetime.strptime(loan_date_str.strip(), "%Y/%m/%d").date()
                return_date = datetime.datetime.strptime(datereturned.strip(), "%Y/%m/%d").date()
                days_late = (return_date - loan_date).days - 14
                if days_late > 0:
                    fee_amount = min(10, 2 + (days_late - 1))  # Example fee calculation
                    log_fee(returner, isbn, fee_amount, datereturned)
                    print(f"Late fee of {fee_amount} RM has been logged for Member ID: {returner}")

    print("Would you like to return to the main menu?")
    choice = input('Y/N: ')
    if choice == 'Y':
        print("Returning to main menu.")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        librarian_menu()
    else:
        return_book()
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
    print("Would you like to return to the main menu?")
    choice = input('Y/N: ')
    if choice == 'Y':
        print("Returning to main menu.")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        librarian_menu()
    else:
        edit_catalogue()
def view_logs():
    print("Loan Logs:")
    with open('loan_logs.txt', 'r') as file:
        for line in file:
            print(line.strip())

    print("\nReturn Logs:")
    with open('return_logs.txt', 'r') as file:
        for line in file:
            print(line.strip())

    print("Press Enter to return to the main menu.")
    input()
    print("Returning to main menu.")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    librarian_menu()
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
        print("Press Enter to return to the main menu.")
        input()
        print("Returning to main menu.")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        librarian_menu()

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
                print("Press Enter to return to the main menu.")
                input()
                print("Returning to main menu.")
                time.sleep(1)
                print(".")
                time.sleep(1)
                print(".")
                time.sleep(1)
                print(".")
                librarian_menu()
            else:
                print("No late fee.")
            print(f"Date Returned: {return_date_str}")
            print("Press Enter to return to the main menu.")
            input()
            print("Returning to main menu.")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            librarian_menu()
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
                print("Press Enter to return to the main menu.")
                input()
                print("Returning to main menu.")
                time.sleep(1)
                print(".")
                time.sleep(1)
                print(".")
                time.sleep(1)
                print(".")
                librarian_menu()
    else:
        print("No recent loans found.")
        print("Press Enter to return to the main menu.")
        input()
        print("Returning to main menu.")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        librarian_menu()
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
def log_fee(member_id, isbn, fee_amount, date_incurred):
    with open('fees.txt', 'a') as fee_file:
        fee_file.write(f"Member ID: {member_id}, ISBN: {isbn}, Fee Amount: {fee_amount}, Date Incurred: {date_incurred}\n")
def bookviewer_m(member_id):
    borrowed_books = []
    returned_books = []

    # Read the loan logs to find books borrowed by a member
    with open('loan_logs.txt', 'r') as loan_file:
        for line in loan_file:
            if f"Member ID: {member_id}" in line:
                parts = line.strip().split(',')
                loaned_bookisbn = parts[1].split(':')[1].strip()
                date_loaned = parts[3].split(':')[1].strip()
                due_date = (datetime.datetime.strptime(date_loaned, "%Y/%m/%d") + datetime.timedelta(days=14)).strftime("%Y/%m/%d")
                borrowed_books.append((loaned_bookisbn, due_date))

    # Read the return logs to find books returned by the member
    with open('return_logs.txt', 'r') as return_file:
        for line in return_file:
            if f"Member ID: {member_id}" in line:
                parts = line.strip().split(',')
                returned_bookisbn = parts[1].split(':')[1].strip()
                returned_books.append(returned_bookisbn)

    # Filter out returned books from borrowed books
    currently_borrowed_books = [(isbn, due_date) for isbn, due_date in borrowed_books if isbn not in returned_books]

    borrowed_books_details = []
    with open('Book_catalogue.txt', 'r') as book_file:
        for line in book_file:
            book = eval(line.strip())
            for isbn, due_date in currently_borrowed_books:
                if book['ISBN'] == isbn and book['Available'] == 'No':
                    borrowed_books_details.append((book['Book Name'], due_date))

    if borrowed_books_details:
        print('Books currently in your inventory:')
        for book_title, due_date in borrowed_books_details:
            print(f"Title: {book_title}, Due Date: {due_date}")
    else:
        print('No books currently in your inventory.')
def booksearch_m(member_id):
    print('''
    ==========================
    || Search catalogue by: ||
    ||                      ||
    || 1. Title             ||
    || 2. Genre             ||
    || 3. Author            ||
    || 4. ISBN              ||
    || 5. Back              ||
    ||                      ||
    ==========================''')
 #ascii art makes everything look nicer
    choice = int(input('Enter your choice: '))

    if choice == 1:
        search_term = input("Enter the title of the book you're looking for: ").strip().lower()
    elif choice == 2:
        search_term = input("Enter the genre of the book you're looking for: ").strip().lower()
    elif choice == 3:
        search_term = input("Enter the author of the book you're looking for: ").strip().lower()
    elif choice == 4:
        search_term = input("Enter the ISBN of the book you're looking for: ").strip().lower()
    elif choice == 5:
        member_menu(member_id)
        return
    else:
        print("Invalid choice. Please try again.")
        booksearch_m(member_id)
        return

    with open('Book_catalogue.txt', 'r') as file:
        found = False
        for line in file:
            book = eval(line.strip())
            if choice == 1 and search_term in book['Book Name'].strip().lower():
                print(book)
                found = True
                print("Would you like to search for another book?")
                choice2 = input('Y/N: ').strip().upper()
                if choice2 == 'Y':
                    booksearch_m(member_id)
                else:
                    member_menu(member_id)
                    print("Returning to main menu.")
                    time.sleep(1)
                    print(".")
                    time.sleep(1)
                    print(".")
                    time.sleep(1)
                    print(".")
                    member_menu(member_id)

            elif choice == 2 and search_term in book['Genre'].strip().lower():
                print(book)
                found = True
                print("Would you like to search for another book?")
                choice2 = input('Y/N: ').strip().upper()
                if choice2 == 'Y':
                    booksearch_m(member_id)
                else:
                    member_menu(member_id)
                    print("Returning to main menu.")
                    time.sleep(1)
                    print(".")
                    time.sleep(1)
                    print(".")
                    time.sleep(1)
                    print(".")
                    member_menu(member_id)

            elif choice == 3 and search_term in book['Author'].strip().lower():
                print(book)
                found = True
                print("Would you like to search for another book?")
                choice2 = input('Y/N: ').strip().upper()
                if choice2 == 'Y':
                    booksearch_m(member_id)
                else:
                    member_menu(member_id)
                    print("Returning to main menu.")
                    time.sleep(1)
                    print(".")
                    time.sleep(1)
                    print(".")
                    time.sleep(1)
                    print(".")
                    member_menu(member_id)

            elif choice == 4 and search_term in book['ISBN'].strip().lower():
                print(book)
                found = True
                print("Would you like to search for another book?")
                choice2 = input('Y/N: ').strip().upper()
                if choice2 == 'Y':
                    booksearch_m(member_id)
                else:
                    print("Returning to main menu.")
                    time.sleep(1)
                    print(".")
                    time.sleep(1)
                    print(".")
                    time.sleep(1)
                    print(".")
                    member_menu(member_id)

    if not found:
        print("No matching books found. Would you like to try again?")
        choice3 = input('Y/N: ').strip().upper()
        if choice3 == 'Y':
            booksearch_m(member_id)
        else:
            print("Returning to main menu.")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
            print(".")
            member_menu(member_id)
def viewfees_m(member_id):
    total_fees = 0
    loans = []

    def calculate_fee(days_late):
        if days_late == 1:
            return 2
        elif days_late == 2:
            return 3
        elif days_late == 3:
            return 4
        elif days_late == 4:
            return 5
        elif days_late == 5:
            return 6
        else:
            return 10

    with open('loan_logs.txt', 'r') as loan_file:
        for line in loan_file:
            if f"Member ID: {member_id}" in line:
                loans.append(line.strip())

    if not loans:
        print("No loans found for this user.")
        return

    for loan in loans:
        try:
            loan_date_str = loan.split("Date Loaned: ")[1].split(",")[0]
            loan_date = datetime.datetime.strptime(loan_date_str.strip(), "%Y/%m/%d").date()
        except (IndexError, ValueError):
            print(f"Error processing loan entry: {loan}")
            continue

        current_date = datetime.datetime.now().date()
        days_since_book_borrowed = (current_date - loan_date).days

        with open('return_logs.txt', 'r') as return_file:
            returned = False
            returned_date_str = None
            for return_line in return_file:
                if f"Member ID: {member_id}" in return_line and "Date Returned" in return_line:
                    returned_date_str = return_line.split("Date Returned: ")[1].split(",")[0]
                    returned = True
                    break

        if returned:
            return_date = datetime.datetime.strptime(returned_date_str.strip(), "%Y/%m/%d").date()
            days_late = (return_date - loan_date).days - 14
            if days_late > 0:
                total_fees += calculate_fee(days_late)
        else:
            days_left = 14 - days_since_book_borrowed
            if days_left < 0:
                days_late = abs(days_left)
                total_fees += calculate_fee(days_late)

    print(f"Total fees: {total_fees} RM")
    print("Press Enter to return to the main menu.")
    input()
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".") #using sleep and dots to make code look cooler
    member_menu(member_id)
def update_info(member_id):
    print('''
    ==========================
    || Update Info:         ||
    ||                      ||
    || 1. Change Password   ||
    || 2. Change Name       ||
    || 3. Back              ||
    ||                      ||
    ==========================''')
    choice = int(input('Enter your choice: '))

    if choice == 1:
        new_password = input('Enter new password: ')
        encrypted_password = encrypt_password(new_password)

        with open('memberlogin.txt', 'r') as file:
            lines = file.readlines()

        with open('memberlogin.txt', 'w') as file:
            for line in lines:
                if line.startswith(f'ID: {member_id}'):
                    file.write(f'ID: {member_id},Password: {encrypted_password}\n')
                else:
                    file.write(line)
        print('Password updated successfully.')

    elif choice == 2:
        new_name = input('Enter new name: ')

        with open('member_info.txt', 'r') as file:
            lines = file.readlines()

        with open('member_info.txt', 'w') as file:
            for line in lines:
                if line.startswith(f'ID: {member_id}'):
                    parts = line.strip().split(',')
                    file.write(
                        f'ID: {parts[0].split(":")[1].strip()},Name: {new_name},Gender: {parts[2].split(":")[1].strip()}\n')
                else:
                    file.write(line)
        print('Name updated successfully.')

    elif choice == 3:
        print('Returning to main menu.')
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".") #using sleep and dots to make code look cooler
        member_menu(member_id)
        return

    else:
        print('Invalid choice. Please try again.')
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".") #using sleep and dots to make code look cooler
        update_info(member_id)


#MENUS BELOW
def superadminmenu():
    print('''
    =====================================
    ||  Welcome to the Admin System    ||
    =====================================
    ||                                 ||
    ||  1. Add Admin                   ||
    ||  2. View Admins                 ||
    ||  3. logout                      ||
    ||                                 ||
    ===================================== 
    ''')
    choice = int(input('Enter your choice: '))
    if choice == 1:
        add_admin()
    elif choice == 2:
        view_admin()
    elif choice == 3:
        login()
        return
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
    elif LBSchoice == 6:
        ADMmenu()
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
    elif LBMchoice == 6:
        ADMmenu()
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
def member_menu(member_id):
    print('''
    ================================================================
    ||  Welcome to the Brickfields Kuala Lumpur Community Library.||
    ==============================================================||
    ||                                                            ||
    ||  1. View Books borrowed                                    || 
    ||  2. Search for Books                                       ||
    ||  3. View fee's                                             ||
    ||  4. Update Info                                            ||
    ||  5. Logout                                                 ||
    ||                                                            ||
    ================================================================
    ''')
    choice = int(input('Enter your choice: '))
    if choice == 1:
        bookviewer_m(member_id)
        # borrowed_books = bookviewer_m(member_id)
        # if borrowed_books:
        #     print('Books currently in your inventory: ')
        #     for book_title in borrowed_books:
        #         print(book_title)
        # else:
        #     print('No books currently in your inventory.')
    elif choice == 2:
        booksearch_m(member_id)
    elif choice == 3:
        viewfees_m(member_id)
    elif choice == 4:
        update_info(member_id)
    elif choice == 5:
        login()
        return
    else:
        print('Invalid choice, please try again.')
        member_menu(member_id)
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
            superadminmenu()
            for i in range(20):
                repeat = input('Would you like to add another admin?(Y/N): ')
                repeat = repeat.upper()
                if repeat == 'Y':
                    superadminmenu()
                else:
                    login()
        elif username.startswith('ADM'):
            print(f'You are logged in as {username}, enter your selection:')
            ADMmenu()
            for i in range(20):
                repeat = input('Return to admin menu?(Y/N): ')
                repeat = repeat.upper()
                if repeat == 'Y':
                    ADMmenu()
                else:
                    login()
    elif check_credentials('memberlogin.txt', username, encrypted_password):
        if username.startswith('M'):
            name = get_name('member_info.txt', username)
            print(f'You are logged in as {name}')
            member_menu(username)
            for i in range(20):
                repeat = input('Return to member menu?(Y/N): ')
                repeat = repeat.upper()
                if repeat == 'Y':
                    member_menu(username)
                    pass
                else:
                    login()
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
                    login()
    else:
        print('Incorrect username or password')
        login()

start_superadmin()
login()


