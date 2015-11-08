import random
import math

class Qubit:

   name = ""
   v0 = 0
   v1 = 1

   def __init__(self, name): 
      self.name = name
      self.randomizeState()
      print name

   def randomizeState(self):
      v0 = random.random()
      v1 = math.sqrt(1 - (v0 ** 2))
      print v0
      print v1
