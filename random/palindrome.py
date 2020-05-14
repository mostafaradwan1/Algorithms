
def palindrome(stri):
    reversed=""
    for i in range(1,len(stri)+1):
        reversed+=stri[-i]
    if reversed==stri:return True
    else:return False

print(palindrome("olla"))