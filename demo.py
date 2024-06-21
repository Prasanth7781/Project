print("HELLO")
print("SAI")
print("RASCAL")

def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    print(f)

n=int(input("Enter number:"))
fact(n)