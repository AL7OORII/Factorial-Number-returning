#TASK 1
def factorial_number(n):

    if n == 0:
        return 1 #that the factorial of 0 is 1
    if n < 1:
        print("there is an error, please choose another number") #This message will appear if the number entered is negative
    else:
        return n * factorial_number(n - 1)
      
n = int(input("enter a number to return its factorial : "))
print("the factorial of the number you entered is", factorial_number(n))


