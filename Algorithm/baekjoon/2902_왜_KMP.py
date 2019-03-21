str_=input()
result=''
for _ in range(len(str_)):
    if _ == 0:
        result+=str_[_]
    elif str_[_]=='-':
        result+=str_[_+1]
print(result)