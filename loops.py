# while True:
#     print("hello")  
"""in this case the loop never stop at any point because the givenh value is always 'true'
if we want to stop loop at any point then the value should contain false at any point."""


i = 1       # variable/iterator 'i' is assigned by 1
while i <= 5:   #loop performed till <=5
    print("hello")
    i += 1      #every time the loop takes place it will increase by "1" till 5
    print(i)    #this indicates how many times the loop has occured


j = 1
while j <= 100:
    print("hello world", j) # the 'j' represent that how many times the hello world will print
    j += 1
    print(j)    # this represent how many times the loops has occured



#DOUBT PROBLEM:
students_marks = 10
i = students_marks # we can able to change the variable to the new variable name. 
while i <= 48:
    print("need to improve", i)
    i += 2
students_marks = i # changed to the original name.
del i   # 'i' was deleted and no longer used in this code it is for temporary purpose.
print(students_marks)
