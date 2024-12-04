class Bankaccount:
    def __init__(self,customer_name,mpin,account_type,balance):
        self.customer_name=customer_name

        self.__mpin=mpin

        self.account_type=account_type

        self.__balance=balance

    def get_balance(self):
        print(self.__balance)

    def __str__(self):

        return self.customer_name

Bankaccount_instance=Bankaccount("abhi",4777,"savings",500000)
print(Bankaccount_instance.account_type)  

Bankaccount_instance.get_balance()


