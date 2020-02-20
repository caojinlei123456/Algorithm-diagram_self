# _*_coding:utf-8_*_
# 作者      ：46925
# 创建时间  ：2020/2/209:42  
# 文件      ：Breadth first search.py
# IDE       ：PyCharm
from collections import deque # 队列


def person_name(names):
    return names[-1] == "m"

def breadth_fist_search(dict,name):
    search_deque = deque()
    search_deque += dict[name]
    search_end = []
    while search_deque:
        person =search_deque.popleft()
        if person not in search_end:
            if person_name(person):
                print(person + " is our mango!")
                return True
            else:
                search_deque +=dict[person]
                search_end.append(person)
    return False

if __name__ == "__main__":
    graph = dict()
    graph['You'] = ['bob', 'alice', 'claire']  # 只找出最短路径
    graph['bob'] = ['jane', 'peggy']
    graph['alice'] = ['peggy', 'james']
    graph['claire'] = ['tom','tony']
    graph['tom'] = []
    graph['jane'] = []
    graph['peggy'] = ['You']
    graph['james'] = []
    graph['tony'] = []
    breadth_fist_search(graph,'You')










