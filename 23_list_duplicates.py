# Remove Duplicates: Remove duplicate elements from a list

print("Remove Duplicates: Remove duplicate elements from a list")
elems = input("Enter elements separated by spaces: ").split()

unique_list = []
for elem in elems:
    if elem not in unique_list:
        unique_list.append(elem)

print("Original List:", elems)
print("List without duplicates:", unique_list)
