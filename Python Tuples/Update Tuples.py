# --  Change Tuple Values

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)


# --Add Items

thetuple = ("Car", "Bus", "Micro")
y = list(thetuple)
y.append("kiwi")
thetuple = tuple(y)
print(y)