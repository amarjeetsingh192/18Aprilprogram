##Set the ith bit of a number
def setbit(n, k):
    return ((1 << k) | n)
n = int(input("enter a number :"))
k = int(input("enter a number :"))

print("Kth bit set number = ",setbit(n, k))
