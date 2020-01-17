import re

pattern = re.compile('^world')
value = 'world, hello something'
print(re.search(pattern, value))

pattern = re.compile('^\w\w\w$')

print(re.search(pattern, 'abF'))
print(re.search(pattern, 'sldkfjsdf'))

pattern = re.compile('\d\d\d\w')
print(re.search(pattern, 'Hello 2345645'))


pattern = re.compile('^\d{4}$')
print(re.search(pattern, '1234'))
print(re.search(pattern, '12345'))

pattern = re.compile('^\d{4,10}$')
print(re.search(pattern, '123'))

pattern = re.compile('^\d{4,}$')
print(re.search(pattern, '12345567654654'))


pattern = re.compile('^\d{,}$')
print(re.search(pattern, '12'))

# 1 dd.mm.yyyy



# 2 +7999999-00-00 - ok
#   +89999992323 - fail

pattern = re.compile('\7-?\d{3}-?\d{3}-?\d{2}-?\d{2}')


# 3 4et ne4et
pattern = re.compile('[02468]$')