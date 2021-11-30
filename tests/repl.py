from mql import MQLParser
import pprint

p = MQLParser(debug=False)

def query(query):
	result = p.parse(query)
	pprint.pprint(result)

while True:
	q = input("MQL> ")
	query("{};".format(q))