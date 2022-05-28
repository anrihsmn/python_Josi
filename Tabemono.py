
class Food:

  def __init__(self):
      self.food_name = ""
      self.food_price = ""
      self.serve_time = 0

  # setters
  def set_food_name(self,food_name) :
    self.food_name = food_name
  
  def set_food_price(self,food_price):
    self.food_price = food_price
  
  def set_serve_time(self,serve_time):
    self.serve_time = serve_time
  
  # getters
  def get_food_name(self):
    return self.food_name
  
  def get_food_price(self):
    return self.food_price
  
  def get_serve_time(self):
    return self.serve_time