def tinh_tong_so_chan(lst):
    sum = 0
    for i in lst:
        if i % 2 == 0:
            sum += i
    return sum
input_list = input("Nhập danh sách số (phân tách bởi dấu ,):")
number = list(map(int, input_list.split(',')))
tong_chan = tinh_tong_so_chan(number)
print("Tổng các số chẵn trong danh sách là: ", tong_chan)