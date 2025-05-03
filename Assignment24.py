"""
#Q1
l1=[3,5,2,6]
sum=0
for x in l1:
    sum=sum+x
print(sum)
 
#Q2
l1=[3,5,2,6]
sum=0
for x in l1:
    sum=sum+x
print("avg is",sum/len(l1))


#Q3
l1=[3,5,2,6]
l2=[]
for x in l1:
    l2.append(x*x)
print(l2)


#Q4
l1=[0,3,2,8,7,10,6]
for e in l1:
    i=0
    while i<len(l1)-1:
        if l1[i]<l1[i+1]:
            a=l1[i]
            l1[i]=l1[i+1]
            l1[i+1]=a
        i+=1

print(l1)



#Q5
l1=[0,3,2,8,7,10,6,8,5,0]
l2=[]
k=0
for e in l1:
    if k==1:
        l2.append(e)
    k=1-k

print(l2)

#Q1
l1=[]
n=int(input("Enter number of elements you want to enter"))
for e in range(n):
    l1.append(int(input()))
sum=0
for x in l1:
    sum=sum+x
print(sum)



#Q1
print("Enter numbers separated by comma")
l1=[int(e) for e in input().split(",")]
print("sum is ",sum(l1))

#Q2
print("Enter numbers separated by comma")
l1=[int(e) for e in input().split(",")]
print("avg is ",sum(l1)/len(l1))

#Q3

print("Enter numbers separated by comma")
l1=[int(e) for e in input().split(",")]
l2=[e**2 for e in l1]
print(l2)

#Q4
print("Enter numbers separated by comma")
l1=[int(e) for e in input().split(",")]
l1.sort(reverse=True)
print(l1)


"""
#Q4
print("Enter numbers separated by comma")
l1=[int(e) for e in input().split(",")]
l2=l1[1::2]
print(l2)