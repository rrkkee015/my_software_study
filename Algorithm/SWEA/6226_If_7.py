a=[]
#b=[]
for i in range (1,201):
    a.append(i)
for j in range(0,195):
    if a[j] % 7 == 0 and a[j] % 5 != 0:
        print(str(a[j]) +",", end='') #end를 이용해 끝 문자를 지정했다.
print(a[195])
#        b.append(a[j])
#print(b)
