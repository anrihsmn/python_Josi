
from restaurant_res_function import Reservation

reservation_objects = []

def check_lists(res_info):
  # check_reservation is better
  for list in reservation_objects:
    name = list.get_res_name()
    date = list.get_res_date()
    table = list.get_res_table()
    # no need to put name?
    if res_info.get_res_date() == date and res_info.get_res_table() == table:
      return list
      # list or name or list.get_res_name(), list(name, date, table), list(name),list(date), list(table)...???
    return None
    # dont i need to put 'else'?

def show_lists():
  global reservation_objects
  for object in range(len(reservation_objects)):
    print(object, ")", reservation_objects[object].get_res_name(), reservation_objects[object].get_res_date(), reservation_objects[object].get_res_table())



while True:
  menu = input("Press 'r' to reserve, 'c' to cancel, 'u' to update, 'q' to quit: " )
  if menu == "r":
    res_name = input("Enter your name: ")
    res_date = input("Enter date you want tou reserve(mm-dd e.g. 04-05): ")
    res_table = input("Enter table number(1-5)")

    res1 = Reservation(res_name, res_date, res_table)
    # when should i make instance?

    search_reservation = check_lists(res1)
    if search_reservation is None:
      reservation_objects.append(res1)
      print("Reservation seccess!")
    
    else:
      dup_name = search_reservation.get_res_name()
      dup_date = search_reservation.get_res_date()
      dup_table = search_reservation.get_res_table()
      # do i need to make all variables? only reserved_name is fine?
      print("Reservation failed.")
      print("Reservation is already made for", dup_name, ".")
  
  elif menu == "c":
    show_lists()
    selected_object = int(input("Choose number you want to cancel: "))
    reservation_objects.remove(reservation_objects[selected_object])
    show_lists()
  
  elif menu == "u":
    show_lists()
    selected_number = int(input("Choose the number you want tou update: "))
    new_res_name = input("Enter your name again: ")
    new_res_date = input("Enter the date again(mm-dd e.g. 04-05): ")
    new_res_table = input("Enter the table number again(1-5): ")

    res2 = Reservation(new_res_name, new_res_date, new_res_table)
    update_list = check_lists(res2)
    if update_list is None:
      reservation_objects[selected_number].get_res_name = new_res_name
      reservation_objects[selected_number].get_res_date = new_res_date
      reservation_objects[selected_number].get_res_table = new_res_table
      # why i dont need to put()?
      show_lists()
      # error 'str' object is not callable     how to override? 
      print("Reservation success!")
      
    else:
      dup_name = update_list.get_res_name()
      dup_date = update_list.get_res_date()
      dup_table = update_list.get_res_table()
      print("reservation failed.")
      print("the reservation is already made for", dup_name, ".")
  
  elif menu == "q":
    break
