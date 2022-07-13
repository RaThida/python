# 1. Write a python program to print Prime numbers betweens 2 numbers
amount = 0
for num in range(1,10):
    if all (num %i!=0 for i in range(2,num)):
        #print(num)
        amount = 1 + amount
print(amount)