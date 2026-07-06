from data import admin

def admin_login(account:str,password:str):
    if account in admin:
        if password == admin[account]['password']:
            return True
        print("Invalid password")
        return False
    print("Account not found !")
    return False