
l = [1,5,3,6,2]
l2 = [1,3,5,8,9,1,5]

def filter_elements(first_list:list, second_list:list) -> list:
    new_list = []
    for item in first_list:
        if not item in second_list:
            new_list.append(item)
    return new_list

arr = [0,1,0,0,4,5,6,7,0,8,-4,0]

def zero_filter(arr: list) -> list:
    return [item for item in arr if item != 0]


if __name__ == "__main__" :
    print(filter_elements(l, l2))
    print(zero_filter(arr))
