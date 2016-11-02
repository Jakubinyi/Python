def fibonacci(n):
    print("fibonacci: "+str(n))
    if n == 0:        #vagy: if n == 0 or n ==1:    vagy: if < 2
        return 0      #          return n                    return n
    elif n == 1:      # töröl
        return 1      # töröl
    else:
        return (fibonacci(n-1)+fibonacci(n-2))