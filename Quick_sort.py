# _*_coding:utf-8_*_
# 作者      ：46925
# 创建时间  ：2020/2/1910:46  
# 文件      ：Quick_sort.py
# IDE       ：PyCharm
import numpy as np
def quick_sort(list):
    if len(list)<2:
        return list
    else:
        arr = list[0]
        smaller = [i for i in list[1:] if i<=arr]
        bigger = [i for i in list[1:] if i >arr]
        return quick_sort(smaller)+[arr]+quick_sort(bigger)  # 列表相加是列表融合如[1]+[2]=[1,2]

if __name__ == "__main__":
    data = np.random.normal(1,5,20)
    data_sort = quick_sort(data)
    print(data)
    print(data_sort)
