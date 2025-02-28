s = "password1234"

#a
NewS1 = s[0].upper() + s[1:]
print(NewS1)

#b
print(s.replace('a', 'e').replace('e', 'i').replace('i', 'o').replace('o', 'u').replace('u', 'a'))

#c
print(s.replace('s', '$').replace('S', '$'))

#d
Converted_s = s[:-4] + str(int(s[-4:])*2)
print(Converted_s)


