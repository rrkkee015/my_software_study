#1. 양의 정수를 받는다.
#2. 정수 받은걸 문자로 치환한다.
#3. for 문 돌려서 갯수를 센다.
#4. 출력한다.
a,b,c,d,e,f,g,h,i,z=0,0,0,0,0,0,0,0,0,0
number=input("")
li=[]
for element in number:
    li.append(element)
for j in li:
    if j == '1':
        a += 1
    elif j == '2':
        b += 1
    elif j == '3':
        c += 1
    elif j == '4':
        d += 1
    elif j == '5':
        e += 1
    elif j == '6':
        f += 1
    elif j == '7':
        g += 1
    elif j == '8':
        h += 1
    elif j == '9':
        i += 1
    elif j == '0':
        z += 1
print("0 1 2 3 4 5 6 7 8 9")
print("{} {} {} {} {} {} {} {} {} {}".format(z,a,b,c,d,e,f,g,h,i))



    

