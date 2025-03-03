
#this code was created with the assistance of online reference material
#I have included comments that specify what ive learned through-out the code

import json  #this allows me to use the data and store it 
#Instruction #1 "define a class with attributes 
#here im  essentially creating a "blueprint" for my class person
class Person:
    def __init__(self, name, age, email): #lookslikeiuseselftotiepersontotheattributes
        self.name = name 
        self.age = age 
        self.email = email 
    def to_dict(self):
        return{
            "type": "Person",
            "name": self.name,
            "age" : self.age
        }   
 #now that the class has been made for person with this name age and email attri
 #we make a instance of that class or in other words our first person        
person1=Person("Mclovin", 24, "coley@cpp.edu")

print(person1.name)
print(person1.age)
print(person1.email)

class Student(Person):
    def __init__(self, name, age, email, student_id):
     super().__init__(name, age, email)
     self.student_id = student_id
    def to_dict(self):
       data = super().to_dict()
       data["type"] = "student"
       data["student_id"] = self.student_id
       return data 
student1 = Student("Fogell", 21, "fogell@cpp.edu", 321)   
print(student1.name) 
print(student1.age)
print(student1.email)
print(student1.student_id)

def save_to_json(filename, people):
    with open(filename,"w") as file:
        json.dump([person.to_dict() for person in people], file,indent=4)
 
 
save_to_json("people_data.json", [person1, student1])   
    
def display_json(filename):
    with open(filename,"r") as file: 
        data = json.load(file)
        print("\n--- JSON File Content ---")
        print(json.dumps(data,indent=4))
        
display_json("people_data.json")
