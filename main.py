import create

option_crud = input("Type the option: ")

CREATE_OPTION = "3"

if option_crud == CREATE_OPTION:
    
    name = input("Type the name contact: ")
    email = input("Type the email contact: ")
    phone = input("Type the phone: ")

    create.create_contact(name, email, phone)
    