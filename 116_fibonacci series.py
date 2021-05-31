'''FIBONACCI SERIES -   [0,1,1,2,3,5,8,13,21,34....]'''

def fib(n):
    if n < 2:
        if n == 1:
            return 1
        else:
            return 0
    else:
        return fib(n-1)+fib(n-2)


if __name__ == "__main__":
    try:
        n = int(input("Enter the number till which u want fibonacci series: "))
        l1 = []
        for i in range(n):
            l1.append(fib(i))
        print(l1)
    except ValueError as e:
        print("Make sure you enter a number!!")
    finally:
        print("Thanks for using the code!!")
