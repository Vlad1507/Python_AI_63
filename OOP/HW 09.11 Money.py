class Money:
    def __init__(self,dollar,cents):
        self.dollar = dollar
        self.cents = cents
    def display(self):
        print(f"{self.dollar} dollars {self.cents} cents")
    def new_dollars(self,new_dollar):
        self.dollar = new_dollar
    def new_cent(self, new_cents):
        self.cents = new_cents

class Product(Money):
    def __init__(self,dollar,cents,name):
        super().__init__(dollar, cents)
        self.name = name
    def discount(self,discount_dollar, discount_cent):
        self.discount_dollar = discount_dollar
        self.discount_cents = discount_cent
        self.total_price = self.dollar * 100 + self.cents
        self.total_discount = discount_dollar * 100 + discount_cent
        if self.total_discount > self.total_price:
            raise ValueError("Помилка! Знижка перевищує ціну товару")
        else:
            remaining = self.total_price - self.total_discount
            self.dollar = remaining // 100
            self.cents = remaining % 100


product = Product(100, 50, "Laptop")
product.display()
product.discount(20, 75)
product.display()
print("===============")
product.discount(200, 50)
product.display()









