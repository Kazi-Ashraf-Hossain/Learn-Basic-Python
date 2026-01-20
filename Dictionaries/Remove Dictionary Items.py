thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "Country": "Switzerland"
}
thisdict.pop("model")
print(thisdict)

del thisdict["year"]  # -- The del keyword removes the item with the specified key
print(thisdict)


# --  clear() method empties the dictionary
thedict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thedict.clear()
print(thedict)