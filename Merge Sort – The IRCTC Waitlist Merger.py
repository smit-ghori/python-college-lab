# h3) Merge Sort – The IRCTC Waitlist Merger

# IRCTC has two separately sorted waitlists—one from its mobile app and one from railway counters. They need to be merged into a single sorted waitlist.

# Question:
# Write a program to merge two sorted arrays/lists into one sorted array using the merge step of Merge Sort.


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    i = 0
    j = 0
    result = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result


arr = [8, 3, 5, 1, 9, 2, 7, 6]

sorted_arr = merge_sort(arr)

print("Original Array:", arr)
print("Sorted Array:", sorted_arr)
