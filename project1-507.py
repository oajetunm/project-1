import math
# Problem 2. Palindromes
#
# Given a string, determine if the string is a palindrome.
#
# Examples:
#     palidrome('anna')  returns 'True'
#     palidrome('abcdef')  returns 'False'
#     palidrome('')  returns 'True'

def palindrome(s):


    def removeWhite(s):
        if len(s) <=1:
            if s[0] == ' ':
                return ''
            elif s[0] == "'":
                return s[0]
            else:
                return s[0]
        else:
                return removeWhite(s[0]) + removeWhite(s[1:])
    def reverse(s):
        if len(s) <= 1:
            return s
        else:
            return reverse(s[-1]) + reverse(s[:-1])

    if s== reverse(s):
        return True
    else:
        return False


  # return '' ### Replace with your code


def test(got, expected):
  score = 0;
  if got == expected:
    score = 3.33;
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score

def main():
  total = 0;
  print()
  print ('Task C: palindromes' """Each OK is worth five points.""")

 #  """ If this is what you get, you are good to go. Each OK is worth five points.
 # OK  Got:  True Expected:  True
 # OK  Got:  False Expected:  False
 # OK  Got:  True Expected:  True
 #  """
  total += test(palindrome('anna'), True)
  total += test(palindrome('bookkeeper'), False)
  total += test(palindrome('a'), True)

  print("You final score is: ", math.ceil(total))

if __name__ == '__main__':
  main()
