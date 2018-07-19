from bql import BQLParser
import pprint

p = BQLParser(debug=False)

def query(query):
	result = p.parse(query)
	pprint.pprint(result)

while True:
	q = input("BQL> ")
	query("{};".format(q))