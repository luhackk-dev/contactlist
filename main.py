import create
import update

option_crud = input("Type the option: ")

CREATE_OPTION = "3"
UPDATE_OPTION = "1"

if option_crud == CREATE_OPTION:
    
    name = input("Type the name contact: ")
    email = input("Type the email contact: ")
    phone = input("Type the phone: ")

    create.create_contact(name, email, phone)
    
if option_crud == UPDATE_OPTION:
    finder = input("Type Email or Phone to find your contact: ")

    update.update_contact(finder)
