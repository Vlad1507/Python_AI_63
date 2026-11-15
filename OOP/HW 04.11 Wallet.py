#task 1
# class Wallet:
#     def __init__(self,owner,balance):
#         if balance < 0:
#             raise ValueError("Баланс не може бути від'ємним")
#         self.owner = owner
#         self.__balance = balance
#     def add_money(self,amount):
#         if amount > 0:
#             self.__balance += amount
#         else:
#             raise ValueError("Не можна поповнювати гаманець на нульову або від'ємну суму")
#     def spend_money(self,amount):
#         if amount > 0 and amount <= self.__balance:
#             self.__balance -= amount
#         else:
#             raise ValueError("Неправильна сума списання")
#     @property
#     def balance(self):
#         return self.__balance
#     def show_info(self):
#         print(f"Власник: {self.owner}\nБаланс: {self.balance}")
# wallet = Wallet("Олександр", 1000)
#
# wallet.add_money(500)
# wallet.spend_money(300)
# wallet.spend_money(2000)
#
# wallet.show_info()
# task 2


