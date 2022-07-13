# print the List in order without using L.sort
def bubblesort(List):
    y = len(List)
    for i in range(y - 1):
        for a in range(0, y-i-1):
            if List[a] > List[a+1]:
                swapped = True
                List[a], List[a + 1] = List[a + 1], List[a]
        if not swapped:
            return
List = [1, 3, 2, 4, 6, 8, 15, 5]
bubblesort(List)
for i in range (len(List)):
    print("% d"% List[i], end=" ")




