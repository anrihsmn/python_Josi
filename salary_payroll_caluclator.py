
def gross_salary(hours,rate):
  return hours * rate
def tax(salary):
  return salary * 0.12
def benefit(medical_bene,unemploy):
  return medical_bene + unemploy

medical_insurance = 1000
unemployment = 1500


while quit != 'q':
  h = float(input('Enter your working hours of this month: '))
  r = int(input('Enter your rate: '))
  sal = gross_salary(h,r)
  if sal > 12000:
    t = tax(sal)
    print('Your tax is: ', t)
  elif sal <= 12000:
    t = 0
    print('Your tax is: ', t)
  else:
    print('Try again.')


  emp_type = input('Press "r" if regular employment, or press the other button: ')
  if emp_type == 'r':
    benef = benefit(medical_insurance,unemployment)
    b = benef
    print('Your benefit is: ', b)
  else:
    b = 0
    print('Your benefit is: ', b)

  
  print('Your gross salary is: ',sal)
  print('Your net salary is: ',int(sal-(t+b)))

  quit = input('Exit? press q to quit: ')
  # if quit == 'q':
  #   break
  quit == 'q'
  