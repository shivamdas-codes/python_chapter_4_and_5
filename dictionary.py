# example: 1
dict = {
    "name" : "shivam das",                     # "KEY" is "STRING" and the "KEYVALUE" is "STRING"
    "age" : 21,                                # "KEY" is "STRING" and the "KEYVALUE" is "INTEGER"
    "marks" : 99.0,                            # "KEY" is "STRING" and the "KEYVALUE" is "FLOAT"
    "is_adult" : True,                         # "KEY" is "STRING" and the "KEYVALUE" is "BOOLEAN"
    "subjects" : ["python", "C", "java"],      # "KEY" is "STRING" and the "KEYVALUE" is "LIST"
    "topics" : ("dictionary", "sets"),         # "KEY" is "STRING" and the "KEYVALUE" is "TUPLE"
# in the dictionary the "keys" also can be written in the form of str(), int(), boolean() and tuple()
    }

print(dict["name"],dict["age"],dict["subjects"])
# if we want to print any particular value in the dictionary we can use   "print(dict["key"])"

dict["name"] = "shreya",
# if we want to replace any value we can use this   "dict["name"] = 'new value'"

dict["sur_name: "] = "das"
# if we want tp assign a new key and a new keyvalue we can use   "dict["newkey"] = 'new keyvalue'"

print(type(dict))
print(len(dict))
print(dict)



# example: 2
#  NESTED DICTIONARY
students = {
    "name" : "shivam",
    "subjects" : ["maths", "english", "science", "social"],
    "marks" : {
        "maths" : 99,
        "english" : 99,
        "science" : 99,
        "social" : 99,
    }
}
print(students)
# the above code represents "NESTED DICTIONARY", which means dictionary inside dictionary. 

print(students["marks"]["english"])
# if we want to print the dictionary which is present inside the dictionary then we can use this and we can also print the value which is inside the dictionary as well.



# METHODS IN DICTIONARY
# (1). keys()
