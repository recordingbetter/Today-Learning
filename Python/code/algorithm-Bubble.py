

def bubble_sort(l):
    i = 0
    l_len = len(l)
    for j in range(l_len-1):
        for i in range(l_len - 1 - j):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
    return l

list1 = [5, 6, 9, 3, 4, 6, 1, 2]
print(bubble_sort(list1))

list2 = [45, 87, 12, 3, 4, 8, 89, 4, 43]
print(bubble_sort(list2))