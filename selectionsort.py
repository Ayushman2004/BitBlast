import array

a=array.array('i',[23,63,25,94,26,93,25])

b=len(a)


for i in range(0,b):
    k=a[i]
    n=i
    for j in range(i,b):
        if k>a[j]:
            k=a[j]
            n=j

            
        
    z=a[i]
    a[i]=a[n]
    a[n]=z



print(a)

