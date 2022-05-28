
class calculators:
  def __init__(self) -> None:
      pass
    
  def area_rectangle(self,xlength,ylength):
    return xlength * ylength
  def area_square(self,xlength):
    return xlength ** 2
  def area_circle(self,radius):
    return radius ** 2 * 3.14159 
  def area_triangle(self,xlength,ylength):
    return xlength * ylength / 2
