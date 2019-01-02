#1. 입력값과 입력값을 뒤집은 값이 같는지 안같은지 if문으로 비교한다.
#2. 입력값이 뒤집어져서 출력할 수 있도록 코드를 짠다.

def function():
    string = input('')
    if string == string[::-1]:
        return string[::-1]+'\n'+'입력하신 단어는 회문(Palindrome)입니다.'
    else:
        return string[::-1]
    
words = function()
print(words)
