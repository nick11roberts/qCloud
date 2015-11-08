from qubit import *
import wap 
import urllib
import json

class Gate:

   @staticmethod   
   def hadamard(quantum_bit):
      v_0 = quantum_bit.v_0
      v_1 = quantum_bit.v_1
      print "hadamard check"
      server = 'http://api.wolframalpha.com/v1/query.jsp'
      appid = 'XWQ95Q-4Y54GGJEGR'
      input = '{' + str(v_0)  + ',' + str(v_1) + '}'
      input += '*{{1,1},{1,-1}}/(sqrt(2))'

      waeo = wap.WolframAlphaEngine(appid, server)
      query = waeo.CreateQuery(input)
      result = waeo.PerformQuery(query)
      waeqr = wap.WolframAlphaQueryResult(result)
      jsonresult = waeqr.JsonResult()

      return jsonresult

   @staticmethod
   def pauli_x(quantum_bit):
      v_0 = quantum_bit.v_0
      v_1 = quantum_bit.v_1
      print "pauli x check"
      server = 'http://api.wolframalpha.com/v1/query.jsp'
      appid = 'XWQ95Q-4Y54GGJEGR'
      input = '{' + str(v_0)  + ',' + str(v_1) + '}'
      input += '*{{0,1},{1,0}}'

      waeo = wap.WolframAlphaEngine(appid, server)
      query = waeo.CreateQuery(input)
      result = waeo.PerformQuery(query)
      waeqr = wap.WolframAlphaQueryResult(result)
      jsonresult = waeqr.JsonResult()

      return jsonresult

   @staticmethod
   def pauli_y(quantum_bit):
      v_0 = quantum_bit.v_0
      v_1 = quantum_bit.v_1
      print "pauli y check"
      server = 'http://api.wolframalpha.com/v1/query.jsp'
      appid = 'XWQ95Q-4Y54GGJEGR'
      input = '{' + str(v_0)  + ',' + str(v_1) + '}'
      input += '*{{0,-i},{i,0}}'

      waeo = wap.WolframAlphaEngine(appid, server)
      query = waeo.CreateQuery(input)
      result = waeo.PerformQuery(query)
      waeqr = wap.WolframAlphaQueryResult(result)
      jsonresult = waeqr.JsonResult()

      return jsonresult

   @staticmethod
   def pauli_z(quantum_bit):
      v_0 = quantum_bit.v_0
      v_1 = quantum_bit.v_1
      print "pauli z check"
      server = 'http://api.wolframalpha.com/v1/query.jsp'
      appid = 'XWQ95Q-4Y54GGJEGR'
      input = '{' + str(v_0)  + ',' + str(v_1) + '}'
      input += '*{{1,0},{0,-1}}'

      waeo = wap.WolframAlphaEngine(appid, server)
      query = waeo.CreateQuery(input)
      result = waeo.PerformQuery(query)
      waeqr = wap.WolframAlphaQueryResult(result)
      jsonresult = waeqr.JsonResult()

      return jsonresult

   @staticmethod
   def phase_shift(quantum_bit, phi):
      v_0 = quantum_bit.v_0
      v_1 = quantum_bit.v_1
      print "phase shift check"
      server = 'http://api.wolframalpha.com/v1/query.jsp'
      appid = 'XWQ95Q-4Y54GGJEGR'
      input = '{' + str(v_0)  + ',' + str(v_1) + '}'
      input += '*{{1,0},{0, exp(i*(' + str(phi) + '))}}'

      waeo = wap.WolframAlphaEngine(appid, server)
      query = waeo.CreateQuery(input)
      result = waeo.PerformQuery(query)
      waeqr = wap.WolframAlphaQueryResult(result)
      jsonresult = waeqr.JsonResult()

      return jsonresult

   @staticmethod
   def read(quantum_bit):
      return quantum_bit.read_state()

