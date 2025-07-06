#q1 a,b
# import random
# a=0
# def find_min_index(li1:list[int],start:int):
#     min_1=li1[start:]
#     min_val = min_1[0]
#     min_index = 0
#     global a
#     for i, j in enumerate(min_1):
#         a+=1
#         if j < min_val:
#             min_val = j
#             min_index = i
#     return min_index + start
#
# def swap(li1:int,i1:int,i2:int):
#     li1[i1], li1[i2] = li1[i2], li1[i1]
#
#
# def selection_sort(li1:list):
#     global a
#     for i in range(len(li1)):
#         a+=1
#         minimum=find_min_index(li1,i)
#         swap(li1,i,minimum)
#     print(f"selection count:{a}")
#     return li1
# def find_max_index(li1:list[int],start:int):
#     max_1=li1[start:]
#     max_val = max_1[0]
#     max_index = 0
#     for i, j in enumerate(max_1):
#         if j > max_val:
#             max_val = j
#             max_index = i
#     return max_index + start
# def decending_selection_sort(li1:list):
#     for i in range(len(li1)):
#         maximum=find_max_index(li1,i)
#         swap(li1,i,maximum)
#
#     return li1
# #q2 a,b
# def bubble_sorting_up(li4:list[int]):
#     c=0
#     for i in range(len(li4)):
#         flag=False
#         c+=1
#         for j in range(len(li4)-1-i):
#             c+=1
#             if li4[j]>li4[j+1]:
#                 flag=True
#                 swap(li4,j,j+1)
#                 c+=1
#         if not flag:
#             break
#     print(f"bubble count: {c}" )
#     return li4
# def bubble_sorting_down(li4:list[int]):
#     c=0
#     for i in range(len(li4)):
#         flag=False
#         c+=1
#         for j in range(len(li4)-1-i):
#             c+=1
#             if li4[j]<li4[j+1]:
#                 flag=True
#                 swap(li4,j,j+1)
#         if not flag:
#             break
#     return li4
# #q3
# def sorting():
#     l1 = []
#     l2 = []
#     for i in range(10):
#         x = random.randint(1,100)
#         l1.append(x)
#         l2.append(x)
#     selection_sort(l1)
#     bubble_sorting_up(l2)
# # sorting()
# # q4
# def bubble_string_len(lis_str:list[str]):
#     for i in range(len(lis_str)):
#         for j in range(len(lis_str)-1):
#             if len(lis_str[j])>len(lis_str[j+1]):
#                 lis_str[j],lis_str[j+1]= lis_str[j+1],lis_str[j]
#     return lis_str
# # lo_str=["avi","avishag","avigail","avraham","israel","mehir"]
# # print(bubble_string_len(lo_str))
# #q5
# def ind_selection_sort(li5:list[int],num:int):
#     for i in range(num):
#         min_ind=i
#         for j in range(i,num):
#             if li5[j]<li5[min_ind]:
#                 min_ind=j
#         swap(li5,i,min_ind)
#     return li5
# def ind_bubble_sort(li5:list[int],num:int):
#     for i in range(num):
#         flag=False
#         for j in range(num-i-1):
#             if li5[j]>li5[j+1]:
#                 swap(li5,j,j+1)
#                 flag=True
#         if not flag:
#             break
#     return li5
# # li2=[14, 16, 6, 16, 7, 7, 16, 1, 5, 19, 5, 8, 4, 3, 17]
# # print(ind_bubble_sort(li2,10))
# #q6
# lis_str=["avi","avishag","avigail","avraham","israel","mehir"]
# # print(bubble_sorting_up(lis_str))
# # print(selection_sort(lis_str))
# #q7
# def menu_list(li6:list[int]):
#     cho_lis1=["a","b","c","d"]
#     choice=input("Please choose what you want to do with your list:\nA. Sort by selection sort\nB. Sort by bubble sort\nC. Sort only part of the list\nD. Check if your list is already sorted\nEnter your choice: ")
#     while choice not in cho_lis1:
#         print("Rong answer!")
#         choice = input("Please choose what you want to do with your list:\nA. Sort by selection sort\nB. Sort by bubble sort\nC. Sort only part of the list\nD. Check if your list is already sorted\nEnter your choice: ")
#     if choice=="a":
#         cho_a=input("How do you want to sort?\nA.Ascending\nB.Descending\n:")
#         while cho_a not in cho_lis1[:2]:
#             print("Rong answer")
#             cho_a = input("How do you want to sort?\nA.Ascending\nB.Descending\n:")
#         if cho_a=="a":
#             print(selection_sort(li6))
#         elif cho_a=="b":
#             print(decending_selection_sort(li6))
#     elif choice=="b":
#         cho_b=input("How do you want to sort?\nA.Ascending\nB.Descending\n:")
#         while cho_b not in cho_lis1[:2]:
#             print("Rong answer")
#             cho_b = input("How do you want to sort?\nA.Ascending\nB.Descending\n:")
#         if cho_b=="a":
#             print(bubble_sorting_up(li6))
#         elif cho_b=="b":
#             print(bubble_sorting_down(li6))
#     elif choice=="c":
#         num=int(input("Please enter a number that will be the limit: "))
#         cho_c=input("How do you want to sort?\nA.selection sort \nB.Bubble sort\n:")
#         if cho_c=="a":
#             print(ind_selection_sort(li6,num))
#         elif cho_c=="b":
#             print(ind_bubble_sort(li6,num))
#     elif choice=="d":
#         flag=False
#         for i in range(len(li6)-1):
#             if li6[i] > li6[i+1]:
#                 flag=True
#         if not flag:
#             print("The list is sorted.")
#         else:
#             print("The list is not sorted.")
#     return None
# menu_list([14, 16, 6, 16, 7, 7, 16, 1, 5, 19, 5, 8, 4, 3, 17])
def swich(li:list[str],a,b):
    li[a],li[b]=li[b],li[a]
    return li
def bubble_pu_up(li:list[str],inde:int):
    for i in range(len(li)-1):
        for j in range(len(li)-1-i):
            if li[i].split(',')[inde] > li[i+1].split(',')[inde]:
                swich(li, i, i + 1)
    return li
def bubble_pu_down(li:list[str],inde:int):
    for i in range(len(li)-1):
        for j in range(len(li)-1-i):
            if li[i].split(',')[inde] < li[i + 1].split(',')[inde]:
                swich(li, i, i + 1)
    return li
def pu_sort(details:list[str]):
    """
    this sort take a list
    and split it by taking
    the first name alone
    and also last name
    and also age alone.
    and asking the user
    which list does he need.
    :param details: list with
    all the details together.
    :return: the choice of the user.
    """
    choice_2=input("please choose from this list how do you want to sort this list?\nA.By first name\nB.By last name\nC.By age\n")
    if choice_2=="a":
        x = 0
    elif choice_2 =="b":
        x = 1
    elif choice_2 == "c":
        x = 2
    cho_a_2= input("How do you want to sort?\nA.Ascending\nB.Descending\n:")
    if cho_a_2=="a":
        li=bubble_pu_up(details,x)
    elif cho_a_2=="b":
        li=bubble_pu_down(details,x)
    return li
d = ["dani,gindi,30", "yonatan,cohen,90", "idan,sananes,40"]
print(pu_sort(d))