def groups_of_3(arr : list[int]) -> list[list[int]]:
    mega_list = []
    for i in range(0, len(arr), 3):
        mega_list.append(arr[i:i + 3])
    return mega_list

lists = [1,2,3,4,5,6,7,8,9,1,2,3,4,5]
print(groups_of_3(lists))




