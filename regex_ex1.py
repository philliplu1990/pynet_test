import re

f = open("show_int_fa4.txt")
output = f.read()
print output

match = re.search(r'^.*\s+(.*)\spackets input.*?\s(.*?)\sbytes.*\s(.*)\spackets output.*?\s(.*?)\sbytes', output, flags=re.DOTALL)
print match
print 'packets input ' + match.group(1)
print 'packets output ' + match.group(3)
print 'bytes input ' + match.group(2)
print 'bytes output ' + match.group(4)
