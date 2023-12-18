For those who likes to solve patterns as I do (xd) this is another way to do it:
You can simply use center() function in the for loops too but i wanted to see the pattern and come up with an idea. (.|.) patterns come with an order and it is i + 3 while i is 1. Also they decrease through i - 3 while i = N-2.

N, M = map(int, input().split())

numOfLines = int((M-3)/2)
firstPattern=1
secondPattern=N-2
pattern = ".|."

for i in range(numOfLines, 0, -3):
    print(('-' * i)+ (pattern * firstPattern) + ('-' * i))
    firstPattern = firstPattern+2
    
print("WELCOME".center(M, "-"))

for j in range(3, numOfLines+1, 3):
    print(('-' * j)+ (pattern * secondPattern) + ('-' * j))
    secondPattern = secondPattern-2
