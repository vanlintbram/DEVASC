class Location:
    def __init__(self,name, country):
        self.name = name
        self.country = country

    def myLocation(self):
        print(f"{self.name} lives in {self.country}")

loc1 = Location("Bram", "Grimbergen")
loc2 = Location("Ine", "Humbeek")
loc3 = Location("Jonas", "Mechelen")

loc1.myLocation()
loc2.myLocation()
loc3.myLocation()


