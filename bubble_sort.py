def bubble_sort(lis4:list[int]):
    c=0
    for i in range(len(lis4)):
        flag=False
        for j in range(len(lis4)-1-i):
            c+=1
            if lis4[j]>lis4[j+1]:
                lis4[j+1],lis4[j]=lis4[j],lis4[j+1]
                flag=True
        if not flag:
            break
    print(c)
    return lis4
b=[8,4,80,14,30,11,56,93,100]
print(bubble_sort(b))