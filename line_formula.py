import numpy as np

#Using y = mx + c formula
def calc_accumulator(arr,point):
    #c = y-mx
    x = point[0]
    y = point[1]
    for m in range(5):
        c = y-m*x
        arr[c][m]+=1

point_A = (1,50)
point_B = (2,50)
point_C = (3,50)

#Ma trận tính toán
accumulate_arr = np.zeros((51,5))

#Nếu xác định được 2 điểm m và c, ta cộng dồn giá trị tại điểm ở tọa độ đó
calc_accumulator(accumulate_arr,point_A)
calc_accumulator(accumulate_arr,point_B)
calc_accumulator(accumulate_arr,point_C)

#Nếu giá trị trên ma trận tính toán có phần tử có giá trị bằng số điểm đang xét
#thì kết luận 3 điểm đó thẳng hàng or nằm trên phương trình đường thẳng
#y = mx + c. Do cùng m và c nên các điểm đó cùng nằm trên đường thẳng
if 3 in accumulate_arr:
    print(True)
else:
    print(False)