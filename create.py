import enviroment

def create_contact(name: str, email: str, phone: str):

    with open(enviroment.DATABASE_NAME, "w") as file:

        line = f"Name: {name} Email: {email} Phone: {phone}"
        
        file.write(line)
        