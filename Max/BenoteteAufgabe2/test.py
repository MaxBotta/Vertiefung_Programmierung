from xbrl import *

file = open("./Novartis/Novartis-2002-11-15.xml", "r")
xbrl_parser = XBRLParser()
xbrl = xbrl_parser.parse(file)

#print(xbrl)

gaap_obj = xbrl_parser.parseGAAP(xbrl, context="year", ignore_errors=0)


dei_obj = xbrl_parser.parseDEI(xbrl)
serializer = DEISerializer()
result = serializer.dump(dei_obj)

print(result.data)
