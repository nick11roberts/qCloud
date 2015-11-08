from qtoken import *
from qubit import *
from gate import *

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
               
      qubit_name = tokenized_data[1].value
      
      # Execute corresponding command
      if tokenized_data[0].type_name == self.RES:

         if tokenized_data[0].value == self.QUBIT:
            # Create a new qubit
            self.quantum_computer[qubit_name] = Qubit(qubit_name)
            return Gate.qubit_init(self.quantum_computer[qubit_name])

         elif tokenized_data[0].value == self.H:
            # Compute the 2*2 Hadamard transformation on the qubit
            return Gate.hadamard(self.quantum_computer[qubit_name])

         elif tokenized_data[0].value == self.PX:
            # 
            return Gate.pauli_x(self.quantum_computer[qubit_name])

         elif tokenized_data[0].value == self.PY:
            # 
            return Gate.pauli_y(self.quantum_computer[qubit_name])

         elif tokenized_data[0].value == self.PZ:
            #
            return Gate.pauli_z(self.quantum_computer[qubit_name])

         elif tokenized_data[0].value == self.P_SHIFT:
            # 
            phi = tokenized_data[2].value
            return Gate.phase_shift(self.quantum_computer[qubit_name], phi)

         elif tokenized_data[0].value == self.READ:
            # 
            return Gate.read(self.quantum_computer[qubit_name])

      elif tokenized_data[0].type_name == self.PHASE:
         # This should not happen
         print self.ERROR

      elif tokenized_data[0].type_name == self.NAME:
         # This should not happen
         print self.ERROR

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

      return QToken(token_type, token_name)
