# Hacker Rank URL - https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

# Answer :
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    newArr = list(set(arr))
    newArr.sort()
    print(newArr[-2])
