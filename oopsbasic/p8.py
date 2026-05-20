class Laptop:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def discont(self,discount):
        a = self.price*discount/100
        b = self.price-a
        print(f"The discount of ruppes {a}")
        print(f"The discounted price is {b}")
    
l = Laptop("LOQ",60000)
print(f"The laptop name is {l.name}")
print(f"The Original price is {l.price}")
l.discont(10)
