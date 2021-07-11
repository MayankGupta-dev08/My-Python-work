def decimalToBinary(n):
    x = 1
    result = 0;
    while(x<=n):
        x *= 2
    x //= 2
    
    while(x>0):
        lastDigit = n//x
        n -= lastDigit*x
        x //= 2
        result = result*10 + lastDigit

    return result

if __name__ == "__main__":
    n = int(input());
    print(decimalToBinary(n))
    