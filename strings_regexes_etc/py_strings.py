# string methods and foirnmatting in py

# upper , lower method

spam = "Hello World"

print(spam.upper())

print(spam.lower())

#check boolean values
#only letters
print(spam.isalpha())
#letters and numbers
print(spam.isalnum())
#numbers
print(spam.isdecimal())
#only whitespace
print(spam.isspace())
#only titlecas
print(spam.istitle())

# starts and ends wtih

print(spam.startswith("Hello"))

print(spam.endswith("World")) 


print(' '.join(['cats', 'rats', 'bats']))

#.split() command does the reverse

shortstr = "My-name-is-Stas"
print(shortstr.split("-"))

# adjust string length with white spaces -> rjust and ljust and center method

spam2 = "Stephan is poor"
print(spam2.rjust(20))

print(spam2.center(20, '='))

#remove character from strom string
#replace with .replace('','')
print(spam2.replace('poor', 'gay'))

a ="  x  "
print(a.strip())
print(a.rstrip())
print(a.lstrip())


#### string formating ####

name = "Alcie"

place ="Main Street"

time ="6pm"

food="pussy"

print('Hello %s, you are invited to a party at %s at %s. Please bring some %s.' % (name, place, time, food))

