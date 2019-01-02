Game = ["가위","바위","보"]
Man1 = input("")
Man2 = input("")
if Man1 == "바위" and Man2 == "가위":
    print("Result : Man1 Win!")
elif Man1 == "바위" and Man2 =="보":
    print("Reulst : Man2 Win!")
elif Man1 == "바위" and Man2 =="바위": #굳이 Draw를 적을 필요가 없었다.
    print("Reulst : Draw!")
elif Man1 == "가위" and Man2 =="보":
    print("Reulst : Man1 Win!")
elif Man1 == "가위" and Man2 =="가위": #굳이 Draw를 적을 필요가 없었다.
    print("Reulst : Draw!")
elif Man1 == "가위" and Man2 =="바위":
    print("Reulst : Man2 Win!")
elif Man1 == "바위" and Man2 =="보":
    print("Reulst : Man2 Win!")
elif Man1 == "보" and Man2 =="바위":
    print("Reulst : Man1 Win!")
elif Man1 == "보" and Man2 =="가위":
    print("Reulst : Man2 Win!")
else:
    print("Draw!")

#if를 중복으로 사용해서 하는 방법도 있다.
#if Man1 == Man2:
#   print("Draw!")
#if Man1 =="바위":
#   if Man2 == "가위":
#       print("Man1 Win!")
#   elif Man2 == "보":
#       print("Man2 Win!")
#이런식으로
