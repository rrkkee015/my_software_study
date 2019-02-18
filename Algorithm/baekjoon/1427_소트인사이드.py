N=input()
# result={}
# word=''
# for i in range(len(N)):
#     if N[i] not in result:
#         result[N[i]]=1
#     else:
#         result[N[i]]+=1
# for k,v in sorted(result.items()):
#     word+=str(k)*v
# print(word[::-1])

result=[0]*10
word=''
for i in range(len(N)):
    result[int(N[i])]+=1
for k in range(len(result)):
    word+=str(k)*result[k]
print(word[::-1])