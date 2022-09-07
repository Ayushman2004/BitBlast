
import array

b=array.array('i',[2,4,6,3,4,2,5,62])

a=len(b)
z=a-1

for j in range(0,a-1):
  for i in range(0,z):
        if b[i]>b[i+1]:
            k=b[i]
            b[i]=b[i+1]
            b[i+1]=k
            z=z-1
        else:
            continue

print(b)



