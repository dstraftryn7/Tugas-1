def cekPalindrome(s):
      return s == s[::-1]

s = "rotator"
ans = cekPalindrome(s)

if ans:
      print("ya palindrome")
else:
      print("bukan palindrome")

