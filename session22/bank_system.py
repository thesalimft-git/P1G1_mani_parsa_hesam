from datetime import datetime;

class BankSystem:
    def __init__(self, accounts):
        self.accounts = accounts
    
    def show_all_info(self, show_history = True):
        if not self.accounts:
            print('account is empty')
            return
            
        for id, info in self.accounts.items():
            print(f"{id}- {info.get('name')} ({info.get('balance')})")
            
            if show_history:
                for item in info.get('history'):
                    print('\t-', item)
         
    def show_one_account(self, id:str):
        # validation
        if not self.accounts:
            print('account is empty')
            return
        
        if id not in self.accounts:
            print('error: id does not exist')
            return
        
        histories = self.accounts[id]['history']
        for history in histories:
            print('\t-', history)
            
    def create_account(self, name:str, balance:str|float|int):
        try:
            balance = float(balance)
        except:
            return 'error: balance must be a number'
        
        # TODO: error handling for name
        id = len(self.accounts) + 1
        current_time = datetime.now().strftime('%d %b %Y at %H:%M')
        self.accounts[str(id)] = {
            'name': name,
            'balance': balance,
            'history': [f'Created on {current_time} with balance = ${balance}']
        }
        return True

    def deposit(self, id:str, amount:float|str|int) -> str:
        try:
            amount = float(amount)
        except:
            return 'error: amount must be a number'
       
        if id not in self.accounts:
            return 'error: just present id'
        
        self.accounts[id]['balance'] += amount   
        
        current_time = datetime.now().strftime('%d %b %Y at %H:%M')
        txt = f'Deposit on {current_time} with balance = ${self.accounts[id]['balance']}'
        self.accounts[id]['history'].append(txt)
        
        return 'deposit successfully'
        
    def withdraw(self, id:str, amount:str|float|int) -> str:
        try:
            amount = float(amount)
        except:
            return 'error: amount must be a number'
        
        if id not in self.accounts:
            return 'error: id is not valid'
        
        if self.accounts[id]['balance'] < amount:
            return 'error: balance is not enough'

        self.accounts[id]['balance'] -= amount
        current_time = datetime.now().strftime('%d %b %Y at %H:%M')
        txt = f'Withdraw on {current_time} with balance = ${self.accounts[id]['balance']}'
        self.accounts[id]['history'].append(txt)
        
        return 'withdraw successfully'
        
    def transfer(self, id_from:str, id_to:str, amount:str|float|int) -> str:
        # write full code
        result = ''
        result = self.withdraw(id_from, amount)
        if 'error' in result:
            return result
        
        result = self.deposit(id_to, amount)
        if 'error' in result:
            return result
        
        return 'transfer successfully'
        
       
 
  
       
       
        
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