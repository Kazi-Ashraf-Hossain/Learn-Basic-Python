# Positional Arguments

def person_details(name, age, country='Bangladesh'):
    print(name, age, country, sep='|')

person_details('Khan', '20', 'Bangladesh')

# Keyword Arguments
person_details(name='Abul', age=40, country='SA')

person_details('Alam', 30)



# Return value

def square(num):
    return num * num

print(square(2), square(2.2), sep='|')

def get_name(fName, lName):
    return fName +" "+ lName

print(get_name('Kazi', 'Hossain'))



# Optional Argument
