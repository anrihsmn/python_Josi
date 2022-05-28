
from module_act import file1
from module_act import file2

number = int(input("Enter your number: "))
name = input("Enter your name: ")
country = input("Enter your country: ")

file1.check_adult(number)
file1.check_number(number)

file2.show_info(name, country)