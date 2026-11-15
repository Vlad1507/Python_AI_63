class Product:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self,value):
        if value < 0:
            raise ValueError("Ціна не може бути відємною")
        else:
            self._price = value
    @property
    def quantity(self):
        return self._quantity
    @quantity.setter
    def quantity(self,value):
        if value < 0 or not isinstance(value,int):
            raise ValueError("Кількість не може бути від'ємною або не являється цілим числом")
        else:
            self._quantity = value
    def sell(self,amount):
        if amount > 0 and amount <= self.quantity and isinstance(amount,int):
            self.quantity -= amount
        else:
            raise ValueError("Некоректна кількість товару або недостатньо товару на складі")
    def restock(self,amount):
        if amount > 0 and isinstance(amount,int):
            self.quantity += amount
        else:
            raise ValueError("Кількість для поповнення повинна бути додатним цілим числом")
    def total_value(self):
        return self.quantity * self.price

product = Product("Навушники", 1500, 10)

product.sell(3)
product.restock(5)

print(product.quantity)
print(product.total_value())






