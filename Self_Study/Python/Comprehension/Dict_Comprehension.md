# Dict

- 한 반에 학생들이 번호 순대로 있다고 생각하고 리스트를 만들어보자

`students = ["태연","진우","정현","하늘","성진"]`

- enumerate를 써볼까?

```python
for number, name in enumerate(students):
    print("{}번의 이름은 {}입니다.".format(number+1,name))
#결과
1번의 이름은 태연입니다.
2번의 이름은 진우입니다.
...
```

- `students_dict = {"{}번".format(number+1):name for number, name in enumerate(students)}`
  1. number와 name을 enumerate를 통해 가져온다.
  2. name은 value가 되고 key는 number _1가 str에 들어가서 해결된다.

- 이번엔 zip을 알아보자

  - zip은 두 개 이상의 리스트나 str을 받아들여서 index에 맞게 for in 문에서 하나씩 던져줄 수 있게 만들어주는 역할을 한다.

  - list와 str가 아니더라도 index로 값을 가져올 수 있으면 쓸 수있지만 list, str 예만 확인해보자

    ```python
    scores = [85,92,78,90,100]
    students = ["태연","진우","정현","하늘","성진"]
    
    for x, y in zip(studnets, scores):
        print(x,y)
    #결과
    태연 85
    진우 92
    정현 78
    ...
    
    score_dic = {student : score for student, score in zip(students,scores)}
    score_dic = {'하늘':90,'정현':78....}
    #zip으로 묶어준 다음에 student, score에 하나씩 던져줬다. 그렇게 하나씩 key와 value가 되었다.
    ```
