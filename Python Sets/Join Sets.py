#-- UNION

set0 = {"a", "b", "c"}
set1 = {1, 2, 3}

set3 = set0.union(set1)
print(set3)

#-- Join Multiple Sets
set2 = {"a", "b", "c"}
set3 = {1, 2, 3}
set4 = {"John", "Elena"}
set5 = {"apple", "bananas", "cherry"}

myset = set2.union(set3, set4, set5)
print(myset)


#--- Update
set11 = {"a", "b" , "c"}
set22 = {1, 2, 3}

set11.update(set22)
print(set11)


#-----------Intersection

setA = {"apple", "banana", "cherry"}
setB = {"google", "microsoft", "apple"}

setC = setA.intersection(setB)
print(setC)