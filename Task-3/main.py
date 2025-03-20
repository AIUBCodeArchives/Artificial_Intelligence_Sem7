Rakin = {
    "Full-name": "Raiyen Zayed Rakin",
    "University": "AIUB",
    "Program": "B.Sc in CSE",
    "CGPA": 2.50,
    "Address": "Shiddeshwari",
    "Facts": "Is sick currently"
}

print(Rakin)

Rakin["Credits Completed"] = 84
print(Rakin)

Rakin.pop("Facts")
print(Rakin)

Rakin.popitem()
print(Rakin)

del(Rakin["Address"])
print(Rakin)

# print all even number in a list using function
def print_even(my_list):
    for x in my_list:
        if x%2==0:
            print(x)

my_list=[10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print_even(my_list)