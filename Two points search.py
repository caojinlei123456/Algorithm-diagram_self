# _*_coding:utf-8_*_
# 作者      ：46925
# 创建时间  ：2020/2/1810:50  
# 文件      ：Two points search.py
# IDE       ：PyCharm
import numpy as np
import math
def binary_search(list , n):
    low = 0
    high = len(list)-1
    step = 0
    while low <= high:
        step = step + 1
        mid = math.floor((low+high)/2)  # 向下取整
        guess = list[mid]
        if guess == n:
            return mid ,step
        elif guess < n:
            low = mid +1
        else:
            high = mid -1
    return None,step



if __name__ == "__main__":
    data = np.arange(1, 101, 1)
    datas = [1, 3, 5, 7, 9]
    result = binary_search(data,78)
    print(result)


