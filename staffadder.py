import json
staffname = input("Insert Staff Name: ")
staffId = input("Insert Staff ID: ")
staffemail = input("Insert Staff Email: ")
staffPass = input("Insert new password: ")
hasAdmins = input("Has admin permissions? (Yes/No): ")

# Initialize Admin as "False" by default
Admin = "False"

if hasAdmins.lower() == "yes":
    Admin = "True"

# function to add to JSON
def write_json(new_data, filename='Library staff.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["staff_details"].append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)

    # python object to be appended
signin = {"staff_name":staffname,
     "staffId": staffId,
     "staff_email": staffemail,
     "staffPass":staffPass,
     "hasAdminperms":Admin
    }
    
write_json(signin) 