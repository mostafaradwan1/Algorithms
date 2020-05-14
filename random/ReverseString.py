def reverse(stri):
    reversed=""
    for i in range(1,len(stri)+1):
        reversed+=stri[-i]

    return reversed

print(reverse("mostafa"))