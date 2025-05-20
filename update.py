import environment

def collect_info(name, email, phone):
    name = input("Type the name contact: ")
    email = input("Type the email contact: ")
    phone = input("Type the phone: ")

    string_contact = f"Name: {name} Email: {email} Phone: {phone}\n"

    return string_contact

def update_contact(finder):

    with open(environment.DATABASE_NAME, "r+") as file:
        old = file.read()

    file.write(collect_info() + old)
