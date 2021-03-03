def palindrome(s):
    if(s == s[::-1]):
        return "Yes"
    return "No"

s = input()
print(palindrome(s))