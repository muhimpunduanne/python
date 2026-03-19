for number in range(1,10):
    if number % 2 ==0:

        print(number)



def greet():
    print("hello there")
    print("you're welcome")

greet()
 


def get_greeting(name):
    return f"Hi {name}"

message = get_greeting("anne")




def increment(number,by):
    return number + by


result= increment(2,1)

print(result)