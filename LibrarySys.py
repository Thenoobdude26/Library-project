import datetime
import time
#Work in progress
def AddBook():
    print("Insert Book details Below: ")
    print("------------------------------")
    name_book = input('Insert Name: ')
    ISBN = input('INSERT ISBN: ')  # 
    author = input('Insert Author/s ')
    genre = input('Genre: ')
    publishDate = input('Date Published: ')
    current_date_time = datetime.datetime.now()
    addDate = current_date_time.date()#date added to catalogue
    Available = "Yes"


    new_book = {
        'Book Name': name_book, 
        'ISBN': ISBN, 
        'Author': author,
        'Genre': genre, 
        'Date Published':publishDate, 
        'Date Added': addDate,
        'Available':Available
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
    loanID = "LID"+dateloaned+loaner+isbn

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
    returnID = "LID"+datereturned+returner+isbn

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
        print("|| 10. Exit                        ||")
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
            break
        else:
            print("Invalid choice. Please try again.")

        time.sleep(2)




librarian_menu()
