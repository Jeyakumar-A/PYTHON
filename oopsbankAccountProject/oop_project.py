from bank_accounts import *

kumar = BankAccount(1000,"Kumar")

suresh=BankAccount(2000,"suresh")

kumar.get_balance()
suresh.get_balance()

kumar.deposite(500)
suresh.deposite(200)

kumar.withdraw(100)

kumar.transfer(100,suresh)

mani = InterestRewardAcct(100,"Mani")
mani.get_balance()
mani.deposit(100)

kani =SavingsAcct(1000,"kani")
kani.get_balance()
kani.withdraw(200)
kani.transfer(100,kumar)