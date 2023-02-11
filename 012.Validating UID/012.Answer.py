# Hacker Rank URL - https://www.hackerrank.com/challenges/validating-uid/problem?isFullScreen=false

# Answer :
import re
n = int(input())
for i in range(n):
    Uid = input()
    if((len(re.findall(r'[A-Z]',Uid)) >=2 ) 
    and (len(re.findall(r'[0-9]',Uid)) >=3)
    and len(Uid) == 10 and Uid.isalnum()
    and len(Uid) == len(set(Uid))):
        print("Valid")
    else:
        print("Invalid")