import datetime
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
        log_file.write(f"ISBN: {isbn}, Member ID: {loaner}, Date Loaned: {dateloaned}\n")


def return_book():
    print("Insert ISBN of the book to be returned: ")
    isbn = input(" ")
    print("Member ID of returner: ")
    returner = input(" ")
    print("Date Returned (YYYY/MM/DD): ")
    datereturned = input("")

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

    with open('loan_logs.txt', 'a') as log_file:
        log_file.write(f"ISBN: {isbn}, Member ID: {returner}, Date Returned: {datereturned}\n")

def view_loan_logs():
    with open('loan_logs.txt', 'r') as file:
        for line in file:
            print(line)

def search_loan():
    print("Insert ID: ")
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
        loan_date_str = most_recent_loan.split("Date Loaned: ")[1]
        loan_date = datetime.datetime.strptime(loan_date_str, "%Y/%m/%d").date()
        current_date = datetime.datetime.now().date()
        days_since_loan = (current_date - loan_date).days

        # Check if the loan has been returned
        if "Date Returned" not in most_recent_loan:
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
            print("No late fee.")
    else:
        print("No recent loans found.")


