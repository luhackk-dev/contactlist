import environment

def delete_contact(finder: str) -> str:

    with open(environment.DATABASE_NAME, "r") as file:
        
        lines = file.readlines()
        line_position = 0 

        for line in lines:
            if finder in line:
                lines.pop(line_position)
                break
            
            line_position += 1
        
    with open(environment.DATABASE_NAME, "w") as file:
        file.writelines(lines)