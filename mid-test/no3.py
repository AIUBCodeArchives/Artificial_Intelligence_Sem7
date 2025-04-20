d = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}

def check_key(D, key):
    if key in D.keys():
        return "Already Exist"
    else:
        return "Don't exist"


user_key = int(input("Enter key:"))
print(check_key(d, user_key))

