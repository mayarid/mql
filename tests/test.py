from mql import MQLParser
import pprint

p = MQLParser(debug=False)
filename = "test.mql"
result = p.parse(open(filename).read())
pprint.pprint(result)