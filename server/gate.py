from qubit import *
import wap 
import urllib
import json

class Gate:

   @staticmethod
   def qubit_init(quantum_bit):
      v_0 = quantum_bit.v_0
      v_1 = quantum_bit.v_1
      print "hadamard check"
      server = 'http://api.wolframalpha.com/v1/query.jsp'
      appid = 'XWQ95Q-4Y54GGJEGR'
      input = 'vector {' + str(v_0)  + ',' + str(v_1) + '}'

      waeo = wap.WolframAlphaEngine(appid, server)

      queryStr = waeo.CreateQuery(input)
      wap.WolframAlphaQuery(queryStr, appid)
      result = waeo.PerformQuery(queryStr)
      result = wap.WolframAlphaQueryResult(result)

      for pod in result.Pods():
         waPod = wap.Pod(pod)
         if waPod.Title()[0] == "Result":
            for subpod in waPod.Subpods():
               waSubpod = wap.Subpod(subpod)
               plaintext = waSubpod.Plaintext()[0]
               img = waSubpod.Img()
               src = wap.scanbranches(img[0], 'src')[0]
         
      return src

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

      queryStr = waeo.CreateQuery(input)
      wap.WolframAlphaQuery(queryStr, appid)
      result = waeo.PerformQuery(queryStr)
      result = wap.WolframAlphaQueryResult(result)

      for pod in result.Pods():
         waPod = wap.Pod(pod)
         if waPod.Title()[0] == "Result":
            for subpod in waPod.Subpods():
               waSubpod = wap.Subpod(subpod)
               plaintext = waSubpod.Plaintext()[0]
               img = waSubpod.Img()
               src = wap.scanbranches(img[0], 'src')[0]
      
      return src   

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

      queryStr = waeo.CreateQuery(input)
      wap.WolframAlphaQuery(queryStr, appid)
      result = waeo.PerformQuery(queryStr)
      result = wap.WolframAlphaQueryResult(result)

      for pod in result.Pods():
         waPod = wap.Pod(pod)
         if waPod.Title()[0] == "Result":
            for subpod in waPod.Subpods():
               waSubpod = wap.Subpod(subpod)
               plaintext = waSubpod.Plaintext()[0]
               img = waSubpod.Img()
               src = wap.scanbranches(img[0], 'src')[0]
      
      return src   
   
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

      queryStr = waeo.CreateQuery(input)
      wap.WolframAlphaQuery(queryStr, appid)
      result = waeo.PerformQuery(queryStr)
      result = wap.WolframAlphaQueryResult(result)

      for pod in result.Pods():
         waPod = wap.Pod(pod)
         if waPod.Title()[0] == "Result":
            for subpod in waPod.Subpods():
               waSubpod = wap.Subpod(subpod)
               plaintext = waSubpod.Plaintext()[0]
               img = waSubpod.Img()
               src = wap.scanbranches(img[0], 'src')[0]
      
      return src  

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

      queryStr = waeo.CreateQuery(input)
      wap.WolframAlphaQuery(queryStr, appid)
      result = waeo.PerformQuery(queryStr)
      result = wap.WolframAlphaQueryResult(result)

      for pod in result.Pods():
         waPod = wap.Pod(pod)
         if waPod.Title()[0] == "Result":
            for subpod in waPod.Subpods():
               waSubpod = wap.Subpod(subpod)
               plaintext = waSubpod.Plaintext()[0]
               img = waSubpod.Img()
               src = wap.scanbranches(img[0], 'src')[0]
      
      return src  

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

      queryStr = waeo.CreateQuery(input)
      wap.WolframAlphaQuery(queryStr, appid)
      result = waeo.PerformQuery(queryStr)
      result = wap.WolframAlphaQueryResult(result)

      for pod in result.Pods():
         waPod = wap.Pod(pod)
         if waPod.Title()[0] == "Result":
            for subpod in waPod.Subpods():
               waSubpod = wap.Subpod(subpod)
               plaintext = waSubpod.Plaintext()[0]
               img = waSubpod.Img()
               src = wap.scanbranches(img[0], 'src')[0]
      
      return src  

   @staticmethod
   def read(quantum_bit):
      state = quantum_bit.read_state()
      print "read check"
      server = 'http://api.wolframalpha.com/v1/query.jsp'
      appid = 'XWQ95Q-4Y54GGJEGR'
      input = str(state)
 
      waeo = wap.WolframAlphaEngine(appid, server)

      queryStr = waeo.CreateQuery(input)
      wap.WolframAlphaQuery(queryStr, appid)
      result = waeo.PerformQuery(queryStr)
      result = wap.WolframAlphaQueryResult(result)

      for pod in result.Pods():
         waPod = wap.Pod(pod)
         if waPod.Title()[0] == "Input":
            for subpod in waPod.Subpods():
               waSubpod = wap.Subpod(subpod)
               plaintext = waSubpod.Plaintext()[0]
               img = waSubpod.Img()
               src = wap.scanbranches(img[0], 'src')[0]
         
      return src

