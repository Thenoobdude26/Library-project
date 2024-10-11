staffname = input("Insert Staff Name: ")
staffId = input("Insert Staff ID: ")
staffemail = input("Insert Staff Email: ")
staffPass = input("Insert new password: ")
hasAdmins = input("Has admin permissions? (Yes/No): ")

# Initialize Admin as "False" by default
Admin = "False"

if hasAdmins.lower() == "yes":
    Admin = "True"


    # python object to be appended
signin = {"staff_name":staffname,
     "staffId": staffId,
     "staff_email": staffemail,
     "staffPass":staffPass,
     "hasAdminperms":Admin
    }