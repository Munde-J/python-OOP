class Student:
    name = "Angela"
    age  = 20
    country ="Kenya"
    school = "Akirachix"

#Add these methods to class student - full_name, year_of_birth, initials. 
#Create two instances and verify the work as expected

class Student:
    school ="Akirachix"
    def __init__(self,name,age,country):
        self.name = name
        self.age  = age
        self.country =country

    def greeting(self):
      return f"Hello {self.name} from {self.country} welcome to {self.school}"


#Add these methods to class student - full_name, year_of_birth, initials. 
#Create two instances and verify the work.

class Student:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        

    def full_name(self):
        name=f"{self.first_name} {self.last_name}"
        return name
        
    def year_of_birth(self):
        year=2022-self.age
        return year

    def initials(self):
        return f" {self.first_name[0]}{self.last_name}" 


        
          
        
        

  

          

        

