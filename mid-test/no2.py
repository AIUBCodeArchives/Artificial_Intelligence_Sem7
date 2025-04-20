l1 = [1,4,6,3,8,10,7]
l2 = [11,12,3,15,10,6]

def least_one_common(L1, L2):
    flag = False
    count = 0
    for i in L1:
        for j in L2:
            if i == j:
                count = count + 1
                flag = True

    return (flag, count)
 



print(least_one_common(l1, l2))
