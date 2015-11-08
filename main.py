import os
import tornado.httpserver
import tornado.ioloop
import tornado.web
import application

def main():
	# start the web app

	try:
		port = int(os.environ.get("PORT", 5000))
	except:
		port = 8000

	print "Running on port " + str(port)

	app = application.Application()
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(port)

	print"running"
	tornado.ioloop.IOLoop.instance().start();

if __name__ == "__main__":
	main()