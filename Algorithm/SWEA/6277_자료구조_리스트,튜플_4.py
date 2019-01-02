#리스트 내포 기능을 활용해 입력된 정수 값 5개의 평균을 출력하는 프로그램을 작성하십시오.
#lis = [a for a in input('').split(' ')]
#lis = list(map(int,lis))
#average = 0
#for i in lis:
#    average = average + i
#average = average / len(lis)
#print("입력된 값 {}의 평균은 {}입니다.".format(lis,average))
#########################################
lis = [int(input('')) for a in range(1,6)]
average = 0
for i in lis:
    average = average + i
average= average / len(lis)
print("입력된 값 {}의 평균은 {}입니다.".format(lis,average))
