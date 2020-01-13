
def min(x, y):
    if(x < y): return x
    else:
        return y

print(min(7,5))


def max(x, y):
    if (x > y): return x
    else:
        return y


num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
print("The maximum is:",max(num1, num2))



def len(iterable):
    return sum(1 for x in iterable)

x = input("Enter a word:")

print("The length is:", len(x))



def multiply(x, y):

   if x == 0:
      return 0
   elif x == 1:
      return y
   else:
      return y + multiply(x-1, y)

num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
print("The result is:", multiply(num1, num2))


def pow(x, y):
    num = 1
    for function in range(y):
        num = num*x 
    return num


num1=int(input("Enter number: "))
num2=int(input("Enter exponent: "))
print("The result is:", pow(num1, num2))