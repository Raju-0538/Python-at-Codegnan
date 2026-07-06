from data import users

def transfer(sender:int,receiver:int,transfer_amount:int):
    if receiver in users:
        if transfer_amount <= users[sender]['balance']:
            users[sender]['balance'] = users[sender]['balance']-transfer_amount
            users[receiver]['balance'] = users[receiver]['balance']+transfer_amount
            return f"Transfer is Successfull ! Current Balance : {users[sender]['balance']}"
        else:
            return "insufficient balance to transfer"
    return "Receiver not found"