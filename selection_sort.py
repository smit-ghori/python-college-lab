l1 = [3, 4, 5, 21, 43, 12]

for i in range(len(l1)):
    max_index = i
    for j in range(i, len(l1)):
        if l1[j] < l1[max_index]:
            max_index = j
    l1[max_index], l1[i] = l1[i], l1[max_index]

print(l1)
