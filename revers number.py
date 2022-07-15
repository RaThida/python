# num = 5642
# def reverse(num):
#     rev= 0
#     while num> 0:
#        rem = num %10
#        rev = (10*rev) + rem
#        num = num//10
#     return rev

# Num = 5642
# rev_num = 0
# while Num > 0:
#     rev_num = rev_num * 10 + Num%10
#     Num = Num//10
# print('reverse integer number: ', rev_num)



# write a python program to check whether an integer number is a palindrome or not

# number = int(input('integer number: '))
# temp = number;
# print(number)
# reverse = 0
# while number >0:
#     reverse = reverse * 10 + number%10
#     number = number  //10
# print('reverse integer number: ', reverse)
# if (reverse == temp):
#     print('True')
# else:
#     print('False')


#18. python program to check number representation is in binary 
dec = int(input('decimal number: '))
while dec !=0:
    remainder = dec %2
    if (remainder !=0 and remainder !=1):
        print('number is not in binary representation')
        break
    dec = dec //2
    print(dec %2, end='')
    
    if (dec == 0):
        print(' number is in binary representation!')
        
    

    


    













    



