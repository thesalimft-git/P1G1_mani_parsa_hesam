from bank_system import BankSystem

accounts = dict()

def main():
    bs = BankSystem(accounts)
    
    bs.create_account('ali', 100)
    bs.create_account('reza', 200)
    print(accounts)
    
    bs.deposit('1', 50)
    print(accounts)
    
    bs.withdraw('2', 20)
    print(accounts)




main()



