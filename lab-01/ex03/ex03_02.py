def dao_nguoc_list(lst):
    return lst[::-1]
lst = input("Nhập danh sách số (phân tách bởi dấu ,):")
number = list(map(int, lst.split(',')))
reverse_lst = dao_nguoc_list(number)
print("Danh sách sau khi đảo ngược là: ", reverse_lst)