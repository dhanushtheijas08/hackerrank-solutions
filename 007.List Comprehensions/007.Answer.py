# Hacker Rank URL - https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=false

# Answer :
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    arrs = []
    for i in range(0, x+1):
        for j in range(0, y+1):
            for k in range(0, z+1):
                arrs.append([i, j, k])

    finalArr = [arr for arr in arrs if (arr[0] + arr[1]+arr[2] != n)]
    print(finalArr)
