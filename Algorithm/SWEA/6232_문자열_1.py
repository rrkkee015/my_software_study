# 다음의 결과와 같이 회문(앞뒤 어느 쪽에서도 같은 단어, 말) 여부를 판단하는 코드를 작성하십시오.
# 입력 : madam
# 출력 : madam
#        입력하신 단어는 회문(Palindrome)입니다.

#1. input 받은 변수를 만들자.
#2. if문으로 뒤집어도 같으면 입력하신 ~~이 출력되도록하자.
#3. 어떻게 뒤집지?

letter = input('')
#count = 0
#for i in range(-1, -len(letter), -1):
#    j = -i-1
#    if letter[i] != letter[j]:
#        count +=1
#if count == 0:
#    print("{}\n입력하신 단어는 회문(Palindrome)입니다.".format(letter))
#else:
#    print("입력하신 단어는 회문이 아닙니다.")

if letter == letter[::-1]:
    print("{}\n입력하신 단어는 회문(Palindrome)입니다.".format(letter))
else:
    print("{}\n입력하신 단어는 회문이 아닙니다.".format(letter))
