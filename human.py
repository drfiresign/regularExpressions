import re

names_file = open("names.txt", encoding="utf-8")
data = names_file.read()
names_file.close()

line = re.compile(r'''
    ^(?P<name>(?P<last>[-\w ]*), \s(?P<first>[-\w ]+))\t  # last and first name
    (?P<email>[-\w\d.+]+@[-\w\d.]+)\t  # email
    (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t  # phone numbers
    (?P<job>[\w\s]+,\s[\w\s.]+)\t?  # job and company
    (?P<twitter>@[\w\d]+)?$  # twitter
''', re.X | re.M)


class Person:
    last = "None"
    first = "None"
    email = "None"
    phone = "None"
    job = "None"
    twitter = "None"

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return """First Name: {}
Last Name: {}
Email: {}
Phone: {}
Job Title: {}
Twitter: {}""".format(self.first, self.last, self.email, self.phone, self.job,
                      self.twitter)


class Human(Person):
    last = line.search(data).group("last")
    first = line.search(data).group("first")
    email = line.search(data).group("email")
    phone = line.search(data).group("phone")
    job = line.search(data).group("job")
    twitter = line.search(data).group("twitter")


jeff = Human()

print(jeff)
