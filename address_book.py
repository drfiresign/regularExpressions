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
print(re.findall(r'\w*, \w+', data))
