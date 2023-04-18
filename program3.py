###Remove the last set bit of a number

def fun(n):
    return n & (n - 1)

n = int(input("enter a values : "))
print("The number after unsetting the rightmost set bit", fun(n))


s={10,20,30,40}
s.remove(40)
print(s)

