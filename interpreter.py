from token import *
from qubit import *

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

   ERRROR = "error"

   quantum_computer = {}
   # Dictionary of qubits for name access

   def add(self, data):

      split_data = []
      tokenized_data = []
      
      split_data = data.split()
      
      for word in split_data:
         tokenized_data.append(self.tokenize(word))

      for token_item in tokenized_data:
               
         qubit_name = tokenized_data[1].value
         
         # Execute corresponding command
         if tokenized_data[0].type_name == self.RES:

            if tokenized_data[0].value == self.QUBIT:
               # Create a new qubit
               self.quantum_computer[qubit_name] = Qubit(qubit_name)

            elif tokenized_data[0].value == self.H:
               # Compute the 2*2 Hadamard transformation on the qubit
               

            elif tokenized_data[0].value == self.PX:
               # 
               print ""

            elif tokenized_data[0].value == self.PY:
               # 
               print ""

            elif tokenized_data[0].value == self.PZ:
               #
               print ""

            elif tokenized_data[0].value == self.P_SHIFT:
               # 
               print ""

            elif tokenized_data[0].value == self.READ:
               # 
               print ""

         elif tokenized_data[0].type_name == self.PHASE:
            # This should not happen
            print ERROR

         elif tokenized_data[0].type_name == self.NAME:
            # This should not happen
            print ERROR

      for token_item in tokenized_data:
         # Print the current data for debugging
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
