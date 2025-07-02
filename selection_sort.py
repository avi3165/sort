def find_min_index(li1:list[int],start:int):
    min_1=li1[start:]
    min_val = min_1[0]
    min_index = 0
    for i, j in enumerate(min_1):
        if j < min_val:
            min_val = j
            min_index = i
    return min_index + start

def swap(li1:int,i1:int,i2:int):
    li1[i1], li1[i2] = li1[i2], li1[i1]

def selection_sort(li1:list):
    for i in range(len(li1)):
        minimum=find_min_index(li1,i)
        swap(li1,i,minimum)
    return li1
#q1
def find_max_index(li1:list[int],start:int):
    max_1=li1[start:]
    max_val = max_1[0]
    max_index = 0
    for i, j in enumerate(max_1):
        if j > max_val:
            max_val = j
            max_index = i
    return max_index + start
def decending_selection_sort(li1:list):
    for i in range(len(li1)):
        maximum=find_max_index(li1,i)
        swap(li1,i,maximum)
    return li1
#q2
def char_selection_sort(str1:str):
    str_list=list(str1)
    selection_sort(str_list)
    return ''.join((str_list))
#q3
def positive_selection_sort(li1:list[int]):
    positive=[]
    for i in li1:
        if i>0:
            positive.append(i)
    new_list=selection_sort(positive)
    return new_list
#q4
def find_min_len(l:list[str]):
    min_len =len(l[0])
    min_index = 0
    for i in range(len(l)):
        if len(l[i]) < min_len:
            min_len = len(l[i])
            min_index = i
    return min_index

def string_length(lis_str:list[str]):
    for i in range(len(lis_str)):
        minimum = find_min_len(lis_str[i:])
        swap(lis_str, i, minimum+i)
    return lis_str
#q5

def part_of_sort(li3:list[int],num:int):
    for i in range(num):
        minimum = find_min_index(li3, i)
        swap(li3, i, minimum)
    return li3
h=[5000,87,7664,2,454,65,75,35,36,1,55,4,3]
print(part_of_sort(h,3))