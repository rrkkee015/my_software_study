#리스트 내포 기능을 이용해 다음 문장으로부터 모음('aeiou')을 제거하십시오.
#'Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open.'

sen = "Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open."
result = [a for a in sen if a != "a" and a !="e" and a !="i" and a !="o" and a !="u"]
result = [''.join(result[:])]
print(result[0])



#for i in sen:
#  if i != "a" and i != "e" and i != "i" and i != "o" and i != "u":
#       result.append(i)
#result=[''.join(result[:])]
#print(result[0])




#result = sen.replace("a","")
#result = result.replace("e","")
#result = result.replace("i","")
#result = result.replace("o","")
#result = result.replace("u","")
#print(result)
