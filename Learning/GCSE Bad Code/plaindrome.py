def palindrome(word):
  palindrome = "false"
  n = len(word)-1
  for i in range (0,n):
    if word[i] != word[n-1]:
        palindrome = "true"
    else:
        palindrome = "false"
    if palindrome == "true":
        return True
    else:
        return False

print (palindrome("racecar"))