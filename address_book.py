import re

names_file = open("names.txt", encoding="utf-8")
data = names_file.read()
names_file.close()

# print(data)

last_name = r'Love'
first_name = r'Kenneth'
# print(re.match(last_name, data))
# print(re.search(first_name, data))
# print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data))
# print(re.findall(r'\w*, \w+', data))
# print(re.findall(r'[-\w\d+.]+@[-\w\d.]+', data))
# print(re.findall(r'\b[trehous]{9}\b', data, re.I))

# print(re.findall(r'''
#     \b@[-\w\d.]* #find a word bountry, an @, and any number of characters
#     [^gov\t]+  # ignore 1+ instances of 'g', 'o', or 'v' and a tab.
#     \b  # match another word boundary
# ''', data, re.VERBOSE | re.I))

# print(re.findall(r"""
#     \b[-\w]+,  # find a word boundary, 1+ hyphens or characters, and a comma
#     \s  # find 1 whitespace
#     [-\w ]+  # 1+ hyphens and characters and explicit spaces
#     [^\t\n]  # ignore tabs and new lines
# """, data, re.X))

line = re.search(r'''
    ^(?P<name>[-\w ]*, \s[-\w ]+)\t  # last and first names
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t  # email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t  # phone numbers
    (?P<job>[\w\s]+,\s[\w\s.]+)\t?  # job and company
    (?P<twitter>@[\w\d]+)?$  # twitter
''', data, re.X | re.M)
print(line)
print(line.groupdict())
