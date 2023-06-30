marks=[1,2,3,4,5,6,7,8,9,10]
print(marks)
print("=============================")
marks.append(-12)
print(marks)
print(" after intertion =============================")

marks=marks+[29]

print(marks)
print(" another way to insertion =============================")

# list.insert(position, element)

# del my_list[index]

# Delete the element at the specified index

del marks[2]
print(marks)





marks.remove(4)  # Remove the first occurrence of the specified value
print(marks)
print(" 4 not present  another way to insertion =============================")

marks.remove(5)
print(" lets see what happend if value not present in the list")
print(marks)

# my_list.sort(reverse=True)  my_list.sort()
marks.sort()

print(marks)

marks.sort(reverse=True)
print(marks)

print(len(marks))