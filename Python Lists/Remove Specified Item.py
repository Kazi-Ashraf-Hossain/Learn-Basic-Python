thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")  # Specific word dhore
print(thislist)

thisslist = ["apple", "banana", "cherry", "banana", "kiwi"]
thisslist.remove("banana")  # Same word multiple thakle index er first ta remove korbe
print(thisslist)

# Remove Specified Index -----
# ---If you do not specify the index, the pop() method removes the last item.
list = ["apple", "banana", "cherry"]
list.pop(1)  # index e 1 value remove kore dibe
print(list)

# --The del keyword also removes the specified index:
itemlist = ["apple", "banana", "cherry"]
del itemlist[0]
print(itemlist)

# --The del keyword can also delete the list completely
itemslist = ["apple", "banana", "cherry"]
del itemslist

# -----Clear the List
thelist = ["apple", "banana", "cherry"]
thelist.clear()
print(thelist)
