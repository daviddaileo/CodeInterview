#!/home/daiwei/anaconda/bin/python

import os
import sys

def buildSubsequences(s):
      ss=list()
      n=len(s)
      if n==0:
       return ''
      elif n==1:
       ss.append(s)
       return ss
      else:
        tmp = s.replace(s[n-1],'')
        ss.append(s[n-1])
        for elem in buildSubsequences(tmp):
            ss.append(elem)
            ss.append(elem + s[n-1])
        return sorted(ss) 
