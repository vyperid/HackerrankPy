#Problem link is: https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

n = int(input())
s = set(map(int, input().split()))
N = int(input())

for i in range(N):
    sentence = input().split()
    if sentence[0] != "pop": #checks whether the value is pop or not, i do this because when the value is equal to pop it doesn't have a second value.
        expression = sentence[0]
        number = int(sentence[1])
    if sentence[0] == "pop":
        s.pop()
    elif (expression == "remove") and (number in s):
        s.remove(number)
    elif (expression == "discard") and (number in s):
        s.discard(number)
        
print(sum(s))
