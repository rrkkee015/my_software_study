#상근이는 요즘 설탕공장에서 설탕을 배달하고 있다. 상근이는 지금 사탕가게에 설탕을 정확하게
#N킬로그램을 배달해야 한다. 설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와
#5킬로그램 봉지가 있다.
#상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다. 예를 들어 18킬로그램 설탕을 배달해야
#할 때, 3킬로그램 봉지 6개를 가져가도 되지만, 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은
#개수의 봉지를 배달할 수 있다.
#상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는
#프로그램을 작성하시오.

#1. N을 입력 받는다.
#2. N이 5로 나눠지면 나눈 몫이 정답 !
#3. 나눠지지 않으면 우선 5로 나눈 몫을 제외한 나머지를 3으로 또 나누어본다.
#4. 3으로 나누어 진다면 5로 나눈 몫과 3으로 나눈 몫을 더해준다.
#5. 근데 그래도 안된다면 초기값을 5로 나눈 몫에서 1을 빼주고 한번 더 3으로 나누어본다.
#6. 5로 나눈 몫이 음수가 된다면 5와 3으로 아무리 해도 안되는 수이니까 -1을 출력한다.

N=int(input(''))
i=N//5
while N>=5*i and i >= 0:
    if N%5==0:
        print(N//5)
        break
    elif (N-5*i)%3==0:
        print((N-5*i)//3+i)
        break
    i -= 1
if i <0:
    print(-1)
