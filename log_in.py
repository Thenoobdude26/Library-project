#super admin username: SDM001 and password: SDMpassword
# Log in as super admin first to create an admin account
#step 1: log in as super admin (admin account that existed after running the program)
#step 2: add a new admin account for new employees (Make sure the username start with ADM) ex. ADM002 ADM001 
#step 3: log in as the admin account you created
#step 4: you are now able to unlock admin perms
#Only Super Admin can add staff, because yes



def Addstaff():
     dik = {"STAFF": []}
     name_staff = input('Insert Name: ')
     id_staff = input('Insert ID: (ADM-ADMIN, LB-librarian)')
     email_staff = input('Insert Email: ')
     password_staff = input('Insert: ')
     AdminPerms = input('Has Admins: ')
     new_staff = {'Name': name_staff, 'ID': id_staff, 'Email': email_staff,'HasPerms': AdminPerms}
     dik["STAFF"].append(new_staff)
     with open('log.txt', "a") as t:  # Use 'with' to handle file opening and closing
         t.write(str(dik) + '\n')
     print(f'Added: {name_staff}')
  


Addstaff()

#     dik["FoodItem"].append(newfood)  # Append the food dictionary to 'FoodItem' list
#     with open('food.txt', "a") as t:  # Use 'with' to handle file opening and closing
#         t.write(str(dik) + '\n')
#     print(f'Added: {food_name}')


# signin = {"staff_name":staffname,
#      "staffId": staffId,
#      "staff_email": staffemail,
#      "staffPass":staffPass,
#      "hasAdminperms":Admin
#     }