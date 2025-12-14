# # (1).WHILE LOOP:

# # while True:
# #     print("hello")  
# """in this case the loop never stop at any point because the givenh value is always 'true'
# if we want to stop loop at any point then the value should contain false at any point."""

# while True:
#     print("hello world")
#     break
# # this is the correct format to stop any infinite loop by using 'break' statement.



# i = 1       # variable/iterator 'i' is assigned by 1
# while i <= 5:   #loop performed till <=5
#     print("hello")
#     i += 1      #every time the loop takes place it will increase by "1" till 5
#     print(i)    #this indicates how many times the loop has occured


# j = 1
# while j <= 100:
#     print("hello world", j) # the 'j' represent that how many times the hello world will print
#     j += 1
#     print(j)    # this represent how many times the loops has occured



# #DOUBT PROBLEM (1):
# students_marks = 10
# i = students_marks # we can able to change the variable to the new variable name. 
# while i <= 48:
#     print("need to improve", i)
#     i += 2
# students_marks = i # changed to the original name.
# del i   # 'i' was deleted and no longer used in this code it is for temporary purpose.
# print(students_marks)

# #DOUBT PROBLEM (2): IMP FORMAT(HOW BOOLEAN VALUES WORK IN LOOP)
# x = [True, True, (True+1)*4] # x = 10
# y = False*3 + 1 # y = 1
# # we know that in boolean "TRUE = 1" and "FALSE = 0"
# for i in range(y + sum(x) - 9): #i is the variable here, the range(2)
#     print(sum(x)+i) #though we know that the range is 2 we have to find the i value 2 times which is (10,11)



# i = 1   # loop started 
# while i <= 500: # loop will continue till assigned value and stopes when it reaches 'assigned value/false'
#     print(i)
#     i += 1
# print("loop ended")



# BREAK STATEMENT()
password = "shiv@shre33"
while True:
    userinput = input("enter the password:")
    if userinput == password:
        print("LOGIN SUCCESFULLY\nWELCOME BUDDY")
        if userinput != password:
            print("NO PROBLEM\nTRY AGAIN")
        break
    else:
        print("STILL HOW MANY ATTEMPTS YOU WANT TO TRY \nDO ONE THING GO AND STUDY")

