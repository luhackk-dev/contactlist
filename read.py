import environment

def read_contact(finder: str):
    
    with open(environment.DATABASE_NAME, "r") as file:
        for line in file:
            if finder in line:
                return line