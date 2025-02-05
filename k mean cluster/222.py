def list_transformation():
    alist = [4, 2, 8, 6, 5]
    blist = [alist] * 2
    alist[3] = 999
    return blist

print(list_transformation())