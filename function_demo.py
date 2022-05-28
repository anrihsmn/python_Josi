
# def show_sum(a,b):
#   print(a+b)

# show_sum(10,20)


# def show_sum_if_numbers_odd(a,b):

#   if a % 2 == 1 and b % 2 == 1:
#     print(a + b)
#   else:
#     print("numbers not odd!")

# show_sum_if_numbers_odd(13,17)
# show_sum_if_numbers_odd(20,18)


# def keyword_agument1(name1,name2,age1,age2):

#   print("name1", name1)
#   print("age1", age1)
#   print("name2,", name2)
#   print("age2",age2)

# keyword_agument1(name1="kinoko",age1=20,name2="Jessica",age2=40)


# def demo_default_params(name1="Kyoko",age1=100,name2="nakata",age2=0):
#   print("name1",name1)
#   print("age1",age1)
#   print("name2",name2)
#   print("age2",age2)

# demo_default_params()


# def get_squeare_of_number(number):
#   return number ** 2

# print(get_squeare_of_number(20))

# def show_sum(a,b):
#     return a+b

# print(show_sum(10,20))


# functions returning values
def return_square_even(some_value1):
  #Return squere only if value is even
  if some_value1 % 2 == 0:
    return some_value1**2
  else:
    return some_value1
  
print(return_square_even(20))
print(return_square_even(17))



number1 = 10

# number1 = number1 + 15 same 
number1 += 15

print(number1)