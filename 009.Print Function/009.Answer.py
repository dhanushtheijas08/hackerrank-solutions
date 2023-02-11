# Hacker Rank URL - https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

# Answer :
if __name__ == '__main__':
    n = int(input())
    newNum = ''
    for i in range(1, n+1) :
        newNum = str(newNum) + str(i)
    print(newNum)
