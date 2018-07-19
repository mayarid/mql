from bql import BQLParser
import pprint

p = BQLParser(debug=False)
filename = "test.bql"
result = p.parse(open(filename).read())
pprint.pprint(result)