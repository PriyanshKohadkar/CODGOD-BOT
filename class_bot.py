class maths:
  def __init__(self, int):
        self.int = int   
  def square(self):
      return self.int * self.int 
  def cube(self):
      return self.int * self.int * self.int    
  def exponent(self, power):
      ans = self.int ** power
      return ans