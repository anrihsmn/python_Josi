
menu = '''
(1) add
(2) subtract
(3) mulplication
(4) divide
(5) modulo
(6) power
(7) floor divition
'''
# block string ''' or """

print(menu)
selected_number = int(input("choose your number: "))
first_number = int(input('enter first number: '))
second_number = int(input('enter second number: '))


if selected_number == 1:
  print('answer: ',first_number + second_number)
elif selected_number == 2:
  print('answer: ',first_number - second_number)
elif selected_number == 3:
  print('answer: ',first_number * second_number)
elif selected_number == 4:
  print('answer: ',first_number / second_number)
elif selected_number == 5:
  print('answer: ',first_number % second_number)
elif selected_number == 6:
  print('answer: ',first_number ** second_number)
elif selected_number == 7:
  print('answer: ',first_number // second_number)
else:
  print('try again')
