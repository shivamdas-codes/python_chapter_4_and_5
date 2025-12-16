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



# # BREAK STATEMENT()
# password = "shiv@shre33"
# while True:
#     userinput = input("enter the password:")
#     if userinput == password:
#         print("LOGIN SUCCESFULLY\nWELCOME BUDDY")
#         if userinput != password:
#             print("NO PROBLEM\nTRY AGAIN")
#         break
#     else:
#         print("STILL HOW MANY ATTEMPTS YOU WANT TO TRY \nDO ONE THING GO AND STUDY")


# # CONTINUE STATEMENT():
# i = 0
# while i <= 5:
#     if i == 3:
#         i += 1
#         continue    # when i=3 the loop will skip that value and continue the loop
#     # basically when the value meets the condition it will not print that value and continue the loop 
#     print(i)
#     i += 1




# # (2).FOR LOOP():
# LIST = [1,2,3,4]
# for i in LIST:  # each item of the list will be printed in a new line
#     print(i)

# name = "shivam"
# for i in name:  # each letter will be printed in a new line
#     print(i)

# # for loop with else statement:
# list = [1,2,3,4,5]
# for i in list:
#     print(i)
# else:
#     print("loop ended") #in this case after the loop ends the else statement will be executed which is not necessary


# # for loop with break statement:
# name = "shivam das"
# for i in name:
#     if i == "a":
#         print("found")
#         break
#     print(i)
# else:
#     print("not found")

# # for loop with continue statement:
# name = "shivam das"
# count = 0
# for i in name:
#     if i == "a":
#         count += 1
#         print("count is:",count)


# RANGE FUNCTION(): this is only used in for loop
for i in range(10): #this is the stoping point
    print(i)

for i in range(1,5):  # this is the starting and stopping point
    print(i)

for i  in range(1,11,2): # this is the starting, stopping and incrementing point (here 2 is the incrementing value)
    print(i)