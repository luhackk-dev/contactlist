import environment

def collect_info():
    name = input("Type the new name contact: ")
    email = input("Type the new email contact: ")
    phone = input("Type the new phone: ")

    string_contact = f"Name: {name} Email: {email} Phone: {phone}\n"

    return string_contact

def update_contact(finder: str):

    with open(environment.DATABASE_NAME, "r") as file:
       
        lines = file.readlines()
        line_position = 0

        for line in lines:
            if finder in line:
                lines[line_position] = collect_info()
                break
            
            line_position += 1
            
    
    with open(environment.DATABASE_NAME, "w") as file:
        file.writelines(lines)
