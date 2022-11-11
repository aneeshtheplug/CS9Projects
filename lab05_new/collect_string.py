def collectStrings(aList, length):
    if len(aList) == 0:
        return []
    elif len(aList[0]) >= length:
        new_list = []
        item_list = [aList[0]]
        new_list = new_list + item_list
        return new_list + collectStrings(aList[1:], length)

    else:
        return collectStrings(aList[1:], length)






list1 = []
list2 = ["Harry","Hermoine","Hagrid"]
list3 = ["CA","WA","NV"]
assert collectStrings(list1,1) == []
print(collectStrings(list2,7))

assert collectStrings(list2,7) == ["Hermoine"]
assert collectStrings(list3,2) == ["CA","WA","NV"]
assert collectStrings(list3,3) == []