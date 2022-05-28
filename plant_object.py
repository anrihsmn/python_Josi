
# class Plant:
#   def __init__(self):
#     self.size = 0
#     # self.flower_date = flower_date
#     # self.fruits_date = fruit_date
  
#   def added_water(self,water_value):
#     self.size += water_value

#   def added_bad_food(self,food_value):
#     self.size -= food_value

#   def get_size(self):
#     return self.size
  
#   def get_flower(self,date):
#     if date =="04/12/2021":
#       return "Here is your flower."

#   def get_fruit(self,date):
#     if date =="04/13/2021":
#       return "Here is your fruit."



# new
class Plant:
  def __init__(self):
      self.size = 0
  
  def grow(self,water):
    self.size += water
    return self.size

  def get_flower(self,date):
    if date == "04/12":
      return "Here is your flower!"
  
  def get_fruit(self,date):
    if date == "04/13":
      return "Here is kiwi!"
  
  def wilt(self,bad_food):
    self.size -= bad_food
    return self.size
