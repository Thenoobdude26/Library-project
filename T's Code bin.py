import datetime
# #super admin username: SDM001 and password: SDMpassword
# # Log in as super admin first to create an admin account
# #step 1: log in as super admin (admin account that existed after running the program)
# #step 2: add a new admin account for new employees (Make sure the username start with ADM) ex. ADM002 ADM001 
# #step 3: log in as the admin account you created
# #step 4: you are now able to unlock admin perms
# #Only Super Admin can add staff, because yes



# def Addstaff():
#     dik = {"STAFF": []}
#     name_staff = input('Insert Name: ')
#     id_staff = input('Insert ID: (ADM-ADMIN, LB-librarian)')#ADM001/LB0001
#     email_staff = input('Insert Email: ')
#     password_staff = input('Insert: ')
#     AdminPerms = input('Has Admins: ')#Librerians don't have admin status
#     new_staff = {'Name': name_staff, 'ID': id_staff, 'Email': email_staff, 'HasPerms': AdminPerms}
#     encryption = password_staff.encode("utf-8").hex()
#     passwords = {'Password': encryption}  # adding password encryption
#     dik["STAFF"].append(new_staff)
#     dik["STAFF"].append(passwords)#Password stored in hex
#     with open('staff_list.txt', "a") as t:
#         t.write(str(dik) + '\n')
#     print(f'Added: {name_staff}')

# def Addmember():
#     dic = {"MEMBER": []}
#     name_member = input('Insert Name: ')
#     id_member = input('Insert ID: (M###)')#M001
#     email_member = input('Insert Email: ')
#     password_member = input('Insert: ')
#     new_member = {'Name': name_member, 'ID': id_member, 'Email': email_member}
#     encryption = password_member.encode("utf-8").hex()
#     passwords = {'Password': encryption}  # adding password encryption
#     dic["MEMBER"].append(new_member)
#     dic["MEMBER"].append(passwords)#Password stored in hex
#     with open('member_list.txt', "a") as t:
#         t.write(str(dic) + '\n')
#     print(f'Added: {name_member}')
    
# # Addmember()
# # Addstaff()

# #     dik["FoodItem"].append(newfood)  # Append the food dictionary to 'FoodItem' list
# #     with open('food.txt', "a") as t:  # Use 'with' to handle file opening and closing
# #         t.write(str(dik) + '\n')
# #     print(f'Added: {food_name}')


# # signin = {"staff_name":staffname,
# #      "staffId": staffId,
# #      "staff_email": staffemail,
# #      "staffPass":staffPass,
# #      "hasAdminperms":Admin
# #     }

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
# AddBook()
return_book()