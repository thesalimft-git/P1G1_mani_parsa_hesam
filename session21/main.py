from bank_system import BankSystem
from services import show_menu
from data_manager import DataManager

dm = DataManager()
accounts = dm.get()

def main():
    bs = BankSystem(accounts)
    while True:
        show_menu()
        command = input('select from menu: ')
        
        match command:
            case '1':
                bs.show_all_info()
                
            case '2':
                pass
            
            case '3':
                name = input('name: ')
                balance = input('balance: ')
                bs.create_account(name, balance)
                
            case '4':
                bs.show_all_info(show_history = False)
                id = input('id: ')
                amount = input('amount: ')
                result = bs.deposit(id, amount)
                print(result)
                
            case '5':
                bs.show_all_info(show_history = False)
                id = input('id: ')
                amount = input('amount: ')
                result = bs.withdraw(id, amount)
                print(result)
                
            case '6':
                bs.show_all_info(show_history = False)
                id_from = input('id from: ')
                id_to = input('id to: ')
                amount = input('amount: ')
                result = bs.transfer(id_from, id_to, amount)
                print(result)
            
            case '7':
                dm.set(accounts)
                print('good bye')
                break
        
        
    
    

main()



