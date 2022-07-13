# 1/ Write the python program to print prime numbes between 2 numbers
def prime(n,x):
    prime_list = []
    for y in range(n,x):
        if y == 0 or y == 1:
            continue
        else:
            for a in range(2, int(y/2)+1):
                if y % a == 0:
                    break
            else:
                prime_list.append(y)
    return prime_list
start_range = 2
end_range = 20
num = prime(start_range, end_range)
if len(num) == 0:
    print("There are no prime numbers in this range")
else:
    print("The prime numbers in this range are:", num)
