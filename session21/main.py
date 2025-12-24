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
                pass
            case '5':
                pass
            case '6':
                pass
            case '7':
                dm.set(accounts)
                print('good bye')
                break
        
        
    
    

main()



