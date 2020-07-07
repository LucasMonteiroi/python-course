import re

# \d means digit, then search the pattern 3 digits - 3 digits - 4 digits
# We used raw string r'' because has many \ to make a pattern
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# The findall method will find all patterns with configured in phoneNumRegex
print(phoneNumRegex.findall('Call me 415-555-1011 tomorrow, or at 455-555-9991'))
# The search method will find the first pattern with configured in phoneNumRegex
mo = phoneNumRegex.search('Call me 415-555-1011 tomorrow, or at 455-555-9991')
# The group, will group the first result to print
print(mo.group())

# Now a pattern to Brazilian phone
brlPhoneRegex = re.compile(r'\d\d\s\d\d\d\d\d-\d\d\d\d')
number = brlPhoneRegex.search('Call me to talk about the study 11 94883-7234')
print(number.group())

# We have a group and pipe regex
newNumRegex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mobile = newNumRegex.search('Call me in (415) 555-1010')
print(mobile.group())

# Search an pattern or other
batRegex = re.compile(r'(Bat|bat)(man|mobile|copter|movel)')
bat = batRegex.search('The Batmovel lost a wheel')
print(bat.group())

bat = batRegex.search('The batmobile lost the signal')
print(bat.group())