import re

names_file = open("names.txt")
data = names_file.read()
names_file.close()

# last_name = r'Love'
# first_name = r'Kenneth'

# print(re.match(last_name, data))
# print(re.search(first_name, data))
# print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data))
# print(re.findall(r'\w*, \w+', data))
# FINDING EMAILS:
# print(re.findall(r'[-\w\d+.]+@[-\w\d.]+', data))
# print(re.findall(r'\b[trehous]{9}\b', data, re.I))

# NEGATING .GOV MAILS:
# print(re.findall(r'''
#     \b@[-\w\d.]*
#     [^gov\t]+
#     \b
# ''', data, re.VERBOSE|re.I))

# print(re.findall(r'''
#     \b[-\w]*,
#     \s
#     [-\w ]+
#     [^\t\n]
#     ''', data, re.X))

#GROUPS
line = re.search(r'''
    ^(?P<name>[-\w ]*,\s[-\w ]+)\t #last & first names
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t #email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t #phone
    (?P<job>[\w\s]+,\s[\w\s.]+)\t? #job and company
    (?P<twitter>@[\w\d]+)?$ #twitter
''', data, re.X|re.M)

# print(line)
print(line.groupdict())

# line = re.compile(r'''
#     ^(?P<name>(?P<last>[-\w ]*),\s(?P<first>[-\w ]+))\t  # Last and first names
#     (?P<email>[-\w\d.+]+@[-\w\d.]+)\t  # Email
#     (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t  # Phone
#     (?P<job>[\w\s]+,\s[\w\s.]+)\t?  # Job and company
#     (?P<twitter>@[\w\d]+)?$  # Twitter
# ''', re.X|re.M)








