import re

input = 'happening, hed, ring, heated'

out = re.sub('ing|ed', ':)', input)

print(out)