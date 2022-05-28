
first_num = int(input("enter first number: "))
second_num = int(input("enter second number: "))
third_num = int(input("enter third number: "))

def return_square_odd(first_num, second_num, third_num):
  if first_num % 2 == 1:
    return second_num ** 2, third_num ** 2
  else:
    return second_num + third_num

print(return_square_odd(first_num, second_num, third_num))
# print(return_square_odd(1, 4, 6))

