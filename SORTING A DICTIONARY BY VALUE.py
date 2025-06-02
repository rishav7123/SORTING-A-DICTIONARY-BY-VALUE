marks = {"Rishav":99, "Rohan":80, "Palak":60}
print(marks)

# SOLUTION 1 (SORT THE DICTIONARY BASED ON VALUES)
sorted_value = sorted(marks.items(), key = lambda x : x[1])
print(sorted_value)

# SOLUTION 2 (SORT ONLY THE VALUES)
v = sorted(marks.values())
print(v)
