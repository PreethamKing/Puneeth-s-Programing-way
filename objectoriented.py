class Ex1:
    pass

class Car :
    def __init__(self):
        print("class content")
        print('self : ',self)

class Myfunction :
    def __init__(self,name):
        self.name = name
        print(f"name {self.name}")
        
    def some_method(self) :
        print(f"some_method {self.name}")
    
    def __del__(self) :
        print(f"delete {self.name}")
        
class Person :
    def __init__(self,name,age) :
        self.name = name
        self.age = age
    def display(self) :
        print(self.name,self.age)

class getset :
    def __init__(self,name) :
        self.name = name
    def get_name(self) :
        return self.name
    def set_name(self,new_name) :
        self.name = new_name 

class candidate :
    def __init__(self):
        self.register_no = None
        self.score = None
    def input(self) :
        self.register_no = input("Enter the register number")
        self.score = input("Enter the score obtained")
    def Selection(self) :
        if self.score >= 60 :
            print ("Selected")
        else :
            print ("not Selected")
            
class Travel:
    def __init__(self):
        self.travel_code = 105
        self.place = "Bombay"
        self.number_of_travelers = 15
        self.number_of_buses = 5

    def input(self):
        self.travel_code = int(input("Enter Travel Code: "))
        self.place = input("Enter Place: ")
        self.number_of_travelers = int(input("Enter Number of Travelers: "))
        if self.number_of_travelers >= 10:
            self.number_of_buses = 1
        else:
            self.number_of_buses = 0

    def display(self):
        print(f"Travel Code: {self.travel_code}")
        print(f"Place: {self.place}")
        print(f"Number of Travelers: {self.number_of_travelers}")
        print(f"Number of Buses: {self.number_of_buses}")
        
class Stock :
    def __init__(self):
        self.item_code = None
        self.item_name = None
        self.price = None
        self.quality = None
        self.discount = 0
    
    def  CalcDisc(self):
        if self.quality <= 100 :
            self.discount = 0
        elif self.quality <= 150 :
            self.discount = 5
        else :
            self.discount = 10        
    def Enter_Details(self) :
        self.item_code = input("Entre the item code >> ")
        self.item_name = input("Enter the name of item >> ")
        self.price = input("Enter the price of item >> ")
        self.quality = input("Enter the quality of item >> ")
        self.CalcDisc()
    def display(self) :
        print(self.item_code)
        print(self.item_name)
        print(self.price)
        print(self.quality)
        print(self.discount)
        
        
class BankAccount:
    def __init__(self):
        self.account_type = None
        self.balance = 0.0

    def initialize(self, account_type, initial_balance):
        self.account_type = account_type
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Insufficient balance.")

    def display(self):
        print(f"Account Type: {self.account_type}")
        print(f"Balance: {self.balance}")

class shape :
    def cal_area(self) :
        pass

class rectangle(shape) :
    def  __init__(self,length,breath):
        self.length = length
        self.breath  = breath
    def cal_area(self) :
        return self.length*self.breath
    
class triangle(shape) :
    def __init__(self,radius):
        self.radius = radius
    def cal_area(self):
        return (3.14*(self.radius**2))
    
class Audiofile:
    def __init__(self, filename):
        self.filename = filename

    def play(self):
        raise NotImplementedError("Subclasses must implement this method")

class MP3File(Audiofile):
    def play(self):
        print(f"Playing MP3 file: {self.filename}")

class WAVFile(Audiofile):
    def play(self):
        print(f"Playing WAV file: {self.filename}")

class car :
    car_name = "Cau"

class TotalRuns:
    def __init__(self, name, no_matches):
        self.name = name
        self.no_matches = no_matches
        self.run = 0

    def calculate_runs(self):
        self.run = self.no_matches * 6

    def display(self):
        print(f"No of runs scored by {self.name} is {self.run}")

# Data
players = ["k", "ni", "si"]
no_matches = [1, 2, 3]

# Creating objects and displaying runs
"""for i in range(len(players)):
    player = TotalRuns(players[i], no_matches[i])
    player.calculate_runs()
    player.display()"""
    
    
class car :
    make =  "TATA"
    def __init__(self,name,milage):
        self.name = name
        self.mil = milage
        
        
class A :
    def __init__(self,L):
        self.list = L
class B(A) :
    def remove(self) :
        list1 = []
        for i in self.list :
            if i not in list1 :
                self.list.append(list1)
        return list1
        
ls = [1,23,4,4,1]
c = B(ls)