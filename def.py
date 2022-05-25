#  create a function that accepts 2 numbers
#  greeting(name ="susan",age=21 )
#  greeting(age=21, name ="susan")
def my_country(country="Uganda",student= "angela"):
         return f"hello {student}you are from {country}"


def hello_people(*names):
     print(names)

     hello_people()
     hello_people( "Jojo","Angel")

     for name in names:
         print(f"hello names")


#write a function that accepts any number of integers and returns sum of all them
       
def sum(*numbers):
     sum=0
     for number in numbers:
       sum+=number
     return sum

#  #write a function that accepts any number of integers and returns sum of all them

#  def multiply(*numbers):
#           num=1
#           for number in numbers:
#               num*=number
#           return num