from qubit import *
import wap 
import urllib
import json

class Gate:

   @staticmethod
   def qubit_init(quantum_bit):
      v_0 = quantum_bit.v_0
      v_1 = quantum_bit.v_1
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
      server = 'http://api.wolframalpha.com/v1/query.jsp'
      appid = 'XWQ95Q-4Y54GGJEGR'
      hadamard = '{{1,1},{1,-1}}/(sqrt(2))'
      input = '{' + str(v_0)  + ',' + str(v_1) + '}'
      input += '*' + hadamard
      link_set = ""

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
      
      link_set += src + " "      

      input = hadamard
      
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
      
      link_set += src + " "

      queryStr = waeo.CreateQuery(input)
      wap.WolframAlphaQuery(queryStr, appid)
      result = waeo.PerformQuery(queryStr)
      result = wap.WolframAlphaQueryResult(result)

      for pod in result.Pods():
         waPod = wap.Pod(pod)
         if waPod.Title()[0] == "Matrix plot":
            for subpod in waPod.Subpods():
               waSubpod = wap.Subpod(subpod)
               plaintext = waSubpod.Plaintext()[0]
               img = waSubpod.Img()
               src = wap.scanbranches(img[0], 'src')[0]
      
      link_set += src

      return link_set

   @staticmethod
   def pauli_x(quantum_bit):
      v_0 = quantum_bit.v_0
      v_1 = quantum_bit.v_1
      server = 'http://api.wolframalpha.com/v1/query.jsp'
      appid = 'XWQ95Q-4Y54GGJEGR'
      pauli_x = '{{0,1},{1,0}}'
      input = '{' + str(v_0)  + ',' + str(v_1) + '}'
      input += '*' + pauli_x
      link_set = ""

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
      
      link_set += src + " "      

      input = pauli_x
      
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
      
      link_set += src + " "

      queryStr = waeo.CreateQuery(input)
      wap.WolframAlphaQuery(queryStr, appid)
      result = waeo.PerformQuery(queryStr)
      result = wap.WolframAlphaQueryResult(result)

      for pod in result.Pods():
         waPod = wap.Pod(pod)
         if waPod.Title()[0] == "Matrix plot":
            for subpod in waPod.Subpods():
               waSubpod = wap.Subpod(subpod)
               plaintext = waSubpod.Plaintext()[0]
               img = waSubpod.Img()
               src = wap.scanbranches(img[0], 'src')[0]
      
      link_set += src

      return link_set   
   
   @staticmethod
   def pauli_y(quantum_bit):
      v_0 = quantum_bit.v_0
      v_1 = quantum_bit.v_1
      server = 'http://api.wolframalpha.com/v1/query.jsp'
      appid = 'XWQ95Q-4Y54GGJEGR'
      pauli_y = '{{0,-i},{i,0}}'
      input = '{' + str(v_0)  + ',' + str(v_1) + '}'
      input += '*' + pauli_y
      link_set = ""
      
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
      
      link_set += src + " "      

      input = pauli_y
      
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
      
      link_set += src + " "

      queryStr = waeo.CreateQuery(input)
      wap.WolframAlphaQuery(queryStr, appid)
      result = waeo.PerformQuery(queryStr)
      result = wap.WolframAlphaQueryResult(result)

      for pod in result.Pods():
         waPod = wap.Pod(pod)
         if waPod.Title()[0] == "Matrix plot":
            for subpod in waPod.Subpods():
               waSubpod = wap.Subpod(subpod)
               plaintext = waSubpod.Plaintext()[0]
               img = waSubpod.Img()
               src = wap.scanbranches(img[0], 'src')[0]
      
      link_set += src

      return link_set  

   @staticmethod
   def pauli_z(quantum_bit):
      v_0 = quantum_bit.v_0
      v_1 = quantum_bit.v_1
      server = 'http://api.wolframalpha.com/v1/query.jsp'
      appid = 'XWQ95Q-4Y54GGJEGR'
      pauli_z = '{{1,0},{0,-1}}'
      input = '{' + str(v_0)  + ',' + str(v_1) + '}'
      input += '*' + pauli_z
      link_set = ""
      
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
      
      link_set += src + " "      

      input = pauli_z
      
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
      
      link_set += src + " "

      queryStr = waeo.CreateQuery(input)
      wap.WolframAlphaQuery(queryStr, appid)
      result = waeo.PerformQuery(queryStr)
      result = wap.WolframAlphaQueryResult(result)

      for pod in result.Pods():
         waPod = wap.Pod(pod)
         if waPod.Title()[0] == "Matrix plot":
            for subpod in waPod.Subpods():
               waSubpod = wap.Subpod(subpod)
               plaintext = waSubpod.Plaintext()[0]
               img = waSubpod.Img()
               src = wap.scanbranches(img[0], 'src')[0]
      
      link_set += src

      return link_set   

   @staticmethod
   def phase_shift(quantum_bit, phi):
      v_0 = quantum_bit.v_0
      v_1 = quantum_bit.v_1
      server = 'http://api.wolframalpha.com/v1/query.jsp'
      appid = 'XWQ95Q-4Y54GGJEGR'
      p_shift = '{{1,0},{0, exp(i*(' + str(phi) + '))}}'
      input = '{' + str(v_0)  + ',' + str(v_1) + '}'
      input += '*' + p_shift
      link_set = ""

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
      
      link_set += src + " "      

      input = p_shift
      
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
      
      link_set += src + " "

      queryStr = waeo.CreateQuery(input)
      wap.WolframAlphaQuery(queryStr, appid)
      result = waeo.PerformQuery(queryStr)
      result = wap.WolframAlphaQueryResult(result)

      for pod in result.Pods():
         waPod = wap.Pod(pod)
         if waPod.Title()[0] == "Matrix plot":
            for subpod in waPod.Subpods():
               waSubpod = wap.Subpod(subpod)
               plaintext = waSubpod.Plaintext()[0]
               img = waSubpod.Img()
               src = wap.scanbranches(img[0], 'src')[0]
      
      link_set += src

      return link_set   

   @staticmethod
   def read(quantum_bit):
      state = quantum_bit.read_state()
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

