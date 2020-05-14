# version 1
def reverse(stri):
    reversed=""
    for i in range(1,len(stri)+1):
        reversed+=stri[-i]

    return reversed
    

# version 2

def reverse1(stri):
    reversed=''
    for char in stri:
        reversed=char +reversed
    return reversed


print(reverse("mostafa"))