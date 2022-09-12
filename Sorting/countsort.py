import array

a=array.array('i',[2,4,2,4,6,7,4,6,8,])
b=array.array('i',[0,0,0,0,0,0,0,0,0,0])
print(a)

n=len(a)


for i in range(0,n):
    z=a[i]
    b[z]=b[z]+1
w=0
for j in range (0,9):
    q=b[j]

    for x in range(0,q):
        a.pop(w)
        a.insert(w,j)
        w=w+1

print(a)





