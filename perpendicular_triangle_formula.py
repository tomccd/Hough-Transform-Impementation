import cv2 as cv
import numpy as np

#-Using p = y*cos(angle) - x*cos(angle) theo cách tìm
#đường thẳng vuông góc ngắn nhất trong tam giác (perpendicular distance in a triangle)

#-Với p là khoảng cách vuông góc với đường thẳng đi 
#qua điểm có tọa độ (x,y)

#-Với angle là góc giữa trục Ox và đường thẳng vuông góc

def calc_accumulator(arr,point,max_value):
    x = point[0]
    y = point[1]
    angles = np.array([0,np.pi/6,np.pi/4,np.pi/3,np.pi/2,2*np.pi/3,3*np.pi/4,5*np.pi/6,np.pi])
    for theta_point in range(9):
        p = y*np.cos(angles[theta_point]) - x*np.sin(angles[theta_point])
        if p<0:
            p = max_value-p
        p = int(p)
        arr[p][theta_point]+=1            

#Cho 3 điểm nằm trên 1 bức ảnh gray kích thước 100x100
#Lúc này p sẽ có độ dài giới hạn là đường chéo chính của bức ảnh 100x100
point_A = (50,50)
point_B = (3,50)
point_C = (11,50)

#Tính đường chéo chính
diagonal_picture = int(np.sqrt(pow(100,2)+pow(100,2)))
#Do tính cả dương và âm, nên ta gấp đôi kích thước của accumulate array
accumulate_arr = np.zeros((diagonal_picture*2,9))

calc_accumulator(accumulate_arr,point_A,diagonal_picture)
calc_accumulator(accumulate_arr,point_B,diagonal_picture)
calc_accumulator(accumulate_arr,point_C,diagonal_picture)

#Nếu 3 điểm cùng nằm trên đường thẳng
if 3 in accumulate_arr:
    print(True)
else:
    print(False)

