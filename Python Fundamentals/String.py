print("Hello Python String")

print("Are You 'OK' ")

print('Everything is "Fine" ')

# Assign String to a Variable

a = "Hello Python String"
print(a)

# Multiline Strings

b = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(b)

# Strings are Arrays

d = "Hello, World!"
print(d[1])
print()
# Looping Through a String
for x in "banana":
    print(x)

# String Length

e = "Banana"
print(len(e))

# Check String
txt = "The best things in life are free!"
print("free" in txt)

# Use it in an if statement:
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

# Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)

print("Not Present ")
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
