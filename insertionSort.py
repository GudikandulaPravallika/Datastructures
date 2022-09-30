def insertionSort(a):
    for i in range(1,len(a)):
        j=i-1
        next_element=a[i]
        while a[j]>next_element and j>=0:
            a[j+1]=a[j]
            j=j-1
        a[j-1]=next_element
    return a
lt=[]
n=int(input("enter the size of the list"))
for i in range(n):
    x=int(input())
    lt.append(x)
print(lt)
print(insertionSort(lt))

