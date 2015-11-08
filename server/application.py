import os
import tornado.web
import socket
import urlparse    

ip_id = []	# array of ip addresses

class BaseHandler(tornado.web.RequestHandler):
	def set_default_headers(self):
		def db(self):
			return self.application.db

		# Get the current session from the db
		self.set_header("Access-Control-Allow-Origin", "http://nick11roberts.github.io/qCloud/")
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


# This is a test for hello world
class HelloHandler(BaseHandler):
	def get(self):
		try:
			self.write("Current session is %s" % str(self.get_current_session()))
		except:
			print("Hello failed")
			raise
	def post(self):
		try:
			stuff = self.get_argument('stuff', '')
			self.write("you sent me: " + stuff)
		except:
			raise
			self.write("something horrible happened")


class Application(tornado.web.Application):
	def __init__(self):
		handlers = [
			(r"/",			HelloHandler),
			(r"/hello",		HelloHandler),

		]
		tornado.web.Application.__init__(self, handlers)
