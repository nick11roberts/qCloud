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
      split_data = self.data.split()
      
      for word in split_data:
         tokenized_data = self.tokenize(word)

      #for token_item in tokenized_data:
         # Execute corresponding command
      
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
      #else: 
         # Must be either a NAME or a PHASE

      return Token(token_type, token_name)
