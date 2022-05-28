
grade_number = float(input('Enter a grade number: '))
print(grade_number)

if grade_number >= 97.5 and grade_number <= 100:
  print('A+')
elif grade_number >= 92.5 and grade_number <= 97.4:
  print('A')
elif grade_number >= 90 and grade_number <= 92.4:
  print('A-')
elif grade_number >= 87.5 and grade_number <= 89.9:
  print('B+')
elif grade_number >= 82.5 and grade_number <= 87.4:
  print('B')
elif grade_number >= 80 and grade_number <= 82.4:
  print('B-')
elif grade_number >= 77.5 and grade_number <= 79.9:
  print('C+')
elif grade_number >= 72.5 and grade_number <= 77.4:
  print('C')
elif grade_number >= 70 and grade_number <= 72.4:
  print('C-')
elif grade_number >= 67.5 and grade_number <= 69.9:
  print('D+')
elif grade_number >= 60 and grade_number <= 67.4:
  print('D-')
elif grade_number < 60:
  print('E')
else:
  print('Try again')