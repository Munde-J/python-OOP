def add(a,b):
    answer=a+b
    return answer

def subtract(a,b):
    answer=a-b
    return answer

def multipl(a,b):
    answer=a*b
    return answer

def divide(a,b):
    answer=a/b
    return answer

def modulus(a,b):
    answer=a%b
    return  answer

def exponent(a,b):
    answer=a**b
    return  answer  

def int_divide(a,b):
    answer=a//b
    return answer

def square(a):
    answer=a*a
    return answer

def cube(a):
    answer=a**a
    return answer

    n = 23
fact = 1
  
# for i in range(1,n+1):
#     fact = fact * i
      
# print ("The factorial of 23 is : ",end="")
# print (fact)

# def factorial(a):
#     n= 200
#     factorial = 1
#     for n in  range(5,factor+_1):
#      factorial=fa

def factorial(number):
    factor=1
    for i in  range(1,number,+1):
        factor*= i
    return factor
