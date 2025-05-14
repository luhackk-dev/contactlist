import enviroment

def create_contact(name: str, email: str, phone: str):

    with open(enviroment.DATABASE_NAME, "a") as file:

        line = f"Name: {name} Email: {email} Phone: {phone}\n"
        
        file.write(line)
        