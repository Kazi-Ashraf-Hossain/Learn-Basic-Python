# Append Items ------

list = ["apple", "banana", "cherry"]
list.append("orange")  # append = arry r ses e value add korbe
print(list)

# Insert -------

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")  # koto number e index e value dhukbe seta mention kora
print(thislist)

# Extend List ---

itemslist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
itemslist.extend(tropical)  # First list er sathe
print(itemslist)

# Add Any Iterable ------
thisslist = ["apple", "papaya", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thisslist.extend(thistuple)
print(thisslist)
