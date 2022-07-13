#1a. Write a python programm to print how many Prime Numbers between 2 numbers
# not using else in this program
# amount = 0
# prime =  True
# for num in range(1,10):
#     for i in range(2,num):
#         if (num%i==0):
#             prime = False
#             break
#     if (prime):
#         print(num)
#         amount = amount + 1
#     prime = True
# print(amount)


# using else
amount = 0
for num in range(1,10):
    for i in range(2,num):
        if (num%i==0):
            prime = False
            break
    else:

        print(num)
        amount = amount + 1
print(amount)


