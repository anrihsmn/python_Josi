
# new
number_lists = []

print("Press 't' in enter number place, when you want to see top5 numbers.")
print("Press 'q' to quit.")

while True:
  add_number = input("Enter number you  want to add lists: ")
  if add_number == "q":
    break

  elif add_number == "t":
    print(number_lists)
    number_lists.sort()
    print(number_lists)
    for list in range(-1, -6, -1):
      print(number_lists[list], end=" ")
    print()

  else:
    number_lists.append(add_number)




# old one
# print("Press t if you want to see list.")
# selected_lists = []

# while True:
#   selected_number = input("Enter number: ")
#   if selected_number == "t" or selected_number == "T":
#     print(selected_lists)
#     selected_lists.sort()
#     print(selected_lists)
#     for number in range(-1,-6,-1):
#       print(selected_lists[number], end=" ")
#     print()
      
#   else:
#     selected_lists.append(selected_number)

