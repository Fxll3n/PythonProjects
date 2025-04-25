#Made by TheArchangelWarrior on github

nterms = int(input("Enter the number of terms"))
n1, n2 = 0, 1
count = 0

if nterms == None and nterms <= 0:
  print("Please use a valide intager that is higher than 0")
else:
  while count < nterms:
    print(n1)
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    count += 1
