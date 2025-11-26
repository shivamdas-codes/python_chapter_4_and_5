set0 = {1,3,5}
print(type(set0)) # type of the set
print(set0)
# the above code represents the set.

set1 = {1,2,3,"hello", "world"} #we can give any value inside set, like int(), str(), float(), boolean() and tuple() because they are immuatble. we cant use list[] and dictionary{} because thay are mutable
print(len(set1)) # lenght of the set
print(set)

set2 = {1,1,2,3,4,3, "hello", "world", "hello"}
print(len(set2)) #the lenght also ignore the duplicate elements and print the unique elements
# though we know that sets are unorder and each element in the set are unique, it doesn't print any duplicate and alwayes takes the first element. 
print(set2)


# empty set():
empty_set = set()
print(type(empty_set))
print(empty_set)
# the above code represents the empty set().



# SET METHODS
# (1). add()
collection = set()
collection.add(1)
collection.add(2)
# this is used to add any new elememnt to the empty set
collection.add(3)
collection.add(3)
collection.add(4)
# if we want to add any duplicate value, it will always take only one of that duplicate
collection.add("hello world") # string
collection.add(("hello", "welcome", "shivam das")) # tuple
# collection.add([1,2,3]).........we cannot add list inside a set as an element
print(collection)

set0 = {1,3,5} # the methods not only applicable for the empty set for also applicable to the set which is already assigned by any values.
set0.add(4)
# set0.add(6,7).....we cant assign multiple values to print.
set0.add("hello world")
print(set0)
# NOTE: IF WE TRY TO PRINT THE VALUE WHICH IS NOT PRESENT IN THE SET IN WILL THROUGH ERROR


# (2). remove()
collection1 = set()
collection1.add(1)
collection1.add(2)
collection1.remove(2) # this method is use to remove the value inside the set
print(collection1)


# (3). clear()
