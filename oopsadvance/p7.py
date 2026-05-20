class pri:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    
    def getter(self):
        print(f"The name is {self.__name}")
        print(f"The age is {self.__age}")
    def setter(self,name,age):
        self.__name = name
        self.__age = age
    
p = pri("riyan",19)
p.getter()
p.setter("Hello",20)
p.getter()
