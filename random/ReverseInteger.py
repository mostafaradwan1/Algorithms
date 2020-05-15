def reverse_integer(num):
    reversed_integer=0
    while num != 0 and num !=-1:

        n=num%10
        reversed_integer=(reversed_integer*10) +n
        num//=10
        print(reversed_integer)
    return reversed_integer 
           
print(reverse_integer(15000))