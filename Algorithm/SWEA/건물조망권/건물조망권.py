import sys

sys.stdin = open('input.txt','r')
for j in range(1, 11):
    test_case = int(input())
    building_floors = list(map(int,input().split()))
    count = 0
    for i in range(2, test_case-2):
        max_building = max(building_floors[i-2],building_floors[i-1],building_floors[i+1],building_floors[i+2])
        if building_floors[i] >  max_building:
            count += building_floors[i] - max_building
    print(f'# {j} {count}')
