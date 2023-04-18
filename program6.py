##WAP to find the ones and zeros in number using bitwise operators in c
def Dec(num):
    return "{0:b}".format(int(n))
n=input("enter a values of num :")

z=Dec(n)
print({z})
count0=0

ch="0"

for i in z:
    if i==ch:
        count0=count0+1


print("count0",count0)
count1=len(z)-count0
print("count1",count1)


