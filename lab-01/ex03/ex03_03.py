def tao_tuple_tu_list(a):
    # return a tuple from a list
    return tuple(a)
lst = input("Nhập danh sách số (phân tách bởi dấu ,):")
numbers = list(map(int, lst.split(',')))
my_tuple = tao_tuple_tu_list(numbers)
print("List", numbers)
print("Tuple được tạo từ danh sách số là:", my_tuple)