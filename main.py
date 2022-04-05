"""
Given a number as input, convert it into binary
Input-> 8
Output-> Binary=1000
"""

def deci_to_binary(n):
  if n>=1:
    deci_to_binary(n//2)
  binary = n%2
  print(binary, end="")

num = 8
deci_to_binary(num)