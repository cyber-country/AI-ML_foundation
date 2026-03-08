def sumlist(n):
    total=0
    for i in range(len(n)):
        total+=n[i]
    return total
def sum(a,b):
    return a+b
def sub(b,a):
    return b-a
def mul(a,b):
    return a*b
def div(b,a):
    return b/a
def maker(n):
    s=[]
    for j in range(n):
        s.append(input())
    return s