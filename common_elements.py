def common_elements(list1, list2):
    common = []
    for element in list1:
        if element in list2:
            common.append(element)
    return common

print(common_elements([1,2,3,4,5,6], [3,5,7,9]))