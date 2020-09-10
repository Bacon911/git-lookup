def add_element_to_list(my_list, a):
    my_list.append(a)
    return my_list


def delete_element_to_list(my_list):
    my_list.pop()
    return my_list


my_list = [1, 2, 3, 4]
print("Изначальный список: ", my_list)
print("Список с удаленным последним элементом: ")
print(delete_element_to_list(my_list))
x = int(input("Введите ваше число:"))
print(add_element_to_list(my_list, x))

