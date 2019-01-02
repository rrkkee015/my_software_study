#a=int(input(""))
#number=[]
#while a!=0:
    #if a%2 == 1:
       # a = a//2
      #  number.append(1)
    #if a%2 ==0:
  #      a = a//2
 #       number.append(0)
#number.pop()
#number.reverse()
#for i in number:
#    print(i,end='')

a=int(input("10진수:"))
b=[]
while a !=0:
    b.append(a%2)
    a=a//2
b.reverse()
for i in b:
    print(i,end="")
