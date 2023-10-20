import math as m
def main():
    n=1000
    print('#','x',' sin(x)')
    for i in range(n):
        x= (2*(m.pi)/n)*float(i)
        z= m.sin(x)
        print(i,x,z)

main()




