# N=int(input())
# result=[]
# cnt=0
# for i in range(N):
#     a,b,c,d=input().split()
#     result+=[(int(b),int(c),int(d),a)]
#
# for i in range(len(result)-1,0,-1):
#     for j in range(i):
#         if result[j][0]<result[j+1][0]:
#             result[j],result[j+1]=result[j+1],result[j]
#
# min=0
#
# for i in range(len(result)-1):
#     if result[i][0] != result[i+1][0]:
#         for i in range(i,min+1,-1):
#             for j in range(min+1,i):
#                 if result[j][1]>result[j+1][1]:
#                     result[j],result[j+1]=result[j+1],result[j]
#         min=i+1
#     if result[i][0]==result[-1][0]:
#         for k in range(len(result)-1,min+1,-1):
#             for j in range(min,k):
#                 if result[j][1]>result[j+1][1]:
#                     result[j],result[j+1]=result[j+1],result[j]
#
# min =0
#
# for i in range(len(result)-1):
#     if result[i][0]==result[i+1][0] and result[i][1]!=result[i+1][1]:
#         for k in range(i,min+1,-1):
#             for j in range(min+1,k):
#                 if result[j][2]<result[j+1][2]:
#                     result[j],result[j+1]=result[j+1],result[j]
#         min=i+1
#     if result[i][0]==result[-1][0] and result[i][1] == result[-1][1]:
#         for p in range(len(result)-1,min+1,-1):
#             for j in range(min,p):
#                 if result[j][2]>result[j+1][2]:
#                     result[j],result[j+1]=result[j+1],result[j]
#
# for i in result:
#     print(i)
# 틀린 코드

# N = int(input())
# students = []
# for _ in range(N):
#     student = list(map(str,input().split()))
#     student[1] = int(student[1])
#     student[2] = int(student[2])
#     student[3] = int(student[3])
#     students.append(student)
# students = sorted(students, key = lambda x:(-x[1],x[2],-x[3],x[0]))
# for _ in range(len(students)):
#     print(students[_][0])
# sorted 이용

N = int(input())
students = []
for _ in range(N):
    stu = list(map(str,input().split()))
    students.append([-int(stu[1]), int(stu[2]), -int(stu[3]), stu[0]])
students.sort()
for _ in range(len(students)):
    print(students[_][3])

# append 할 때 +, - 특성을 이용