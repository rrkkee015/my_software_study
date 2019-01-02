x=0
for i in range(1,101):
    if i % 2 ==0:
        x+=1
        if x==50:
            print(i)
        else:
            print(i,end=' ') #끝을 공백으로 만든다.

