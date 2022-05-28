
def conv_to_roman(number):

  if number >= 1000:
    print('M',end='')
    number -= 1000
    conv_to_roman(number)
  elif number >= 500:
    print('D',end='')
    number -= 500
    conv_to_roman(number)
  elif number >= 100:
    print('C',end='')
    number -= 100
    conv_to_roman(number)
  elif number >= 50:
    print('L',end='')
    number -= 50
    conv_to_roman(number)
  elif number >= 40:
    print('XL',end='')
    number -= 40
    conv_to_roman(number)
  elif number >= 10:
    print('X',end='')
    number -= 10
    conv_to_roman(number)
  elif number == 9:
    print('IX',end='')
    number -= 9
    conv_to_roman(number)
  elif number >= 5:
    print('V',end='')
    number -= 5
    conv_to_roman(number)
  elif number == 4:
    print('IV',end='')
    number -= 4
    conv_to_roman(number)
  elif number >= 1:
    print('I',end='')
    number -= 1
    conv_to_roman(number)

conv_to_roman(1500)