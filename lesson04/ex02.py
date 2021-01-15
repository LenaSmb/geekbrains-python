def greater_than_prev(my_list):
    result = []

    for el in range(len(my_list)-1):
        if my_list[el] < my_list[el+1]:
            result.append(my_list[el+1])
    
    return result

print(greater_than_prev([300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]))