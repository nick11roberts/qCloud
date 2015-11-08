import random
import math

class Qubit:

   name = ""
   v_0 = 0
   v_1 = 1
   final_state = 0
   state_read = False

   def __init__(self, name): 
      self.name = name
      self.randomize_state()

   def randomize_state(self):
      rand = random.random()
      rand_comp = 1 - rand
      self.v_0 = math.sqrt(rand)
      self.v_1 = math.sqrt(rand_comp)

   def read_state(self):
      if not(self.state_read):

         self.state_read = True
         rand = random.random()

         if rand > self.v_0:
            self.final_state = 1
         elif rand < self.v_0:
            self.final_state = 0
         else:
            self.read_state()

      return self.final_state
