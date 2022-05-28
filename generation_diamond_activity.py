
generation = int(input("Enter the number(min:2)"))

for x in range(1,generation+1):
  number = "1"
  number *= x
  print(number)

for x in range(generation-1,0,-1):
  number = "1"
  number *= x
  print(number)

