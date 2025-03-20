# Function

def say_hello(name):
    print(f"hello {name}")
    
say_hello("Tanjila")


def say_name(*name):
    print(f"hello {name[2]}")
    
say_name("Tanjila", "habib", "Chowdhury")

def myfor_function(lis):
    for x in lis:
        print(x)

lis = ["ae", "baet", "gaet"]

myfor_function(lis)