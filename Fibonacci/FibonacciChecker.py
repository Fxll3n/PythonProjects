import math


def isPerfectSquare(x):
	s = int(math.sqrt(x))
	return s*s == x
	
def isFibonacci(n):
	
	return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)
	
number = int(input("Enter an intager: "))

x = isFibonacci(number)

if x == True:
	print(f"{number} is a fibonacci!")
else:
	print(f"{number} is not a fibonacci...   :(")
