l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def binary_search(start, end, target):

    if end < start:
        return "Not found"

    mid = (start + end) // 2

    if l1[mid] == target:
        return mid
    elif l1[mid] < target:
        return binary_search(start=mid + 1, end=end, target=target)
    else:
        return binary_search(start=start, end=mid - 1, target=target)


print(binary_search(0, len(l1) - 1, 11))
