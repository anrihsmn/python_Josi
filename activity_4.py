menu = '''
(1) trapezoid
(2) cylinder
'''
# (1) V = (t + b)* h / 2
# (2) V = h * r * r * 3.14159

print(menu)
selected_number = int(input("choose your number: "))

if selected_number == 1:
  bottom_length = int(input('Enter a bottom length: '))
  top_length = int(input('Enter a top length: '))
  height = int(input('Enter a height: '))
  print('Trapezoid answer is ', (bottom_length + top_length) * height / 2)

elif selected_number == 2:
  height = int(input('Enter a height: '))
  radius = int(input('Enter a radius: '))
  print('Cylinder answer is ', height * (radius ** 2) * 3.14159)

else:
  print("Try again")