##Check if the number is power of 2 or not

def power(x):

    return (x and (not(x & (x - 1))) )


x=int(input("enetr a value of x :"))

if (power(x)):
    print('Yes')
else:
    print('No')
x=int(input("enetr a value of x :"))
if (power(x)):
    print('Yes')
else:
    print('No')
