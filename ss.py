s=int(input())
g=0
temp=s
while temp>0:
 digit=temp%10
 g += digit**3
 temp//=10
if s==g:
    print("yes")
else:
    print("no")
