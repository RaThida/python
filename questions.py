# 3. writing sort function without using the list.sort function
initial_list = [12, 21, 13, 2, 42, 34, 23]
new_list = []
while initial_list:
    minimum = initial_list[0]
    for i in initial_list:
        if minimum > 1:
            minimum = i
# new_list.insert(0, minimum)
    new_list.append(minimum)
    initial_list.remove(minimum)
print(new_list)

