def fibo(n):
    if n==1 or n==2:
        return n-1
    else:
        return fibo(n-1)+fibo(n-2)

def odd_eve(n):
    if n==0:
        return
    else:
        odd_eve(n-1)
        if n%2==0:
            print("even : ",n)
        else:
            print("odd : ",n)

def fact(n):
    if n==1:
        return 1
    else:
        return (n*fact(n-1))

n=int(input("enter the value : "))
print(fact(n))