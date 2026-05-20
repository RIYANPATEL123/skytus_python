class Flight:
    def __init__(self,total):
        self.total = total
        self.booked = 0

    def booking(self,num):
        if (self.booked<=self.total):
            self.booked +=  num
        
        return self.booked

f = Flight(50)
print(f"The total no of seats {f.total}")
f.booking(20)
print(f"Booked seat {f.booked}")
f.booking(10)
print(f"Booked seat {f.booked}")
