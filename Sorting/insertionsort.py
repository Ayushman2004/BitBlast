
import array 

a=array.array('i',[4,6,3,64,6,3,4])

b=len(a)

for i in range(0,b):
    for j in range(0,i):
        if a[i]<a[j]:
            k=a[i]
            a[i]=a[j]
            a[j]=k
        else:
            continue

print(a)