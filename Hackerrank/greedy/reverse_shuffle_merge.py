#!/bin/python3

import math
import os
import random
import re
import sys
import heapq
#
# Complete the 'reverseShuffleMerge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
class IteratorState:
  def __init__(self, i, buckets):
    self.i = i
    self.charsToConsume = [*buckets]
    self.numRemainingSkips = [*buckets]
    self.queryingBucket = 0

  def clone(self):
    ret = IteratorState(self.i, self.charsToConsume)
    ret.i = self.i
    ret.charsToConsume = [*self.charsToConsume]
    ret.numRemainingSkips = [*self.numRemainingSkips]
    ret.queryingBucket = self.queryingBucket
    return ret

  def proceedQueryingBucket(self): # Returns true if exhausted.
    while self.queryingBucket < 26 and self.charsToConsume[self.queryingBucket] == 0:
      self.queryingBucket += 1
    return self.queryingBucket == 26

  def consume(self, cInd):
    self.charsToConsume[cInd] -= 1

  def canSkip(self, cInd):
    return self.numRemainingSkips[cInd] >= 0

  def canConsume(self, cInd):
    return self.charsToConsume[cInd] >= 0

  def skip(self, cInd):
    self.numRemainingSkips[cInd] -= 1

  def proceed(self):
    self.i -= 1

  def getChar(self, s):
    return s[self.i]

  def __str__(self):
    strs = [
      f"I = {self.i}",
      f"Remaining Skips = {self.numRemainingSkips}",
      f"Needs Consumed = {self.charsToConsume}"
    ]
    return "\n".join(strs)


def reverseShuffleMerge(s):
    # Write your code here
    buckets = [0] * 26
    for c in s:
      buckets[ord(c) - ord('a')] += 1
    for i in range(26):
      buckets[i] = buckets[i] // 2
    skippable_chars = [*buckets]
    consumable_chars = [*buckets]
    stack = []
    for c in reversed(s):
      # print("Stack", stack)
      index = ord(c) - ord('a')
      if consumable_chars[index]:
        while stack and stack[-1] > index and skippable_chars[stack[-1]]:
          skipped = stack.pop()
          skippable_chars[skipped] -= 1
          consumable_chars[skipped] += 1
        stack.append(index)
        consumable_chars[index] -= 1
      else:
        skippable_chars[index] -= 1
    return "".join([chr(index + ord('a')) for index in stack])

      

if __name__ == '__main__':

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()
    result = reverseShuffleMerge(s)

    fptr.write(result + '\n')

    fptr.close()
