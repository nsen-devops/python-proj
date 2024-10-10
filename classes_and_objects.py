class Person_details:
    total_person = 0

    def __init__(self, naam, umar):
        self.name = naam
        self.__age = umar
        Person_details.total_person += 1

    def get_age(self):
        return self.__age

    def info(self):
        return(f"{self.name} is {self.__age} years old")

person_a = Person_details("nitin", 20).info()
#person_b = Person_details("nitesh", 18).info()
print(person_a)
#print(person_b)

class employee_details(Person_details):
    def __init__(self, naam, umar, occ):
        self.occupation = occ
        super().__init__(naam, umar)

    def emp_info(self):
        return(f"{self.name} is a {self.occupation} who is {self.get_age()} years old")
        
    
person_c = employee_details("kirti", 16, "Engineer").emp_info()
print(person_c)

print(f"total {Person_details.total_person} people details recorded.")
