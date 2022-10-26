def serialNo(n):
    if n>0:
        serialNo(n-1)
        print(n, end=' ')
    return

if __name__ == '__main__':
    serialNo(5)
