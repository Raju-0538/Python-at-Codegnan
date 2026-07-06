from data import users

def login(account:int,password:str):
    if account in users:
        if password == users[account]['password']:
            return True
        return False
    return False