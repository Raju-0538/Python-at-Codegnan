from data import Users

def login(account:int,password:str):
    if account in Users:
        if password == Users[account]['password']:
            return True
        print("Invalid password")
        return False
    print("Account not found !")
    return False