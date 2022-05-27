def hello(name,age):
    year = 2022-22
    return(f"Hello {name} you were born in {year}")

def my_country(name="Jojo",country = "Rwanda"):
    return(f"Hello {name} you are from {country}")


def greeting(*names):
    for name in names:
        return(f"Hello {name} you are the best.")

def sum(*numbers):
    sum=0
    for numb in numbers:
        sum+=numb
        return(sum)

def multiply(*numbers):
    multiply=1
    for num in numbers:
        multiply*=num
        print(multiply)

def divide(num1,num2):
    result=num1/num2
    print(result)
    # print(num1/num2)

    # keys= kwargs.keys
def sum_and_greet(*args,**kwargs):
    sum=0
    for num in args:
        sum+=num
    
    keys= kwargs.keys()
    if "name" in keys:
        print(f"Hello {kwargs['name']} the answer is {sum}")

    elif "country" in keys:
         print(f"Hello {kwargs['name']} the answer is {sum}")

    elif not keys:
        print(f"Hello anonymous, the answer is {sum}")


def greet(**kwargs):
    keys = kwargs.keys()
    if "country" in keys:
        print(f"Hello {kwargs['name']} you are from {kwargs ['country']}")

    elif "age" in keys:
        year = 2022 -kwargs["age"]
        print(f"Hello {kwargs['name']} you were born in {year}")




 

        

 





    




        




    



