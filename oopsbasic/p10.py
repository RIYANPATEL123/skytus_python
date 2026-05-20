class Shop:
    def __init__(self):
        self.product=[]
    
    def add(self,product):
        self.product.append(product)
    
    def display(self):
        for i in self.product:
            print(i)
        
s = Shop()
s.add("Mineral water")
s.add("Lays")
s.add("sprite")
s.display()
