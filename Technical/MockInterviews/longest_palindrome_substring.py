"""
Find the number of palindromic substrings the string has.

Input: = 'abc'
Palindormes: ['a', 'b', 'c']
Output: 3

Input: = 'aaa'
palindromes: ['a', 'a', 'a', 'aa', 'aa', 'aaa']
Output: 6

Input string is NOT empty
"""

"""
Answer is always >= len(input)

O(n^2):
For each charater in input:
  use a stack to find palindromes
  Increment a counter by 1 for every palindrome found

Finding palindromes with our stack:
  1. We don't know when we should add to the stack or not.
      if stack.peek() == currentChar:
          we are not popping
      otherwise: stack.push()
     Counterexample: aabaab
  2. We need to do both. We need a version of the stack where we increment and one where we decrement.
  
When we see a new character != previous, We have to:
  1) Assume this is another character in any palindromes that are still increasing length.
  2) Terminate any palindromes that were decreasing.
  3) Start a new palindrome at this location
  4) if this character equals the previous previous, start decreasing any existing palindromes.
When we see a new character that IS equal to the previous, we have to:
  1) Assume this is another character in any previous palindromes
  2) Start decreasing any existing palindromes.
  3) Terminate any palindromes that that this new character breaks
  4. Start a new palindrome at this location

Start at palindrome centers:
  Make an array of all the places I see aAa -> center of a palindrome
                                  I see aa  -> center of a palindrome
                                    Two pointers solution going out from each possible start point.
                                  aaaaaaaaa

  current_palindromes = [] # array of the (substr Length, pivot point)
  for character in string:
    for substr, pivot in current_palindromes:
      if pivot is not None:
        characterToMatch = string[pivot - (i - pivot)]
        if character == characterToMatch:
          palindrome is still going
      else:


Optimization (sliding window):
  abcba -> ['a', 'b', 'c', 'b' 'a', 'bcb', 'abcba']
  When I find a "long" palindrome I can add length(palindrome) // 2 - 1 to the counter (ODD max stack)

  abba ->['a', 'b', 'b', 'a', 'bb', 'abba'] -> length(palindrome) // 2 to the counter (EVEN max stack)
"""

def get_num_palindromes_around_plateau(string, pivot): # aBBa
  i = 1
  count = 1
  while pivot - i >= 0 and pivot + i + 1 < len(string):
    if string[pivot - i] == string[pivot + i + 1]:
      count += 1
      i += 1
    else:
      return count
  return count

def get_num_palindromes_around_peak(string, pivot):    # aBa
  i = 1
  count = 0
  while pivot - i >= 0 and pivot + i < len(string):
    if string[pivot-i] == string[pivot+i]:
      count += 1
      i += 1
    else:
      return count
  return count

def num_palindromes(string):
  total_num_pali = len(string)
  for i in range(len(string) -1):
    if string[i] == string[i+1]:
      total_num_pali += get_num_palindromes_around_plateau(string, i)
    total_num_pali += get_num_palindromes_around_peak(string, i)
  return total_num_pali

def test_pali(string):
  count = num_palindromes(string)
  print(f"String {string} had {count} palindromes")

#Complexity: O(n^2) time (worst case), O(1) space
           

test_pali("aaa")
test_pali("aa")
test_pali("aba")
test_pali('aabbaab') # 7 + [aa, bb, aa, aabbaa, abba, baab]