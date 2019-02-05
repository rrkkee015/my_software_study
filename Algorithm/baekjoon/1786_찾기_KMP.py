P= input()
T= input()

result=[0]
i=0
j=0

for i in range(1,len(T)):
    j=result[i-1]
    while j>0 and T[i]!=T[j]:
        j=result[j-1]
    result.append(j+1 if T[i]==T[j] else j)
i=0
j=0
answer=0
answer_=''
# print(result)
while i<len(P) and j<len(T):
    if j>0 and P[i] != T[j]:
        j = result[j-1]
    if(P[i]==T[j]):
        if j==len(T)-1:
            answer+=1
            answer_+= str(i-j+1) + ' '
            j=result[len(T)-1]
        else:
            j += 1
    i+=1
print(answer)
print(answer_)