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


