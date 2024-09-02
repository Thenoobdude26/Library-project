def gobackmenu():
    goback = input('go back to main menu?(Y/N): ')
    goback = goback.upper()
    return goback

def main_menu():
    print('1. admin')
    print('2. member')
    choice = int(input('enter your role:'))

    if choice == 1:
        admin()
    elif choice == 2:
        member()
    else:
        exit()

    if gobackmenu() == 'Y':
        main_menu()
    else:
        exit()
    
    

def admin():
    username = input("username: ")
    password = input('password: ')

    with open("login.txt", 'a+') as file:
        
        file.write(f'{username},{password}\n')
        

def member():
    with open('login.txt', 'r') as file:
        username = input('username: ')
        password = input('password: ')
        for line in file:
            stored_username, stored_password = line.strip().split(',')
            if (stored_username == username and stored_password == password):
                print('correct')
                break


main_menu()

        