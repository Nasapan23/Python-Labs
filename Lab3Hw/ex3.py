def split_list(lst):
    listEven = [x for x in lst if x % 2 == 0]
    listOdd = [x for x in lst if x % 2 == 1]
    return listEven, listOdd
