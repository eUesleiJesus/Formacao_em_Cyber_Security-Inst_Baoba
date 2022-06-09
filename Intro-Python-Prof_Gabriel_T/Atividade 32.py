for i in range(1,51):

    if a == True and b == True:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
        a = True
    elif i % 3 == 0:
        print("Fizz")
        b = True
    else:
        print(i)