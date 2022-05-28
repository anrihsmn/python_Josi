
class Reservation:
  def __init__(self,name, date, table):
    self.name = name
    self.date = date
    self.table = table
  
  def get_res_name(self):
    return self.name
  
  def get_res_date(self):
    return self.date
  
  def get_res_table(self):
    return self.table