
number_items = [1,3,5,7,9]
banana_numbers = [10,20,30,40,50]

def sum_number(numbers):
  sum = 0
  for x in numbers:
    sum += x
  return sum 

print(sum_number(number_items))
print(sum_number(banana_numbers))

