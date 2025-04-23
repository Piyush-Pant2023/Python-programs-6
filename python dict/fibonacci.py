# n=int(input("enter the number :"))
# a1=0;a2=1
# print(a1,a2,end='')
# for x in range(n-2):
#     sum=a1=a2
#     print(sum,end='')
#     a1,a2=a2,sum

n=int(input("enter the  number :"))
new=n
sum=0
while n>0:
    r=n%10
    sum+=r**3
    n=n//10
if sum==new:
    print("yes it is armstrong number")
else:
     print("no")

