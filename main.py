import math
import os

def nomatch(str):
    s=[None]*len(str)
    for i in range(len(str)):
        s[i]=str[i]

    print(s)
    numberOfDeletion=0
    for i in range(1,len(s),1):
        if s[i]==s[i-1]:
            #s.remove(s[i-1])
            numberOfDeletion+=1
    print(numberOfDeletion)


if __name__ == '__main__':
    for i in range(int(input())):
        nomatch(input())
