# _*_coding:utf-8_*_
# 作者      ：46925
# 创建时间  ：2020/2/1814:43  
# 文件      ：Selection sort.py
# IDE       ：PyCharm
# 选择最小排序
def find_smallest(list):
    small_value = list[0]
    small_index = 0
    for i in range(len(list)):
        if small_value > list[i]:
            small_value = list[i]
            small_index = i
    return small_index

def selection_sort(list):
    new_data = []
    for j in range(len(list)):
        smallest = find_smallest(list)
        new_data.append(list.pop(smallest))
    return new_data



if __name__ == "__main__":
    data = [1, 8, 6, 15, 20, 3, 60, 45]
    result = selection_sort(data)
    print(result)
