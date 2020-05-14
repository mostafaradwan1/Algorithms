def fibonaccci(num):
    if num<2:
        return num
    else:
        return fibonaccci(num-1)+fibonaccci(num-2)
print(fibonaccci(6))