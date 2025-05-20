import environment

def collect_info(name, email, phone):
    name = input("Type the name contact: ")
    email = input("Type the email contact: ")
    phone = input("Type the phone: ")

    string_contact = f"Name: {name} Email: {email} Phone: {phone}\n"

    return string_contact
