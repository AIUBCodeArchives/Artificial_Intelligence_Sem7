# Multi-Dick
myFamily = {
    "child1": {
        "name": "John",
        "year": 1998
    },
    "child2": {
        "name": "Kim So Hyun",
        "year": 1978
    },
    "child3": {
        "name": "Jackie Chan",
        "year": 1959
    },
    "father": {
        "name": "Master Chief",
        "year": 1990
    },
    "mother": {
        "name": "Mary Poppins",
        "year": 1980
    }
}

print(myFamily)

myFamily["child2"]["name"] = "Name changed"
del(myFamily["child3"]["name"])
print(myFamily)
myFamily.pop("mother")
print(myFamily)