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
      rand = random.random()
      randComp = 1 - rand
      v0 = math.sqrt(rand)
      v1 = math.sqrt(randComp)
      print v0
      print v1
