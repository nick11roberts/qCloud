import random
import math

class Qubit:
''' 
   Represents a single qubit in quantum computing.
   Contains a methods for randomizing the state of the
   qubit and for reading the state of the qubit. 
'''

   name = ""
   v_0 = 0
   v_1 = 1
   final_state = 0
   state_read = False

   def __init__(self, name): 
      '''
         constructor. 
      '''
      self.name = name
      self.randomize_state()

   def randomize_state(self):
      '''
         The state should only be randomized once. 
      '''
      rand = random.random()
      rand_comp = 1 - rand
      self.v_0 = math.sqrt(rand)
      self.v_1 = math.sqrt(rand_comp)

   def read_state(self):
      '''
         The state can only be read one time. 
      '''
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
