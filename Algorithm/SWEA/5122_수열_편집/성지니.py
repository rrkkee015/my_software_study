import sys

sys.stdin = open("sample_input.txt", "r")


class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next


def check():
    cur = Head
    while cur != None:
        print(cur.item)
        cur = cur.next


T = int(input())
for t in range(1, T + 1):

    n, m, l = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    Head = Node(nums[0])
    cur = Head
    for i in range(1, n):
        cur.next = Node(nums[i])
        cur = cur.next
    # check()
    for i in range(m):
        edit = input().split()
        if edit[0] == "I":
            # print ("I를 만났다.")
            cnt = 0
            cur = Head
            new = Node(int(edit[2]))
            if int(edit[1]) == 0:
                if Head == None:
                    Head = new
                    continue
                else:
                    new.next = Head.next
                    Head = new
                    continue
            while cnt != int(edit[1]) - 1:
                cur = cur.next
                cnt += 1
            if cur.next == None:
                cur.next = new
            else:
                new.next = cur.next
                cur.next = new
            # check()
        elif edit[0] == "D":
            # print("D를 만났다.")
            cnt = 0
            cur = Head
            if int(edit[1]) == 0:
                Head = cur.next
                continue
            while cnt != int(edit[1]) - 1:
                cur = cur.next
                cnt += 1
            if cur.next.next == None:
                cur.next = None
            else:
                cur.next = cur.next.next
            # check()
        else:  # C
            # print("C를 만났다.")
            cnt = 0
            cur = Head
            while cnt != int(edit[1]):
                cur = cur.next
                cnt += 1
            cur.item = int(edit[2])
            # check()
    # check()
    cnt = 0
    cur = Head
    while cnt != l:
        if cur == None:
            break
        cur = cur.next
        cnt += 1
    if cur == None:
        print(f"#{t} -1")
    else:
        print(f"#{t} {cur.item}")

