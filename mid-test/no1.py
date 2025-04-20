list_of_strings = ["abc", "xyz", "aba", "1221"]
count = 0

for string in list_of_strings:
    if string[0]==string[-1]:
        count = count + 1


print("Result: "+str(count))
