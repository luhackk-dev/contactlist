print("""   
    Menu
Create [1]
Read   [2]
Update [3]
Delete [4]   
""")

option = input("Type your option: ")
import create

if option == "3":

    name = input("Type the name of your contact:")
    email = input("Type the email of your contact: ")
    phone = input("Type the phone of your contact: ")

    create.create_contact(name, email, phone)
       