import requests
default_url = "http://whatever_change_this"
# function should look something like /dog

def send_request(payload, function):
	r = requests.get(default_url + function, params=payload)
	return r.text	# returns response