from datetime import datetime

class Person:
    
    def __init__(self, name = "no_name"):
        self.__name = name
    
    def setname(self, name):
        self.__name = name

    def getname(self):
        return self.__name

    def getFullDetails(self):
        return "Name: " + self.getname()
    
    def displayInfo():
        pass


class Client(Person):

    def __init__(self, name="no_name", discount=0):
        super().__init__(name)
        self.__discount = discount

    def getdiscount(self):
        return self.discount
    
    def setdiscount(self, discount):
        self.discount = discount
    
    def displayInfo(self):
        print(f"name:{self.__name}, discount:{self.__discount}")

class Psychologist(Person):

    def __init__(self, name="no_name", cost=0):
        super().__init__(name)
        self.__cost = cost

    def getcost(self):
        return self.__cost
    
    def setcost(self, cost):
        self.__cost = cost
    
    def displayInfo(self):
        print(f"name:{self.__name}, cost:{self.__cost}")

class Zoom:

    def __init__(self, URL = "", time = ""):
        
        self.__URL = URL 
        self.__time = time

    def geturl(self):
        return self.__URL
    
    def gettime(self):
        return self.__time
    
    def settime(self, time = ""):
        self.__time = time
    
    def setURL(self, URL = ""):
        self.__URL = URL
    
class Meeting:


    def __init__(self,  client = Client(), psychologist= Psychologist(), zoom = Zoom()):
        self.__client, self.__psychologist, self.__zoom = client, psychologist, zoom

    def doMeet(self):
        print(f"client: {self.__client.getname()}, psychologist: {self.__psychologist.getname()}, zoom: {self.__zoom.geturl()}, time: {self.__zoom.gettime()}")


if __name__ == "__main__":
    client = Client("client1", 100)
    psychologist = Psychologist("psy1",2000)
    zoom = Zoom("Zoom/UjwUdnO",datetime(2024, 12, 12, 23, 0,).strftime("%d/%m/%Y %I:%M %p"))
    meet = Meeting(client, psychologist, zoom)
    meet.doMeet()
    



