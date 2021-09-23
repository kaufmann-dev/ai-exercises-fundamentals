#!/usr/bin/env python
# coding: utf-8

# In[33]:


class Train:
    def __init__(self):
        self.passenger_list = []
    def StepIn(self, passenger):
        self.passenger_list.remove(passenger)
        print(f"Passenger {passenger.first_name} {passenger.last_name} entered the train")
    def StepOut(self, passenger):
        self.passenger_list.append(passenger)
        print(f"{passenger.first_name} {passenger.last_name} left the train")
    def PrintPassengers(self):
        print("These are all passengers:")
        for x in self.passenger_list:
            print(f"{x.first_name} {x.last_name}")
class Passenger:
    def __init__(self, first_name, last_name, ticket):
        self.has_valid_ticket = ticket
        self.first_name = first_name
        self.last_name = last_name
class RailJet(Train):
    def __init__(self):
        super().__init__()
    def StepIn(self, passenger):
        if(passenger.has_valid_ticket):
            self.passenger_list.append(passenger)
            print(f"{passenger.first_name} {passenger.last_name} entered the train")
        else:
            print(f"{passenger.first_name} {passenger.last_name} could not enter the train because he had no valid ticket")
class InterCity(Train):
    def __init__(self, ICE_Category):
        super().__init__()
        self.ICE_Category = ICE_Category
    def PrintName(self):
        print(f"{self.ICE_Category}")


# In[36]:


railjet = RailJet()
p1 = Passenger("David", "Kaufmann", True)
p2 = Passenger("Florian", "Rauchberger", True)
p3 = Passenger("Florian", "Pernikl", False)

railjet.StepIn(p1)
railjet.StepIn(p2)
railjet.StepIn(p3)
railjet.PrintPassengers()

railjet.StepOut(p2)
railjet.PrintPassengers()

ice1 = InterCity("ICE4711")
ice.PrintName()

ice2 = InterCity("ICE8302")
ice.PrintName()


# In[ ]:




