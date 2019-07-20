# Date: 7/19/19
# https://www.hackerrank.com/challenges/write-a-function/problem
# Hackerrank python challenges

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        leap = True
    else:
        leap = False
    
    return leap

year = 4000 #int(input())
print(is_leap(year))