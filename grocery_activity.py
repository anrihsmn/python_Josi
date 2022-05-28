
# new
from grocery_object_function import Grocery

grocery_lists = []

def show_lists():
  global grocery_lists
  for item in range(len(grocery_lists)):
    print(item, ")", grocery_lists[item].get_gro_name(), grocery_lists[item].get_gro_price())

def check_total():
  total_price = 0
  for list in range(len(grocery_lists)):
    print(list, ")", grocery_lists[list].get_gro_name(), grocery_lists[list].get_gro_price())
    total_price += grocery_lists[list].get_gro_price()
  print("Total price is: ", str(total_price))

while True:
  menu = input("Press 'a' to add, press 't' to view total, press 'd' to delete: ")
  if menu == "a":
    gro_name = input("Enter grocery name: ")
    gro_price = int(input("Enter grocery price: "))
    
    gg1 = Grocery(gro_name, gro_price)

    grocery_lists.append(gg1)

  elif menu == "t":
    check_total()
  
  elif menu == "d":
    show_lists()
    selected_number = int(input("Choose number you want to delete: "))
    grocery_lists.remove(grocery_lists[selected_number])
    print(grocery_lists)
  
  elif menu == "q":
    break






# from grocery_object_function import Grocery

# grocery_items = []

# print("Press 't' to view total in item name.")
# print("Press 'd' to delete items in item name.")
# print("Press 'q' to qiot in item name.")

# def show_items():
#   global grocery_items
#   for x in range(len(grocery_items)):
#     print(x, ")", grocery_items[x].get_gro_name(), grocery_items[x].get_gro_price())

# while quit != "q":
#   item_name = input("Enter item name: ")
#   if item_name == "t" or item_name == "T":
#     total_price = 0
#     for x in range(len(grocery_items)):
#       print(x, ")", grocery_items[x].get_gro_name(), grocery_items[x].get_gro_price())
#       total_price += grocery_items[x].get_gro_price()
#     print("Total price: ", str(total_price))
#   elif item_name == "d" or item_name == "D":
#     show_items()
#     delete_item = int(input("Which item do you want to delete? Choose index number: "))
#     grocery_items.remove(grocery_items[delete_item])
#     show_items()

#   elif item_name != "q":
#     item_price = int(input("Enter item price: "))
#     gg1 = Grocery(item_name,item_price)
#     grocery_items.append(gg1)

#   elif item_name == "q":
#     break