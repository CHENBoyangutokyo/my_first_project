class student():
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return "Name = " + self.name + " age = " + str(self.age)
    
  