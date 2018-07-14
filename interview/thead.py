#encoding:utf-8

def fib(index):
    n,a,b=0,0,1
    
    while n>index:
        yield b
        a,b=b,a+b
        n+=1

fib(5)


