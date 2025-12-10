from datetime import datetime;

class BankSystem:
    def __init__(self, accounts):
        self.accounts = accounts
    
    def create_account(self, name:str, balance:float) -> bool:
        id = len(self.accounts) + 1
        current_time = datetime.now().strftime('%d %b %Y at %H:%M')
        self.accounts[str(id)] = {
            'name': name,
            'balance': balance,
            'history': [f'Created on {current_time} with balance = ${balance}']
        }
        return True

    def deposit(self, id:str, amount:float) -> bool:
        if id not in self.accounts:
            return False
        
        self.accounts[id]['balance'] += amount
        
        
        current_time = datetime.now().strftime('%d %b %Y at %H:%M')
        txt = f'Deposit on {current_time} with balance = ${self.accounts[id]['balance']}'
        self.accounts[id]['history'].append(txt)
        return True
        
    def withdraw(self, id:str, amount:float) -> bool:
        if id not in self.accounts:
            return False
        
        if self.accounts[id]['balance'] < amount:
            return False

        self.accounts[id]['balance'] -= amount
        current_time = datetime.now().strftime('%d %b %Y at %H:%M')
        txt = f'Withdraw on {current_time} with balance = ${self.accounts[id]['balance']}'
        self.accounts[id]['history'].append(txt)
        return True
        
        
       
       
 
  
       
       
        
# account = {
#     '101' : {
#         'name': 'ali',
#         'balance': 100,
#         'history': [
#                     {'type': 'create', 'time': '12-04-2025 13:21', 'amount': 100, 'remaining': 100},
#                     {'type': 'deposit', 'time': '14-04-2025 13:41', 'amount': 20, 'remaining': 120},
#                     {'type': 'withdraw', 'time': '14-04-2025 13:41', 'amount': 10, 'remaining': 110}
#         ]
#     },
# }