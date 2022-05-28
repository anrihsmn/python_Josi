
from math_functions import calculators

cc = calculators()

menu = '''
(1) rectangle
(2) square
(3) circle
(4) triangle
'''

print(menu)
selected_number = int(input("Enter a menu number: "))
print(selected_number)

# x = int(input("enter x: "))
# y = int(input("enter y: "))
# r = int(input("enter a radius: "))

if selected_number == 1:
  x = float(input("enter x: "))
  y = float(input("enter y: "))
  print(cc.area_rectangle(x,y))
elif selected_number == 2:
  x = float(input("enter x: "))
  print(cc.area_square(x))
elif selected_number == 3:
  r = float(input("enter radius: "))
  print(cc.area_circle(r))
elif selected_number == 4:
  x = float(input("enter x: "))
  y = float(input("enter y: "))
  print(cc.area_triangle(x,y))
else:
  print('Try again')




  
