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
# line = re.search(r'''
#     ^(?P<name>[-\w ]*,\s[-\w ]+)\t #last & first names
#     (?P<email>[-\w\d.+]+@[-\w\d.]+)\t #email
#     (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t #phone
#     (?P<job>[\w\s]+,\s[\w\s.]+)\t? #job and company
#     (?P<twitter>@[\w\d]+)?$ #twitter
# ''', data, re.X|re.M)
# print(line)
# print(line.groupdict())

# sample
# string = 'Perotto, Pier Giorgio'
# names = re.match(r'''
#     ^(?P<firstname>[\w]*),\s #first name
#     (?P<lastname>[\w\s\w]*)$ #last name
# ''', string, re.X)

# string = '''Love, Kenneth, kenneth+challenge@teamtreehouse.com, 555-555-5555, @kennethlove
# Chalkley, Andrew, andrew@teamtreehouse.co.uk, 555-555-5556, @chalkers
# McFarland, Dave, dave.mcfarland@teamtreehouse.com, 555-555-5557, @davemcfarland
# Kesten, Joy, joy@teamtreehouse.com, 555-555-5558, @joykesten'''

# contacts = re.search(r'''
#     (?P<email>[-\w\d.+]+@[-\w\d.]+),\s #email
#     (?P<phone>\d{3}-\d{3}-\d{4}) #phone
# ''', string, re.X|re.M)

# create a twitters variable
# twitters = re.search(r'''
#     (?P<twitter>@[\w\d]+)$ #twitter
# ''', string, re.X|re.M)

#COMPILING AND LOOPS
# line = re.compile(r'''
#     ^(?P<name>(?P<last>[-\w ]*),\s(?P<first>[-\w ]+))\t #last & first names
#     (?P<email>[-\w\d.+]+@[-\w\d.]+)\t #email
#     (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t #phone
#     (?P<job>[\w\s]+,\s[\w\s.]+)\t? #job and company
#     (?P<twitter>@[\w\d]+)?$ #twitter
# ''', re.X|re.M)

# # print(re.search(line, data).groupdict())
# # print(line.search(data).groupdict())

# for match in line.finditer(data):
#     # print(match.group('name'))
#     print('{first} {last} <{email}>'.format(**match.groupdict()))

##### create a variable players
# string = '''Love, Kenneth: 20
# Chalkley, Andrew: 25
# McFarland, Dave: 10
# Kesten, Joy: 22
# Stewart Pinchback, Pinckney Benton: 18'''
# players = re.search(r'(?P<last_name>[\w ]+),\s(?P<first_name>[\w ]+):\s(?P<score>[\d]+)', string, re.M)

#*****create a class named Player that has those same three attributes, last_name, first_name, and score. I should be able to set them through __init__

class Player:

    def __init__(self, last_name, first_name, score):
        self.last_name = last_name
        self.first_name = first_name
        self.score = score




