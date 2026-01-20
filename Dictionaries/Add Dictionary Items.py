thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

# ---Update Dictionary
thedict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thedict.update({"color": "red"})
thedict.update({"Country": "Franc"})
print(thedict)