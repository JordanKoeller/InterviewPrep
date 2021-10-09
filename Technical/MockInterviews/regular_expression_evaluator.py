"""
Write a function that takes two strings as arguments, s and p
and returns a bool denoting s matches p

p is a sequence of the folloiwng:
  1. a-z
  2. . = wildcard
  3. * = 0 or more matches of the previous character

Examples:

  s = "aba", p ="ab"
  s = "aa", p = "a*"
  s = "ab", p = ".*"
  s = "aab", p = "c*a*b" => true
"""
from collections import deque

def matches(s, p, sI, pI):
  return p[pI] == '.' or s[sI] == p[pI]


def regMatch(s, p):
  stack = deque()
  stack.append((0, 0))
  if s == '' and len(p) == 2 and p[1] == '*':
    return True
  while stack:
    sI, pI = stack.pop()
    if sI >= len(s) and pI >= len(p):
      return True
    if pI >= len(p) or sI >= len(s): # Maybe get rid of this depending on what I push
      continue
    if pI+1 < len(p) and p[pI+1] == '*':
      if matches(s, p, sI, pI):
        stack.append((sI+1, pI))
        stack.append((sI+1, pI+2))
      else:
        stack.append((sI, pI+2))
    elif matches(s, p, sI, pI):
      stack.append((sI+1, pI+1))
  return False 

print(regMatch('aba', 'ab'))
print(regMatch('aa', 'a*'))
print(regMatch('aa', '.'))
print(regMatch('aa', '.*'))
print(regMatch('aab', 'c*a*b'))
print(regMatch('abababaa', 'a.*a'))
print(regMatch('abababaa', 'a.*b.*'))
print(regMatch('', '.*'))