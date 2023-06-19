def linear(a,key):
 n=len(a)
 for i in range(n):
     if a[i]==key:
      return i
      return -1
a=[4,6,7,2,]
key= int(input("enter yor number :"))
i=linear(a,key)
if i==-1:
 print(' sucefully')
else:
    print(" unsucsfully:",i+1)
## pogram
    def bubble(a):
     n=len(a)
    for i in range(n):
     for j in range(n-i):
        if a[j]<a[j+1]:
         temp=a[j]
         a[j]=a[j+1]
         a[j+1]=temp
a=[4,7,2,2,3,1]
bubble(a)
print(a)
