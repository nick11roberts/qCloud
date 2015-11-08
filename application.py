import os
import tornado.web
import socket
import urlparse    
import sys
sys.path.append("server") 
from token import *
import token
import interpreter
from interpreter import *
import qubit
import gate
from qubit import *
from gate import *

ip_id = []	# array of ip addresses

class BaseHandler(tornado.web.RequestHandler):
	def set_default_headers(self):
		def db(self):
			return self.application.db

		# Get the current session from the db
		self.set_header("Access-Control-Allow-Origin", "http://nick11roberts.github.io")

	def get_current_session(self):
		global ip_id

		hostname = urlparse.urlparse("%s://%s"
		    % (self.request.protocol, self.request.host)).hostname
		ip_address = socket.gethostbyname(hostname)

		try: 
			ip = ip_id.index(ip_address)
		except ValueError:
			print "Creating new session"
			ip_id = ip_id + [ip_address]

		print "Current session is " + str(ip_id.index(ip_address))
		return ip_id.index(ip_address)
curr_session = Interpreter()

# This is a test for hello world
class HelloHandler(BaseHandler):
	def get(self):
		try:
			self.write("Current session is %s" % str(self.get_current_session()))
		except:
			print("Hello failed")
			raise
	def post(self):
		global curr_session
		try:
			data = self.request.body
			# print data
			# print data == "qubit yes"
			if data:

				if (data[0] == '"' and data[-1] == '"'):
					data = data[1:-1]
				# print data
				# print data == "qubit yes"
				result = curr_session.add(data)
				self.write(str(result))
			else:
				self.write("No data received")
				return
		except:
			raise
			self.write("something horrible happened")

		return result


class Application(tornado.web.Application):
	def __init__(self):
		handlers = [
			(r"/",			HelloHandler),
			(r"/hello",		HelloHandler),

		]
		tornado.web.Application.__init__(self, handlers)
