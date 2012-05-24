from hashlib import new
import json

HASH_FUNCTION = 'sha1' # was md5

def make(string):
	'''
	Create a hash of a string.

	>>> make("Sample string")
	'e9a47e5417686cf0ac5c8ad9ee90ba2c1d08cc14'
	'''
	return new(HASH_FUNCTION, string).hexdigest()

def make6(string):
	return maken(string, 6)

def maken(string, n):
	return make(string)[:n]

def strict(obj):
	''' Convert an object into a strict JSON string '''
	t = type(obj)
	if t==bool or obj==None or t==str or t==int or t==unicode:
		return json.dumps(obj)
	if t==list or t==tuple:
		return "[%s]" % ",".join([strict(x) for x in obj])
	if t==dict:
		strdict = {}
		for key in obj:
			strdict[str(key)] = obj[key]
		keys = strdict.keys()
		keys.sort()
		return "{%s}" % ",".join([strict(key)+":"+strict(strdict[key]) for key in keys])
	else:
		raise TypeError("Not JSONable: "+str(t))

def strictify(jsonstring):
	''' Make a JSON string strict '''
	return strict(json.loads(jsonstring))

def checksum(obj):
	''' Get the checksum of the strict of an object '''
	return make(strict(obj))

def key(string):
	if len(string)>10:
		return string[:10]+make6(string[10:])
	else:
		return string