class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner                
        self.__balance = balance  

    def deposit(self, amount):
        self.__log_transaction("deposit", amount)
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Недостатъчна сума!")
            return

        self.__log_transaction("withdraw", amount)
        self.__balance -= amount

    def get_balance(self):
        return self.__balance

    def __log_transaction(self, type, amount):
        print(f"[Скрит лог] {type}: {amount} лв.")


acc = BankAccount("Simeon", 500)
acc.deposit(200)
acc.withdraw(100)
print("Текущ баланс:", acc.get_balance())
