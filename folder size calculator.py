# Write a program that finds the total size of a folder by adding the sizes of all files inside it,
# including the files inside every subfolder, sub-subfolder, and so on.


def calculate_size(folder):
    total_size = 0

    for item in folder:
        if type(item) == int:
            total_size += item
        else:
            total_size += calculate_size(item)

    return total_size


# Folder Structure
# folder = [
#     100,
#     200,
#     [
#         50,
#         [
#             150
#         ]
#     ]
# ]
folder = [100, 200, [50, [150]]]

print(f"Size: {calculate_size(folder=folder)}")
