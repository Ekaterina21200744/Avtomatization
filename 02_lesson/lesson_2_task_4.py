n = int(input ("Введите число:"))
         
def fizz_buzz(n):
    for x in range (1,n):
        if x % 3 ==0:
            print ("Fizz")
        elif x % 5 ==0:
            print ("Buzz")
        elif x % 5 ==0  and x % 3 ==0: print ("FizzBuzz")
        else: print (x)

fizz_buzz(n)

