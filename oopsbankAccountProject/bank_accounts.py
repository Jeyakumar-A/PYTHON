class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self,initial_Amount,acct_name):
        self.balance = initial_Amount
        self.name = acct_name
        print(f"\nAccount '{self.name}'created.\nBalance = ${self.balance}")
    
    def get_balance(self):
        print(f"\nAccount '{self.name} balance=${self.balance:.2f}")
    
    def deposite(self,amount):
        self.balance=self.balance+amount
        print("\n Deposite complete")
        self.get_balance()

    def viable_transaction(self,amount):
        if self.balance>=amount:
            return
        else:
            raise BalanceException(f"sorry ,account '{self.name}' only has a balance of ${self.balance:.2f}")
    
    def withdraw(self,amount):
        try:
            self.viable_transaction(amount)
            self.balance=self.balance-amount
            print("\nwithdraw complete")
            self.get_balance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')
    
    def transfer(self,amount,account):
        try:
            print('\n*********************\n\nBegining Transfer...')
            self.viable_transaction(amount)
            self.withdraw(amount)
            account.deposite(amount)
            print('\nTransfer complete!\n\n*****')
        
        except BalanceException as error:
            print(f"transfer interrupted.{error}")

class InterestRewardAcct(BankAccount):
    def deposit(self,amount):
        self.balance=self.balance+(amount*1.05)
        print("\nDeposite complete")
        self.get_balance()

class SavingsAcct(InterestRewardAcct):
    def __init__(self, initial_Amount, acct_name):
        super().__init__(initial_Amount, acct_name)
        self.fee = 5

    def withdraw(self,amount):
        try:
            self.viable_transaction(amount+self.fee)
            self.balance=self.balance-(amount+self.fee)
            print("withdraw complete")
            self.get_balance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")

