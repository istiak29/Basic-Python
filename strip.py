'''
rstrip() remove the first and the last extra white space of a string.
Whitespace is a nonprintabel character. white space is a character until you mention that.
'''

name_b = ' Istiak '
print(name_b.rstrip())

'''
You can also remove only the left and only the right side.
For only left side you should use .lstrip() 
and only for right side you have to use .strip()
'''

name_l = ' Istiak '
print(name_l.lstrip())

name_r = ' Istiak '
print(name_r.strip())