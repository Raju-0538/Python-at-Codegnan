from data import users

def withdraw(account:int,amount:int):
    curr = users[account]['balance']
    if amount <= curr:
        users[account]['balance'] = curr-amount
        return f"Wihtdraw is successfull ! current balance: {users[account]['balance']}"
    print("Insufficient Funds")