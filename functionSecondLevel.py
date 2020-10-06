def find_number(arr_len, random_max_num, index):
    import random
    list1 = random.sample(range(0, random_max_num), arr_len)
    print(list1)
    if index > 0:
        return list1[index - 1]
    else:
        return list1[index]


print("Your number is: {}".format(find_number(15, 20, 2)))
