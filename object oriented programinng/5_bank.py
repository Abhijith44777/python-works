# acno,balance,actype,customername


class Bank:
    acno:int

    balance:int

    ac_type:str

    customer_name:str

    def __init__(self,acno,balance,ac_type,customer_name):

        self.acno=acno

        self.balance=balance

        self.ac_type=ac_type

        self.customer_name=customer_name

    def deposit(self,amount):
        self.balance+=amount
        print(f"your account{self.acno}has been credited with amount {amount} avl balance{self.balance}")


    def withdraw(self,amount):
        if self.balance<amount:
            print("insafficant balance")
        else:
                
            self.balance-=amount
            print(f"your account{self.acno}has been debited with amount{amount} avl balance{self.balance}")

    def get_balance(self):
        print("your avl balance",self.balance)    

bank_instance=Bank(9447778926,8000,"international","ABHIJITH VR")
bank_instance.deposit(5000)
bank_instance.withdraw(7000)
bank_instance.get_balance()