# Date: 7/19/19
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# Hackerrank python challenges

if __name__ == '__main__':
    n = 5#int(input())
    arr = map(int, "-77 3 6 66 5".split()) #map(int, input().split())

    maxx = -1000
    runnerup = -1000
    for i in arr:
        if i > maxx:
            runnerup = maxx
            maxx = i
        elif i < maxx and i > runnerup:
            runnerup = i
    print(runnerup)  

