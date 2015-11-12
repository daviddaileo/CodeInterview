#!/home/daiwei/anaconda/bin/python

import os
import sys

def SmallestMultiple(n):
    tmp=1
    if n==0:
      return 0
    elif n==1:
      return 1
    else:
      for i in range(n):
          tmp = lcm(tmp,i+1)
      return tmp

def gcd(m,n):
    while(n!=0):
      tmp = n
      n = m%n
      m = tmp
    return m

def lcm(m,n):
    return m*n/gcd(m,n)
