from data import users

def deposit(account:int,amount:int):
    users[account]['balance'] = users[account]['balance']+amount
    return f"Deposit is successfull ! current balance: {users[account]['balance']}"