ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
tens = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
hundreds = ["one hundred", "two hundred", "three hundred", "four hundred", "five hundred", "six hundred", "seven hundred", "eight hundred", "nine hundred"]

number = int(input("Enter a number: "))

n1 = number // 1000 % 10
n2 = number // 100 % 10
n3 = number // 10 % 10
n4 = number // 1 % 10

if n1 != 0:
    print(f"{ones[n1 - 1]} thousand", end=" ")

if n2 != 0:
    print(f"{hundreds[n2 - 1]}", end=" ")

if n3 != 0:
    print(f"{tens[n3 - 1]}", end=" ")

if n4 != 0:
    print(f"{ones[n4 - 1]}")
