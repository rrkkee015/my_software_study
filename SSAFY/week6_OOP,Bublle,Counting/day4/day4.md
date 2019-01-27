1. 정확히 이터러블 객체가 무엇인지? 왜 딕셔너리는 for문을 돌릴 수 있는지?

2. ```python
   dict(한국어='안녕',영어='hello')
   #결과
   {'한국어':'안녕','영어':'hello'} #왜 한국어가 읽혀지는지?
   ```

3. ```python
   def my_fake_dict(**args):
       return args
   my_fake_dict(한국어='안녕',영어='hello')
   
   #얘는 패킹인가요?
   
   def hi(*args):
       return sum(args)
   print(1,2,3)
   ```

4. ```python
   def user(pw,pwc,user):
       if pw==pwc:
           return 'good'
       else:
           return 'nope'
   user(**{'user':'rrkkee015','pw':1213,'pwc':1213})
   
   #얘는 언패킹 인가요?
   
   def hi(a,b,c):
       return a+b+c
   hi(*[1,2,3])
   ```

---

# Week6_day4

- 어제 했었던 조망권 문제 리뷰

  ```python
  def getMax(idx): #되도록이면 라이브러리를 쓰지말자
      tmax = heights[idx - 2]
      
      if tmax < heights[idx-1]: tmax = heights[idx-1]
      if tmax < heights[idx+1]: tmax = heights[idx+1]
      if tmax < heights[idx+2]: tmax = heights[idx+2]
          
  TC=10
  for tc in range(1,TC+1):
      N=int(input())
      heights=list(map(int,input().split()))
      view=0 #얘가 테스트케이스가 끝나면 초기화 해야하는 걸 잊지말자
      
      for i in range(2,N-2):
          side=getMax(i) #i라는 건물 입장에서
          if side < heights[i]:
              view += heights[i]-side
    	print("#%d %d"%(tc, view))
  ```
