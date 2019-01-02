# 1. 사용자 이름 두 명을 받는 변수를 설정한다.
# 2. 사용자의 가위, 바위, 보가 무엇인지 변수를 설정한다.
# 3. if문을 이용하여 모든 경우를 설정한다. 바위 2가지 경우, 보 2가지 경우, 가위 2가지 경우, 드로우 경우
# 4. 함수를 설정한다.
# 5. 출력한다.

# 1,2. 사용자의 이름과 무기를 설정한다.
# 4. 함수를 선정한다.
def function():
    person_1,person_2,weapon_1,weapon_2 = input().split(" ")
# 3. if문을 이용하여
    if weapon_1 == weapon_2:
        print('draw')
    elif weapon_1 == '바위':
        if weapon_2 == '가위':
            print("{}가 이겼습니다!".format(weapon_1))
        elif weapon_2 == '보':
            print("{}가 이겼습니다!".format(weapon_2))
    elif weapon_1 == '보':
        if weapon_2 == '가위':
            print("{}가 이겼습니다!".format(weapon_2))
        elif weapon_2 == '바위':
            print("{}가 이겼습니다!".format(weapon_1))
    elif weapon_1 == '가위':
        if weapon_2 == '바위':
            print("{}가 이겼습니다!".format(weapon_2))
        elif weapon_2 == '보':
            print("{}가 이겼습니다!".format(weapon_1))
game=function()
