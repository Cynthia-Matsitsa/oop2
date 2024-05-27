class Account:
    def _init_(self,number,pin):
        self.number = number
        self.__pin = pin
        self.__balance = 0

        ac1 = Account()
        ac2 = Account()

    def show_balance(self,pin):
        if pin ==self.__pin:
            return self.__balance
        else:
            return "wrong pin"
    
    



