from token import *

class Interpreter:
   
   # Token types
   # 
   RES = "RES"
   PHASE = "PHASE"
   NAME = "NAME"

   # RES values
   #
   QUBIT = "qubit"
   H = "H"
   PX = "pX"
   PY = "pY"
   PZ = "pZ"
   P_SHIFT = "pShift"
   READ = "read"

   data = ""
   split_data = []
   tokenized_data = []

   def __init__(self, data):
      
      self.data = data
      self.split_data = self.data.split()
      
      for word in self.split_data:
         self.tokenized_data.append(self.tokenize(word))

      for token_item in self.tokenized_data:
         # Execute corresponding command
         print token_item.type_name
         print token_item.value
         print ""
      
   def tokenize(self, word):

      token_type = ""
      token_name = ""

      if word == self.QUBIT:
         token_type = self.RES
         token_name = self.QUBIT
      elif word == self.H:
         token_type = self.RES
         token_name = self.H
      elif word == self.PX:
         token_type = self.RES
         token_name = self.PX
      elif word == self.PY:
         token_type = self.RES
         token_name = self.PY
      elif word == self.PZ: 
         token_type = self.RES
         token_name = self.PZ
      elif word == self.P_SHIFT:
         token_type = self.RES
         token_name = self.P_SHIFT
      elif word == self.READ: 
         token_type = self.RES
         token_name = self.READ
      elif word[0].isdigit(): 
         # Must be a PHASE
         token_type = self.PHASE
         token_name = word
      else: 
         # Must be a NAME
         token_type = self.NAME
         token_name = word

      return Token(token_type, token_name)
