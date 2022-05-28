# from plant_object import Plant

# water1 = Plant()
# give1 = Plant()

# while True:
#   val_water = int(input("Enter water amount: "))
#   water1.added_water(val_water)
#   print('Current amount is: ',water1.get_size())
#   option = int(input('Do you want to give bad food? Enter amount, or 0 if no: '))
#   if option > 0:
#     water1.added_bad_food(option)

#   flowerdate = input("Enter '04/12/2021' if you want your flower, press n if no: ")
#   if flowerdate == "14/12/2021":
#     print(give1.get_flower(flowerdate))
#   fruitdate = input("Enter '04/13/2021' if you want your flower, press n if no: ")
#   if flowerdate == "14/13/2021":
#     print(give1.get_fruit(fruitdate))

#   quit = input("Do you want to quit?(y/n)")
#   if quit == "y" or quit == "Y":
#     break




# new

from plant_object import Plant

pp1 = Plant()

while quit != "q":
  water_amount = int(input("Enter wanter amount: "))
  total_size = pp1.grow(water_amount)
  print("Current size: ", total_size)

  bad_food = int(input("Do you want to give bad food? Enter amount, enter 0,if no.: "))
  if bad_food > 0:
    total_size = pp1.wilt(bad_food)
    print("Current size: ", total_size)

  flower_date = input("Enter 04/12 if you want flower: ")
  # if flower_date ="04/12"
  print(pp1.get_flower(flower_date))

  fruit_date = input("Enter 04/13 if you want fruit: ")
  # if fruit_date == "04/13":
  print(pp1.get_fruit(fruit_date))

  quit = input("Quit? press q to quit.: ")
  quit == "q"